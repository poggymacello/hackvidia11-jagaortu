# Arsitektur MVP JagaOrtu (untuk 24 jam)

Dokumen desain saja, **tanpa kode**. Kode ditulis saat Hacking Day. Arsitektur ini adalah versi 24 jam dari Gambar 2 proposal; tabel konsistensi ada di §6.

## 1. Komponen
```
 HP "Penipu" (nomor ke-3)            HP "Ibu" (Android 13–15)                         Cloud (HTTPS)                         HP "Rina"
 ───────────────────────            ─────────────────────────────                   ─────────────────────────              ───────────────────
 kirim WA / SMS  ─────────────────▶ WhatsApp/SMS → notifikasi                       Backend FastAPI                        Pendamping (PWA)
                                     │                                              ├─ /analisis   (L2 LLM)               ├─ daftar kejadian
                                     ▼                                              ├─ /pendamping (kirim push)           ├─ ringkasan risiko
                                    JagaOrtu Ibu (Kotlin)                           ├─ /event      (log tanpa isi)        ├─ tombol Telepon Ibu (tel:)
                                     ├─ NotificationListenerService                 ├─ penyamaran PII (lapis kedua)       └─ Web Push (service worker)
                                     ├─ L0 aturan (offline)                         ├─ TTS cloud (id-ID, su-ID)
                                     ├─ L1 model ringan (offline)  ── ambigu ──▶     └─ DB: event & langganan push
                                     ├─ penyamaran PII (lapis pertama)  ◀── JSON ──     (SQLite/PostgreSQL)
                                     ├─ peringatan: heads-up + layar besar + TTS
                                     └─ "Tanya Rina dulu" ─────────────────────────▶ /pendamping ───── push ──────────────▶ HP bergetar
 Cadangan demo: Simulasi web (chat mirip WA) ──────────────────────────────────────▶ /analisis (backend yang sama)
```

## 2. Alur keputusan (yang ditunjukkan di log saat demo)
1. **Sumber.** Notifikasi dari paket WhatsApp (`com.whatsapp`, `com.whatsapp.w4b`) atau aplikasi SMS default. Diambil: nama/nomor pengirim (judul notifikasi), teks yang tampil, waktu. Notifikasi dari kontak tersimpan dan grup diabaikan secara bawaan (ikuti A8 "izin terbatas"). Pesan suara/foto hanya muncul sebagai label ("Pesan suara", "Foto"); itu batas WhatsApp, lihat proposal §4.5.
2. **L0 aturan (di HP, < 50 ms).** Skor aturan dari: permintaan uang/transfer + urgensi ("sekarang", "segera", "darurat"), permintaan OTP/PIN/kode, "nomor baru"/"ganti nomor", tautan (domain dicek ke daftar contoh + pola penyingkat URL), nama file `.apk`, kata "jangan bilang", serta nomor/rekening di daftar contoh terlapor. Satu aturan "pasti" (mis. `.apk` atau minta OTP) → **risiko tinggi**, langsung ke peringatan.
3. **L1 model ringan (di HP, < 100 ms).** TF-IDF karakter/kata + regresi logistik, dilatih saat final dari dataset berlabel. Bobot diekspor ke JSON lalu dihitung sebagai perkalian titik di Kotlin. Skor < 0,4 → **Hijau** (diam); ≥ 0,7 → **Merah**; **0,4–0,7 = ambigu → L2** (sama dengan proposal Tabel 5). L2: tinggi → Merah, sedang → **Kuning** (notifikasi bersuara tanpa layar penuh, Pendamping tidak diberi tahu kecuali Ibu menekan tombol), rendah → Hijau. **Aturan monoton:** L2 tidak boleh menurunkan putusan L0, dan untuk pesan berisi uang/tautan/file tidak boleh di bawah Kuning (pertahanan injeksi prompt; siapkan 3 pesan injeksi untuk demo log).
4. **Penyamaran PII** sebelum keluar HP: nomor telepon → `<NOMOR>`, deret ≥8 digit → `<ANGKA>`, nama pengirim → `<PENGIRIM>`, nama kontak/keluarga → `<NAMA>`, tautan → domain saja. Backend menjalankan penyamaran ulang sebagai lapis kedua.
5. **L2 LLM (cloud, target < 4 dtk).** Masukan: teks tersamar + sinyal L0/L1. Keluaran JSON tetap: `risiko` (rendah/sedang/tinggi), `modus` (8 kelas taksonomi proposal + aman), `tanda_bahaya` (≤3, kalimat pendek), `penjelasan_lansia` (≤2 kalimat, tanpa istilah teknis), `saran` (≤2), `bahasa`. Suhu rendah; validasi skema; jika gagal atau timeout → **Kuning** (fail-safe) dengan saran bawaan "Tanya Rina dulu".
6. **Peringatan (L3 manusia).** Heads-up notification "Tunggu dulu, Bu" + layar besar (A3) + TTS otomatis. Dua aksi: **Tanya Rina dulu** (utama) dan **Ini aman** (umpan balik → dicatat untuk menurunkan alarm palsu). JagaOrtu **tidak pernah** memblokir pesan, mentransfer, atau membalas atas nama Ibu.
7. **Pendamping.** Backend mengirim push ke Rina berisi **ringkasan** (modus, tanda bahaya, waktu, tingkat risiko). Isi pesan asli **tidak** dikirim. Tombol "Telepon Ibu". Bila tidak dibuka dalam 10 menit (mode demo: 30 dtk) → push ke pendamping cadangan.

