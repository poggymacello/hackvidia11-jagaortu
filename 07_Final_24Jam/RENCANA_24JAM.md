# Rencana Hacking Day 24 jam: JagaOrtu (final 29–31 Jan 2027, ITB)

> **Aturan yang membentuk rencana ini** (guidebook Hackvidia 11.0):
> - 24 jam non-stop di area karantina.
> - Repo GitHub wajib, dan akun panitia diundang **sejak awal**.
> - **4 checkpoint commit, tiap 6 jam.**
> - **Semua kode dibuat saat final.**
> - API/model AI pihak ketiga boleh; aset harus open source atau public domain.
> - Pitch 5 menit (deck + **demo live**) + tanya-jawab, ditambah video demo ≤5 menit.
>
> Bobot final: prototipe 25 · AI 20 · tema & validasi dampak 15 · bisnis 15 · **konsistensi dengan proposal 10** · pitch & QA 15.
> Jam di bawah ditulis relatif (**H+0** = mulai hacking). Sesuaikan dengan jadwal resmi dari technical meeting 18 Jan.

## 1. Prinsip
1. **Demo dulu, fitur kemudian.** Pada H+12 alur inti "WA penipuan → peringatan bersuara di HP Ibu → HP Rina bergetar" sudah harus jalan end-to-end, walau masih jelek.
2. **Konsisten dengan proposal.** Yang dibangun adalah fitur di proposal, Tabel 4 baris "0. MVP": Penjaga Otomatis WA/SMS, peringatan bersuara, Tanya Dulu, notifikasi Pendamping. Yang tidak sempat dikerjakan **disebut jujur** sebagai roadmap. Jangan pivot diam-diam.
3. **"AI secukupnya" harus terlihat.** Setiap keputusan dicatat di log: L0 aturan / L1 model ringan / L2 LLM / L3 manusia, beserta waktunya. Log ini ditampilkan saat demo.
4. **Selalu ada jalur cadangan:** (a) Android asli → (b) simulasi web yang memakai backend yang sama → (c) video demo yang direkam pada H+20.

## 2. Ruang lingkup MVP (dikunci sebelum final; jangan ditambah saat hacking)
| Prioritas | Fitur | Definisi selesai |
|---|---|---|
| **P0** | Android "JagaOrtu Ibu": *NotificationListenerService* membaca notifikasi WhatsApp & SMS | Notifikasi WA dari nomor tak dikenal muncul di log aplikasi < 2 dtk |
| **P0** | L0 mesin aturan (kata kunci transfer/OTP/"nomor baru", tautan, `.apk`, daftar nomor/rekening contoh) | 10 pesan uji: semua pesan "jelas penipuan" tertangkap tanpa LLM |
| **P0** | L2 LLM via backend, dengan **penyamaran PII** sebelum dikirim; keluaran JSON (modus, tanda bahaya, penjelasan sederhana, saran) | Pesan ambigu → JSON valid < 5 dtk; log menunjukkan teks yang sudah disamarkan |
| **P0** | Peringatan: notifikasi *heads-up* + layar peringatan besar + **TTS** otomatis (Indonesia; Sunda dari audio TTS cloud) | Suara terdengar tanpa menyentuh HP |
| **P0** | Tombol "Tanya Rina dulu" → backend → **Pendamping web (PWA) + push** | HP Rina bergetar < 5 dtk; Rina melihat ringkasan risiko, **bukan isi chat**; tombol "Telepon Ibu" (`tel:`) |
| **P0** | **Simulasi web cadangan**: halaman chat mirip WA yang mengirim pesan ke backend yang sama | Bisa menjalankan seluruh demo tanpa HP Android |
| P1 | L1 model ringan: TF-IDF + regresi logistik dilatih saat final, bobotnya dijalankan di HP | Skor L1 tampil di log; ambang ambigu 0,4–0,7 → L2 |
| P1 | Eskalasi ke pendamping cadangan (10 menit; mode demo 30 dtk) | Cadangan menerima push setelah timer |
| P1 | Tanya Dulu suara: SpeechRecognizer → LLM → TTS | Ibu bercerita, dijawab dengan suara |
| P2 | *CallScreeningService*: panggilan seluler dari nomor tak tersimpan → pengingat kata sandi keluarga | Muncul pengingat saat ditelepon nomor ketiga |
| P2 | Latihan Waspada: Rina mengirim simulasi penipuan aman | Ibu menerima simulasi + pelajaran 30 dtk |
| ✗ | iOS, deteksi deepfake suara, membaca isi chat penuh, integrasi bank | Disebut sebagai batasan/roadmap |

