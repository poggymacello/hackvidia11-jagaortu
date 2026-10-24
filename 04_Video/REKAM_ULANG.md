# Rekam ulang video Hackvidia (wajah & suara tim)

**Kenapa direkam ulang:**
1. Guidebook meminta video berisi **perkenalan tim** + masalah, cara kerja AI, walkthrough wireframe, serta kelayakan & dampak. Video sekarang hanya berisi narasi TTS dan slide nama, tanpa wajah atau suara tim.
2. Segmen 01 video sekarang memuat klaim "10 detik rekaman" dengan sumber yang tidak tepat. Versi benar: **McAfee (2023): 3 detik rekaman cukup untuk tiruan suara dengan kecocokan ±85%**.
3. Kalimat bahasa Sunda belum dicek penutur asli.

**Batas:** ≤ 5:00 (target 4:30–4:45). YouTube **unlisted**, judul `<NamaTim> - JagaOrtu - Hackvidia 11.0`.
**Alat:** HP untuk kamera (1080p, mode lanskap), mikrofon clip-on/earphone ber-mic, ruangan sepi, cahaya dari depan (jendela). Edit: Clipchamp (bawaan Windows 11), CapCut, atau DaVinci Resolve.
**Bahan visual siap pakai:** slide `build/slides/s00–s24.png` (1920×1080), wireframe `03_Wireframe/A1–A8.png`, arsitektur `build/arch.png`. Slide 00/01 sudah diperbarui di `build/video.py` (3 detik, McAfee); render ulang slide dengan `build_all.py --only video` jika ffmpeg tersedia, atau pakai teks baru di bawah sebagai *text overlay* di editor.

---

## Naskah revisi (± 4:40)
Kode: **[KAM]** = wajah di kamera · **[VO]** = suara tim di atas slide/wireframe · **[LAYAR]** = rekaman layar/gambar. Nama anggota di `[...]` diisi sendiri.

| # | Waktu | Visual | Siapa | Ucapan |
|---|---|---|---|---|
| 1 | 0:00–0:12 | [LAYAR] bubble WA gelap (slide s00) | suara laki-laki (anggota) | "Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer lima juta sekarang, ya. Jangan bilang Papa dulu." |
| 2 | 0:12–0:25 | [LAYAR] slide s01 baru ("3 detik", sumber McAfee 2023) | [VO] P1 | "Pesan seperti ini datang setiap hari ke ponsel orang tua kita. Dan kini suaranya pun bisa dipalsukan: riset McAfee menunjukkan tiga detik rekaman sudah cukup untuk membuat tiruan suara yang mirip." |
| 3 | 0:25–0:55 | **[KAM]** semua anggota dalam satu frame (berdiri/duduk berjajar), lalu potongan close-up tiap orang 3–4 detik dengan *lower-third* nama · prodi · kampus | Tiap anggota bicara sendiri | Ketua: "Halo, kami Tim **[NamaTim]** dari Hackvidia Arkavidia 11.0. Saya **[nama]**, **[prodi, kampus]**, mengurus arsitektur dan keamanan." → A2: "Saya **[nama]**, **[prodi, kampus]**, di bagian AI." → A3: "Saya **[nama]**, Android dan backend." → A4: "Saya **[nama]**, riset pengguna dan bisnis." → Ketua: "Pertanyaan kami: bagaimana melindungi orang tua dari penipuan digital, **tanpa merampas kemandirian mereka**?" |
| 4 | 0:55–1:30 | [LAYAR] slide data s03–s06 | [VO] A4 | "IASC OJK menerima 702.342 laporan penipuan sejak November 2024. Modus menyamar keluarga atau petugas menimbulkan kerugian terlapor terbesar, 2,09 triliun rupiah. Literasi keuangan usia 51 sampai 79 tahun hanya 54,55 persen, sementara lansia yang online naik dari 14 menjadi 34 persen. Jawa Barat mencatat laporan terbanyak." |
| 5 | 1:30–1:55 | **[KAM]** A4 di lokasi wawancara (tanpa wajah lansia kecuali diizinkan) **atau** [LAYAR] slide insight s07 | [KAM/VO] A4 | "Kami mewawancarai **[n]** lansia di Bandung dan menyurvei **[n]** anak dewasa. **[1 temuan asli + kutipan, mis. "Kalau sudah dengar anak kecelakaan, saya langsung lemas"]**. Penipu menang ketika korbannya panik dan sendirian." *(Kalau riset belum selesai, pakai kalimat s07–s08 lama dan jangan menyebut angka.)* |
| 6 | 1:55–2:10 | [LAYAR] slide konsep s09 | [VO] Ketua | "Karena itu kami merancang JagaOrtu: aturan dua orang berbasis AI. Prinsip *maker-checker* bank, kini untuk keluarga." |
| 7 | 2:10–3:25 | [LAYAR] wireframe A1 → A3 → A6 → A4 → A5 → A7 (zoom pelan) | [VO] A4/Ketua | Pakai narasi segmen 10, 11, 13, 14, 15, 16 dari `Naskah_Video.md` (A1 pemasangan, A3 peringatan, A6 Pendamping, A4 Tanya Dulu, A5 telepon, A7 Latihan Waspada). Di A3 sisipkan **suara Sunda** (baris 8). |
| 8 | (di dalam 7) | [LAYAR] A3 | **penutur asli Sunda** | "Antosan heula, Bu. Pesen ieu menta transfer buru-buru, sareng menta dirasiahkeun. Mangga taros heula ka Rina." **← wajib dicek penutur asli sebelum direkam** (lihat catatan). |
| 9 | 3:25–4:05 | [LAYAR] `build/arch.png`, sorot per lapis | [VO] A2 (AI) | "Bagaimana AI-nya bekerja? Kami memakai AI secukupnya. Aturan pasti menyaring nomor, rekening, dan file berbahaya. Model ringan di perangkat menilai risiko secara offline. Model bahasa besar hanya dipanggil untuk kasus ambigu, dengan data yang sudah disamarkan. Kami sengaja **tidak** mengklaim mendeteksi suara deepfake; kata sandi keluarga tetap ampuh walau suara dikloning. Kami juga jujur soal batas Android: misalnya, WhatsApp terenkripsi, jadi kami hanya membaca teks notifikasi atas izin Ibu." |
| 10 | 4:05–4:35 | [LAYAR] slide bisnis s20–s22 | [VO] Ketua | "Semua komponen memakai API Android resmi dan model yang sudah tersedia, sehingga MVP dapat dibangun dalam 24 jam. Model bisnisnya B2B2C untuk bank dan BPR, yang wajib menjalankan strategi anti-fraud sesuai POJK 12 tahun 2024, juga dompet digital, ditambah paket keluarga. Pilot dimulai di Bandung dengan 30 keluarga." |
| 11 | 4:35–4:50 | **[KAM]** seluruh tim, lalu slide penutup s24 | Ketua (atau bersama) | "Penipu menang ketika korbannya panik dan sendirian. JagaOrtu memastikan tidak ada lansia yang harus menghadapi penipu sendirian. **Sebelum transfer, tanya dulu.**" |

