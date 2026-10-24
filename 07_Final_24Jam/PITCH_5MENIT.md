# Naskah pitch 5 menit (deck + demo live)

Total **5:00**, target latihan **4:40** (sisakan 20 detik untuk jeda). Dua pembicara: **P1** (ketua, cerita + bisnis) dan **P2** (operator demo; menyampaikan bagian AI). Satu orang lain memegang stopwatch dan memberi kode tangan pada 2:00 / 4:00 / 4:30.
Angka hanya yang ada di proposal atau hasil riset sendiri. Bagian `[...]` diisi data asli.

| Waktu | Slide | Pembicara | Ucapan (kerangka) |
|---|---|---|---|
| 0:00–0:25 | 1. Layar hitam + bubble WA | P1 | "*Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer lima juta sekarang. Jangan bilang Papa dulu.*" (jeda 1 detik) "Pesan seperti ini masuk ke HP orang tua kita setiap hari. Dan sekarang, suaranya pun bisa dipalsukan: riset McAfee menunjukkan tiga detik rekaman sudah cukup." |
| 0:25–0:55 | 2. Data | P1 | "IASC OJK menerima 702 ribu laporan penipuan. Modus menyamar keluarga atau petugas menimbulkan kerugian terlapor terbesar, Rp2,09 triliun. Jawa Barat, provinsi tempat kita berdiri, mencatat laporan terbanyak. Dan dari riset kami sendiri: [n] anak dewasa, [x]% orang tuanya pernah jadi sasaran." |
| 0:55–1:20 | 3. Insight | P1 | "Dari wawancara dengan [n] lansia, polanya sama: penipu menang ketika korbannya **panik dan sendirian**. Edukasi tidak hadir di detik itu. Yang dibutuhkan adalah jeda, dan orang kedua yang dipercaya." [kutipan lansia, bila ada] |
| 1:20–1:40 | 4. Konsep | P1 | "Bank tidak membiarkan satu orang menyetujui transaksi besar sendirian; ada *maker-checker*. **JagaOrtu membawa aturan dua orang itu ke keluarga.** Kita lihat langsung." |
| **1:40–3:10** | 5. **DEMO LIVE** (kamera dokumen/mirroring 2 HP) | P2 menjalankan, P1 menarasikan | Ikuti `DEMO_SKENARIO.md` adegan 1–4. Inti yang harus terlihat: pesan masuk → **suara peringatan terdengar** tanpa disentuh → Ibu menekan "Tanya Rina dulu" → **HP Rina bergetar** → Rina melihat ringkasan, bukan isi chat → telepon. Lalu satu pesan normal yang **tidak** memicu apa pun. |
| 3:10–3:45 | 6. Arsitektur + log | P2 | "Ini log yang tadi. Pesan pertama diputuskan oleh **aturan** di HP dalam [x] milidetik, tanpa AI. Pesan kedua ambigu, jadi baru di situ **LLM** dipanggil, dengan nama dan nomor yang sudah disamarkan. Keputusan akhir di tangan Ibu. Itulah *AI secukupnya*: [x] dari [y] pesan uji selesai tanpa LLM. Kami tidak mengklaim mendeteksi deepfake; kata sandi keluarga tetap ampuh apa pun kualitas suaranya." |
| 3:45–4:20 | 7. Bisnis | P1 | "Siapa yang membayar? Bank dan BPR penyalur pensiun, yang wajib menjalankan strategi anti-fraud menurut POJK 12/2024. Lisensi per pengguna (asumsi Rp4.000/bulan); biaya LLM sekitar Rp90 per pengguna per bulan karena kebanyakan keputusan di HP, margin kotor sekitar 73% (asumsi). Kanal: anak memasang di HP orang tua, komunitas lansia, lalu bank." |
| 4:20–4:45 | 8. Dampak & roadmap | P1 | "Pilot 30 keluarga di Bandung, Februari–April, desain daftar tunggu: tingkat tindakan aman pada simulasi, alarm palsu, check-in dalam 10 menit. Kriteria keberhasilan kami tetapkan sebelum data. Lalu 1.000 keluarga lewat posyandu lansia dan pengajian." |
| 4:45–5:00 | 9. Penutup | P1 | "Penipu menang ketika korbannya panik dan sendirian. JagaOrtu memastikan **tidak ada lansia yang harus menghadapi penipu sendirian**. Sebelum transfer, tanya dulu. Terima kasih." |

## Aturan pitch
- **Demo adalah pusatnya** (25% nilai). Jangan bicara tentang fitur yang tidak ditunjukkan; cukup satu kalimat roadmap.
- Jika demo live gagal >10 detik: P1 berkata "*Kita pindah ke jalur cadangan yang memakai backend yang sama*", lalu buka simulasi web. Gagal lagi → putar video demo (sudah diantrekan di tab). Jangan panik atau meminta maaf berkali-kali.
- Slide: maks. 15 kata per slide, huruf ≥28 pt, satu angka besar per slide data. Sumber kecil di pojok.
- Bahasa tubuh: hadap juri, bukan layar. P2 menyebut apa yang terjadi di HP ("sekarang HP Ibu berbicara…").
- Latihan minimal 5× penuh dengan stopwatch, 2× di antaranya di depan orang luar tim.

## Slide yang perlu disiapkan (deck PDF + versi offline)
1. Hook (bubble WA) · 2. Data (3 angka) · 3. Insight + kutipan · 4. Aturan Dua Orang · 5. Demo (judul saja + tampilan mirroring) · 6. Arsitektur 4 lapis + log · 7. Bisnis · 8. Roadmap & metrik · 9. Penutup + nama tim.
Lampiran (untuk Q&A, tidak ditampilkan kecuali ditanya): batasan Android (§4.5 proposal), privasi & UU PDP, hasil evaluasi 30 pesan, tabel konsistensi proposal↔MVP, biaya per pengguna, tabel pembeda vs Google/Truecaller.