## 3. Pembagian peran
### Tim 4 orang
| Kode | Peran | Tanggung jawab utama |
|---|---|---|
| **A** (Ketua) | Arsitek + backend + keamanan | Repo, backend API, L0 aturan, penyamaran PII, log keputusan, checkpoint commit, pitch utama |
| **B** | AI engineer | Prompt & skema JSON LLM, evaluasi 30 pesan uji, L1 model, TTS (Indonesia/Sunda), STT |
| **C** | Android | NotificationListener, foreground service, layar peringatan, TTS playback, tombol Tanya Rina, (P2) CallScreening |
| **D** | Web Pendamping + UX + pitch | PWA Pendamping + push, simulasi web, deck, naskah demo, video demo, latihan Q&A |

### Tim 3 orang
A = arsitek + backend + L0 + **web Pendamping**; B = AI + **deck & video demo**; C = Android. Pitch dibagi A (utama) & B (demo).
Turunkan semua P1/P2 kecuali L1.

### Tim 2 orang
A = backend + AI (LLM, TTS) + web Pendamping (versi sederhana: halaman yang auto-refresh/SSE + Web Push bila sempat); B = Android + simulasi web.
L1 diganti **skor heuristik berbobot** (dijelaskan jujur sebagai versi awal L1). Deck disusun bersama pada H+18–H+20. Tidak ada P1/P2.

## 4. Jadwal jam demi jam
Commit tiap ±1 jam. **Checkpoint wajib** (panitia memeriksa): **CP1 H+6, CP2 H+12, CP3 H+18, CP4 H+24**. Di setiap checkpoint, isi `CHANGELOG.md` di repo: apa yang jalan, apa yang belum.

| Jam | A (backend/ketua) | B (AI) | C (Android) | D (web/pitch) |
|---|---|---|---|---|
| **H+0–0:30** | Buat repo, **undang akun panitia**, struktur folder, `README` + `.gitignore` (kunci API tidak di-commit) | Uji akses API LLM & TTS dari laptop (curl), cek kuota | Buat proyek Android, uji install di HP Ibu (izin setelan terbatas) | Buat proyek web, siapkan hosting HTTPS |
| H+0:30–3 | Endpoint `analisis` + L0 aturan + log keputusan | Prompt v1 + skema JSON; daftar 30 pesan uji (15 penipuan, 10 aman, 5 ambigu) | NotificationListener: tangkap WA/SMS → kirim ke backend | Simulasi chat web → endpoint `analisis` |
| H+3–6 | Penyamaran PII; endpoint `tanya-pendamping`; simpan event (tanpa isi pesan) | TTS: frasa tetap (Indonesia & Sunda) + TTS dinamis | Layar peringatan + heads-up + putar TTS | Pendamping web: daftar event + ringkasan + `tel:` |
| **H+6 · CP1** | ✅ Commit: backend jalan, L0 menangkap pesan uji, simulasi web memanggil API | | | |
| H+6–9 | Integrasi L2 ke `analisis` (hanya untuk skor ambigu); timeout & fallback ke "Tanya Rina dulu" bila LLM gagal | Evaluasi 30 pesan → tabel recall/alarm palsu (untuk deck) | Tombol "Tanya Rina dulu" → API → konfirmasi "Rina sudah diberi tahu" | **Web Push** (service worker + izin notifikasi) |
| H+9–12 | **Uji end-to-end** dengan 3 HP sungguhan (penipu → Ibu → Rina) | Perbaiki prompt dari hasil evaluasi | Perbaiki bug Android dari uji | Polishing Pendamping (huruf besar, satu aksi utama) |
| **H+12 · CP2** | ✅ Commit: **alur inti end-to-end jalan di HP asli** (kalau belum: putuskan fokus ke simulasi web untuk demo) | | | |
| H+12–13 | **Istirahat bergilir** (tidur 2×90 menit per orang dijadwalkan di H+12–18; minimal 1 orang selalu bangun) | | | |
| H+13–16 | P1: eskalasi cadangan + log keputusan tampil di layar | P1: L1 TF-IDF+logreg → ekspor bobot → serahkan ke C | P1: jalankan L1 di HP; tampilkan skor | Deck v1 (masalah, validasi, solusi, arsitektur, bisnis) |
| H+16–18 | Hardening: mode demo (timer 30 dtk), data contoh daftar nomor/rekening | P1: Tanya Dulu suara (bila sempat) | P2: CallScreening (hanya bila P0+P1 stabil) | Naskah pitch v1 + latihan pertama |
| **H+18 · CP3** | ✅ Commit: P0 stabil + P1 yang sudah jadi. **Feature freeze** (tidak ada fitur baru setelah ini) | | | |
| H+18–20 | Uji ulang end-to-end 5× berturut-turut; catat kegagalan | Siapkan angka evaluasi untuk slide | Perbaiki bug saja | **Rekam video demo cadangan** (layar HP + kamera) |
| H+20–22 | Latihan pitch 3× dengan stopwatch + demo live | Latihan Q&A (BANK_QnA_25) | Siapkan HP demo (baterai, mode Jangan Ganggu kecuali WA/SMS, volume) | Edit video demo ≤5 menit, unggah |
| H+22–23:30 | README repo: cara menjalankan, arsitektur, batasan, **pernyataan aset & API pihak ketiga** | Gladi bersih | Gladi bersih | Finalisasi deck (PDF + offline) |
| **H+24 · CP4** | ✅ Commit final + tag `final`; kumpulkan semua berkas sesuai instruksi panitia | | | |