## 3. Data yang disimpan (minimisasi, sesuai UU 27/2022 di proposal)
| Data | Disimpan? | Di mana | Lama |
|---|---|---|---|
| Isi pesan asli | **Tidak** (hanya di memori HP saat analisis) | — | — |
| Teks tersamar yang dikirim ke LLM | Tidak disimpan backend (log demo hanya di layar) | — | — |
| Event: waktu, modus, skor, lapis pemutus, aksi Ibu | Ya | DB backend | 30 hari (kebijakan) |
| Langganan push Pendamping | Ya | DB backend | sampai dicabut |
| Kunci API | Variabel lingkungan server, **tidak di repo / APK** | — | — |

## 4. Pilihan teknologi (semua tersedia publik; cek lisensi saat final)
| Bagian | Pilihan utama | Alternatif bila macet |
|---|---|---|
| Android | Kotlin, minSdk 26, targetSdk 34/35; NotificationListenerService; Foreground service; `TextToSpeech` (id-ID) | — |
| TTS Sunda | TTS neural cloud (suara su-ID) **atau** rekaman penutur asli untuk 3–5 frasa tetap | Bahasa Indonesia saja (sebut jujur) |
| Backend | Python FastAPI (sesuai proposal), hosting HTTPS (Cloud Run/Render/Railway) | Satu VPS + Caddy (HTTPS otomatis) |
| DB | SQLite (MVP) → PostgreSQL (sesuai proposal untuk produksi) | — |
| LLM | API LLM komersial dengan keluaran JSON terstruktur (pilih yang kuotanya sudah dicek) | LLM kedua sebagai cadangan; cache respons pesan demo |
| Push | Web Push (VAPID) ke PWA Pendamping | Halaman Pendamping terbuka + SSE/WebSocket |
| L1 | scikit-learn (latih) → bobot JSON → Kotlin | Skor heuristik berbobot (sebut sebagai L1 v0) |

## 5. Batasan platform yang memengaruhi demo (lihat proposal §4.5 & BANK_QnA)
- **APK sideload:** akses notifikasi harus dibuka lewat *Info aplikasi → ⋮ → Izinkan setelan terbatas* (Android 13+). Latih langkah ini sebelum pitch.
- **Android 15:** isi notifikasi yang mengandung OTP disensor untuk listener biasa. Jangan memakai SMS OTP sebagai pesan demo; pakai pesan "minta kode" dari penipu (pesan itu sendiri tidak berisi OTP).
- **WhatsApp:** hanya teks pratinjau notifikasi. Pastikan pratinjau pesan aktif dan chat penipu **tidak dibisukan/diarsipkan** di HP Ibu.
- **CallScreeningService (P2):** perlu peran ROLE_CALL_SCREENING dari pengguna, hanya panggilan seluler, respons ≤5 dtk, tanpa audio. Panggilan WA tidak lewat sini.
- **Full-screen intent** dibatasi di Android 14+; pakai heads-up + TTS otomatis, lalu Ibu mengetuk notifikasi untuk layar besar.

## 6. Konsistensi dengan proposal (10% nilai final)
| Proposal | MVP 24 jam | Status yang dikatakan saat pitch |
|---|---|---|
| Penjaga Otomatis WA/SMS (NotificationListenerService) | Ya | "jalan" |
| L0 aturan pasti | Ya | "jalan" |
| L1 model di perangkat: linear TF-IDF di MVP, TFLite di pilot (proposal §7) | Regresi logistik TF-IDF di perangkat | "sesuai proposal: linear di MVP, TFLite di pilot" |
| L2 LLM hanya untuk kasus ambigu, data disamarkan | Ya + log | "jalan; lihat log" |
| L3 manusia memutuskan | Ya (tidak ada pemblokiran otomatis) | "jalan" |
| Tingkat Kuning/Merah + aturan monoton (Tabel 5) | Ya, di log | "jalan; lihat log injeksi prompt" |
| Peringatan bersuara bahasa ibu | Indonesia (+ Sunda frasa tetap) | Jawa: roadmap |
| Aturan Dua Orang + eskalasi 10 menit | Ya (timer demo 30 dtk) | "jalan" |
| Tanya Dulu | P1 (suara) / minimal teks | sesuai hasil |
| Verifikasi Keluarga (CallScreening) | P2 | bila tidak sempat: "roadmap; ini batasan platformnya" |
| Latihan Waspada | P2 | roadmap |
| OCR (ML Kit) | Tidak | roadmap |
| Google Safe Browsing | Opsional (daftar domain contoh dulu) | sebut jujur |
| Aplikasi Pendamping PWA + push | Ya | "jalan" |
