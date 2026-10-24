# Catatan cek fakta proposal (23 Okt 2026)

Cek cepat terhadap statistik dan klaim utama di `build/proposal.py`, Lean Canvas, dan video. Status: ✅ cocok dengan sumber · 🔧 diperbaiki hari ini · ⚠️ perlu dicek/diwaspadai tim. Tidak ada angka baru yang dikarang; yang tidak bisa diverifikasi ditandai.

| # | Klaim | Sumber di proposal | Status | Catatan |
|---|---|---|---|---|
| 1 | IASC menerima **702.342 laporan** (22 Nov 2024–30 Sep 2026) | [1] Kontan | ✅ 🔧 | Angka cocok. Tanggal artikel yang benar **6 Okt 2026** (sebelumnya tertulis 5 Okt). |
| 2 | Kerugian **Rp9,1 T** dari **432.637 aduan** hingga 14 Jan 2026; ≈Rp21 juta/aduan | [2] OJK SP 15/GKPB/OJK/I/2026 | ✅ | Sumber primer OJK. Rata-rata adalah perhitungan tim (9,1 T ÷ 432.637 ≈ Rp21,0 juta). |
| 3 | Tiga modus teratas: belanja daring 113.520 (Rp1,78 T), *fake call* 63.517 (**Rp2,09 T**), investasi 32.251 (Rp2,08 T) | [3] JPNN 21 Agu 2026 | ✅ ⚠️ | Cocok dengan artikel; data **Nov 2024–Jun 2026** (periode berbeda dengan angka 702.342). Sumber sekunder (OJK Jabar dalam konferensi pers). Bila sempat, cari rilis OJK primer. |
| 4 | Jawa Barat tertinggi, **131.445 laporan** | [3] JPNN | ✅ ⚠️ | Badan artikel JPNN juga memuat "131.455" (salah ketik). Republika 21 Agu 2026 mengonfirmasi **131.445** (Nov 2024–Jun 2026, dari 637.055 nasional). Pertimbangkan menambah/mengganti rujukan ke Republika atau Bloomberg Technoz. |
| 5 | Laporan penipuan terindikasi AI: **13 (akhir 2024)**, total **1.379 hingga Jun 2026** | [4] Kontan (konferensi pers 4 Agu 2026) | ✅ 🔧 | Redaksi diperbaiki: sebelumnya ditulis "naik dari 13 menjadi 1.379" seolah-olah angka per periode; 1.379 adalah total kumulatif. |
| 6 | Komdigi: banyak lansia jadi korban scam AI peniru suara pejabat | [5] Kompas 2 Jul 2026 | ✅ | Pernyataan Wamenkomdigi Nezar Patria (kualitatif, tanpa angka). |
| 7 | Kloning suara: **3 detik rekaman → kecocokan ±85%** | [6] McAfee 2023 (Business Wire) | 🔧 | **Diganti.** Sebelumnya "10 detik" dengan rujukan CNBC Indonesia tentang modus penculikan anak (tidak tepat sebagai sumber). Kini: siaran pers McAfee 1 Mei 2023 "The Artificial Imposter" (riset alat kloning suara + survei 7.054 responden, 7 negara). Laporan PDF "Beware the Artificial Impostor" tidak bisa diunduh dari mesin ini; rujukan memakai siaran pers. Angka 85% berasal dari pengujian internal McAfee (satu kasus uji), jadi jangan dilebih-lebihkan menjadi "semua suara bisa dikloning dalam 3 detik". |
| 8 | Penduduk **284,67 juta**, lansia **11,97%** (SUPAS 2025), ≈34 juta lansia | [7] | 🔧 | Artikel Kompas yang dirujuk **tidak** memuat 11,97%. Rujukan diganti ke **rilis BPS 5 Mei 2026** (judulnya memuat 11,97%). 0,1197 × 284,67 jt ≈ 34,1 jt ✅. |
| 9 | Lansia mengakses internet **14,10% (2021) → 34,13% (2025)**; **52,23%** lansia menggunakan HP | [8] GoodStats (16 Jan 2026), mengolah BPS | ✅ 🔧 | Angka cocok. Redaksi diperbaiki dari "memiliki" menjadi "**menggunakan** telepon seluler", sesuai sumber. Sumber sekunder; idealnya rujuk publikasi BPS *Statistik Penduduk Lanjut Usia 2025*. |
| 10 | Literasi keuangan usia 51–79 = **54,55%** | [9] OJK–BPS SP 69/OJK/GKPB/V/2025 | ✅ | Angka metode *keberlanjutan*; metode cakupan DNKI = 55,03%. Bila ditanya, sebut metodenya. |
| 11 | Google Fake Call Detection | [10] Kompas Tekno 4 Jun 2026 | 🔧 | Sumber menyebut **Phone by Google, Android 12+, mulai di Pixel**; **tidak** menyebut RCS. Tabel 1 proposal, Lean Canvas, dan `00_Penilaian` dikoreksi (sebelumnya "Phone by Google/RCS"). Ketersediaan di Indonesia tidak disebut sumber. |
| 12 | POJK 12/2024 mewajibkan strategi anti-fraud | [11] OJK | 🔧 | Isi: strategi anti-fraud **4 pilar** (pencegahan; deteksi; investigasi, pelaporan & sanksi; pemantauan & tindak lanjut) + sosialisasi kebijakan ke pihak eksternal. Redaksi "edukasi pihak eksternal" diganti. **E-wallet diatur Bank Indonesia, bukan OJK**, jadi kalimat "bank, BPR, dan dompet digital yang wajib (POJK 12/2024)" diperbaiki di proposal, Lean Canvas, naskah video, dan pitch: kewajiban POJK hanya untuk bank/BPR (LJK), sedangkan e-wallet tetap calon pelanggan. |
| 13 | AS: usia 60+ rugi **US$4,885 miliar**, **147.127 aduan** (2024) | [13] FBI IC3 2024 | ✅ ⚠️ | Dikonfirmasi lewat beberapa liputan sekunder; PDF primer tidak dibuka dari mesin ini. Cek halaman "Elder Fraud" di laporan IC3 2024 sebelum final. |
| 14 | Dataset SMS Indonesia **1.143 pesan** (normal/penipuan/promo) | [15] | ⚠️ | Tidak diverifikasi hari ini. Cek tautan JTIKA masih hidup dan nama penulis/dataset benar sebelum 1 Des. |
| 15 | TTS mendukung id-ID, su-ID, jv-ID | [16] Microsoft | ✅ | Suara `su-ID-TutiNeural` benar-benar dipakai untuk membangun video. |
| 16 | Inokulasi meningkatkan ketahanan terhadap manipulasi | [17] Roozenbeek dkk. 2022 | ✅ | Konteks studi adalah misinformasi, bukan penipuan finansial. Kalimat proposal ("paparan ringan yang aman") masih wajar; jangan klaim "terbukti mencegah penipuan". |
| 17 | Android 15 OTP redaction; CallScreeningService; WhatsApp E2EE; restricted settings | [18]–[21] (baru) | ✅ | Dicek langsung di developer.android.com, faq.whatsapp.com, support.google.com (§4.5 baru). |
| 18 | "Android dipakai mayoritas pengguna ponsel di Indonesia" (§7) | — | ⚠️ | Benar secara umum, tetapi **tanpa rujukan**. Tambahkan sumber (mis. StatCounter) bila halaman cukup, atau siapkan jawabannya untuk tanya-jawab. |
| 19 | Biaya LLM < Rp10/analisis; < Rp1.000/pengguna/bulan; harga Rp4.000 & Rp25.000; Rp420 juta per 1.000 keluarga | — | ⚠️ asumsi | Sudah diberi label "asumsi/estimasi" di proposal. Hitung ulang biaya per token dengan harga API yang benar-benar dipakai saat final; jangan menyebut sebagai fakta. |