## 5. Hal yang boleh dan tidak boleh disiapkan sebelum final
| Boleh (bukan kode) | **Tidak boleh** |
|---|---|
| Wireframe/desain (sudah ada di proposal), palet warna, ikon open source | Menulis kode aplikasi, backend, skrip, atau notebook |
| **Daftar pesan penipuan & aman berlabel** (CSV/teks) dari sumber publik, untuk evaluasi | Template proyek yang sudah berisi kode buatan sendiri |
| Akun & kuota: API LLM, TTS cloud, hosting, Firebase (tanpa kode) | Model yang dilatih sebelum final |
| HP demo: WA terpasang, nomor aktif, Android 13–15, opsi developer | Menyimpan kode di gist/repo lain lalu menyalinnya |
| Rencana, naskah pitch, bank Q&A (dokumen ini) | |
| Rekaman suara frasa peringatan Sunda oleh penutur asli (aset buatan sendiri) | |

> Tanyakan di technical meeting 18 Jan: (1) bolehkah dataset uji dan prompt teks disiapkan sebelum final; (2) jam mulai/akhir dan detail checkpoint; (3) ketersediaan listrik & internet di karantina. Catat jawabannya.

## 6. Risiko & rencana cadangan
| Risiko | Tanda | Tindakan |
|---|---|---|
| Internet karantina lambat | LLM > 5 dtk | Hotspot sendiri (2 operator berbeda); L0/L1 tetap jalan offline; LLM timeout 4 dtk → tampilkan peringatan L0 |
| WhatsApp tidak memunculkan notifikasi (chat dibisukan/arsip, pratinjau mati) | Log kosong | Cek pengaturan notifikasi WA di HP Ibu; cadangan: SMS; cadangan 2: simulasi web |
| Izin akses notifikasi abu-abu (APK sideload) | Toggle tidak bisa diaktifkan | Info aplikasi → ⋮ → **Izinkan setelan terbatas** → aktifkan akses notifikasi (latih sebelum pitch) |
| Push ke Rina tidak sampai | HP Rina diam | Pendamping web dibuka di layar (fallback realtime), HP Rina tidak terkunci |
| Kuota/biaya API habis | Error 429 | Kunci API cadangan + batas penggunaan; respons LLM untuk 3 pesan demo di-cache |
| Bug di menit terakhir | — | Feature freeze H+18; tag Git `demo-stabil` di setiap versi yang lolos uji 5× |
| Anggota kelelahan | — | Jadwal tidur bergilir; makan teratur; satu orang "penjaga build" |