Subtitle: pakai `.srt` lama sebagai dasar, sesuaikan dengan ucapan baru (YouTube Studio → Subtitles → upload/edit). Subtitle membantu juri dan aksesibilitas.

## Shot list
| Shot | Lokasi | Framing | Durasi rekam | Catatan |
|---|---|---|---|---|
| K1 Tim berjajar | ruangan terang, latar polos/kampus | medium wide, lanskap, kamera setinggi mata | 3 take × 15 dtk | Pakai kaus/atasan seragam warna senada bila ada |
| K2–K5 Close-up per anggota | sama | medium close-up, mata di 1/3 atas | 3 take × 8 dtk tiap orang | Ucapkan nama + peran; tatap lensa |
| K6 Insight riset | posyandu/rumah (izin) | A4 dengan latar lokasi | 2 take × 20 dtk | **Tanpa wajah lansia kecuali ada izin tertulis** |
| K7 Penutup tim | sama dengan K1 | medium wide | 3 take × 10 dtk | Kalimat terakhir serempak boleh |
| B-roll (opsional) | — | tangan memegang HP lansia, layar wireframe di HP | 5–10 klip × 4 dtk | Tanpa nomor/nama asli di layar |
| VO | ruangan kecil berkarpet/lemari baju | mic 15–20 cm dari mulut | per segmen | Rekam per baris naskah, sisakan 1 dtk hening di awal/akhir |

Pengaturan rekam: 1080p 30 fps, kunci fokus & eksposur (tap-tahan di HP), suara mono 48 kHz. Simpan file suara narasi sesuai nomor segmen lama bila ingin memakai pipeline otomatis: `build/audio/custom/segNN.mp3` (lihat `00_BACA_DULU.md`). Klip wajah (K1–K7) tetap disisipkan lewat editor.

## Catatan bahasa Sunda (wajib)
- Kalimat di baris 8 dibuat dengan bantuan AI dan **belum diverifikasi penutur asli**. Minta minimal satu penutur asli Sunda (anggota tim, keluarga, atau dosen/teman asal Priangan) memeriksa:
  - (a) apakah kalimatnya alami dan sopan (undak-usuk/basa lemes untuk orang tua);
  - (b) apakah "buru-buru", "dirasiahkeun", "taros heula" tepat;
  - (c) pelafalan.
- Idealnya **penutur asli itu sendiri yang merekam** kalimatnya. Suara manusia lebih meyakinkan daripada TTS, dan ini bisa menjadi momen kuat di video.
- Catat nama pemeriksa (untuk Anda sendiri) dan versi kalimat final di sini: `Diperiksa oleh: __________ · Kalimat final: ______________________`.

## Checklist sebelum unggah
- [ ] Durasi ≤ 5:00 (cek di editor, bukan perkiraan)
- [ ] Ada wajah & nama semua anggota (perkenalan tim)
- [ ] Klaim "3 detik (McAfee 2023)", bukan "10 detik"
- [ ] Angka sama dengan proposal; angka riset = angka asli dari `06_Riset_Pengguna`
- [ ] Kalimat Sunda sudah dicek penutur asli
- [ ] Musik latar (bila ada) berlisensi bebas (mis. YouTube Audio Library); volume rendah
- [ ] Tidak ada nomor HP/rekening/nama asli orang di layar
- [ ] Unggah sebagai **Unlisted**; judul `<NamaTim> - JagaOrtu - Hackvidia 11.0`; uji tautan dari browser incognito
- [ ] Perbarui `Naskah_Video.md` dengan naskah final yang benar-benar dipakai
