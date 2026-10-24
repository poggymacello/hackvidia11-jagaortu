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