## Yang belum dikerjakan (perlu manusia)
- Membuka PDF primer IC3 2024 dan laporan McAfee bila ingin mengutip langsung.
- Mencari rilis OJK primer untuk angka per modus dan per provinsi (opsional; sumber berita saat ini konsisten).
- Memastikan semua tautan Daftar Pustaka masih dapat dibuka pada 1 Des 2026.

---

# Pembaruan 23 Okt 2026 malam (protokol Juri 90)
Proposal ditulis ulang (lihat `JURI_90/SKOR.md`). Sitasi kini dinomori otomatis dari `build/proposal.py` (`[@kunci]`); referensi yang tidak disitasi tidak dicetak. Klaim baru dan koreksi:

| # | Klaim | Sumber | Status | Catatan |
|---|---|---|---|---|
| 20 | Google Scam Detection sudah menilai **notifikasi aplikasi chat (WhatsApp, Signal, X)** di Pixel 6+, **AS saja** | Android Authority 11 Nov 2025 | 🔧 **koreksi penting** | Klaim lama "Google tidak mencakup WhatsApp" **salah/usang** → dihapus dari proposal, Lean Canvas, Q&A #23. Posisi baru: kami tidak bersaing di deteksi. |
| 21 | Google bermitra dengan 12 merek Android (HONOR, Infinix, iQOO, itel, JOVI, Motorola, OPPO, OnePlus, realme, TECNO, vivo, Xiaomi) untuk membawa Scam Detection notifikasi chat | Google blog 14 Okt 2026 | ✅ | Pos blog tidak menyebut Indonesia; daftar negara ada di halaman bantuan Google yang tidak kami buka. **Cek ulang 1 Des**: bila Indonesia/bahasa Indonesia sudah didukung, ubah kalimat Tabel 1 kolom 3. |
| 22 | Scam Detection Google Messages di 20+ negara; contoh bahasa: Inggris, Arab, Prancis, Jerman, Portugis, Spanyol | Google blog 25 Feb 2026 | ✅ | Bahasa Indonesia tidak disebut (daftar bukan daftar lengkap). Jangan menulis "tidak tersedia di Indonesia"; tulis "sumber resmi belum menyebut". |
| 23 | Truecaller: ID penelepon WhatsApp (beta, Mei 2023) | Reuters via Malay Mail 8 Mei 2023 | ✅ ⚠️ | Peluncuran global setelah beta tidak terkonfirmasi; ditulis "beta 2023". |
| 24 | aduannomor.id = layanan Komdigi untuk melaporkan nomor | detikInet 16 Jul 2025 | ✅ | cekrekening.id tidak disebut di artikel itu; cekrekening.id sudah dikenal sebagai layanan Komdigi (dirujuk tanpa sumber terpisah). |
| 25 | Dataset SMS **1.143 pesan** | Dwiyansaputra dkk. 2021, JTIKA 3(2) | 🔧 | Dibuka & dibaca: **2 kelas, 569 normal + 574 spam**, data asal Rahmi & Wibisono (2016, naskah tidak terbit). Klaim lama "berlabel normal, penipuan, promo" dari sumber ini **tidak tepat** → diperbaiki. Rujukan kini atas nama penulis artikel JTIKA. |
| 26 | Rata-rata kerugian per laporan: *fake call* Rp32,9 jt; investasi Rp64,5 jt; belanja Rp15,7 jt | dihitung dari [JPNN] (periode sama) | ✅ perhitungan tim | 2,09 T ÷ 63.517; 2,08 T ÷ 32.251; 1,78 T ÷ 113.520. |
| 27 | ±11,6 juta lansia daring | 34,1 jt × 34,13% | ✅ perhitungan tim | Menggabungkan BPS SUPAS 2025 dan GoodStats (BPS 2025); periode berdekatan, tetap sebut "sekitar". |
| 28 | James, Boyle & Bennett 2014: kerentanan terkait usia, kognisi, kesejahteraan psikologis, literasi (n=639, model penuh) | PMC3916958 | ✅ | Dukungan sosial **hanya tren** (p=0,053) setelah kontrol kognisi → **jangan** klaim "isolasi sosial terbukti" dari studi ini. Ukuran = skala kerentanan self-report, bukan korban nyata. |
| 29 | Czaja dkk. 2019, *Designing for Older Adults* ed. 3 (CRC) | katalog penerbit | ✅ | Prinsip umum; tidak ada angka yang dikutip. |
| 30 | Akhawe & Felt 2013 (USENIX Sec): desain peringatan memengaruhi *click-through* (25 jt tayangan) | USENIX / Google Research | ✅ | Konteks browser, bukan lansia. Dipakai hanya untuk "desain menentukan kepatuhan". |
| 31 | Anderson dkk. 2015 (CHI): peringatan polimorfik lebih tahan habituasi (fMRI) | BYU / CHI | ✅ | Konteks peringatan keamanan umum. |
| 32 | Amershi dkk. 2019 (CHI): 18 pedoman interaksi manusia-AI | Microsoft Research | ✅ | |
| 33 | FINRA Rule 4512 (trusted contact) & 2165 (temporary hold), berlaku 5 Feb 2018 | FINRA Regulatory Notice 17-11 | ✅ | Pasar modal AS (broker-dealer), bukan bank. Disebut sebagai preseden, bukan bukti efektivitas. |
| 34 | UU PDP: Pasal 4(2) data keuangan pribadi = data spesifik; Pasal 34(2) penilaian dampak wajib untuk (antara lain) data spesifik & teknologi baru; Pasal 10 hak keberatan atas keputusan otomatis | pasal.id (teks UU 27/2022) | ✅ | Pasal 56 (transfer lintas negara) **tidak** diverifikasi → tidak dikutip nomornya. |
| 35 | POJK 12/2024: cakupan meliputi LJK, **konsumen**, dan pihak yang bekerja sama; 4 pilar; sosialisasi ke pihak eksternal | OJK abstrak, Bisnis/Infobank | ✅ | Jangan klaim POJK mewajibkan aplikasi seperti JagaOrtu. |
| 36 | Taspen menyalurkan pensiun lewat **46 mitra bayar** | Bisnis.com 20 Mei 2026 | ✅ ⚠️ | Angka berbeda antar tahun (44–48). Cek situs Taspen sebelum final. |
| 37 | Inggris: penggantian wajib APP fraud hingga £85.000 sejak 7 Okt 2024 | PSR | ✅ | |
| 38 | Singapura: Shared Responsibility Framework berlaku 16 Des 2024 (bank & telko; **tidak** mencakup transaksi yang diotorisasi korban) | Baker McKenzie | ✅ | Karena itu ditulis "untuk *phishing*", bukan untuk semua penipuan. |
| 39 | Android ±77% pangsa OS ponsel Indonesia (Agu 2026) | StatCounter | ✅ | Menutup item ⚠️ #18. StatCounter mengukur trafik web, bukan jumlah perangkat. |
| 40 | Gemini 2.5 Flash-Lite US$0,10 / 0,40 per 1 juta token (masuk/keluar) | ai.google.dev/pricing, dicek 23 Okt 2026 | ✅ | Harga bisa berubah; kurs Rp16.500/US$ adalah asumsi. |
| 41 | IndoNLU / IndoBERT (Wilie dkk. 2020, AACL) | ACL Anthology | ✅ | Hanya sebagai pembanding evaluasi. |

**Dihapus dari proposal:** skenario "Rp420 juta per 1.000 keluarga" (asumsi 1 kejadian per 50 keluarga tidak berdasar) dan rujukan FBI IC3 (primer belum dibuka; tidak penting). Rujukan Kompas Tekno (Fake Call Detection) diganti sumber Google/Android Authority yang lebih baru.
