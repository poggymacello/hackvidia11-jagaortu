# JURI_90 — Skor JagaOrtu (Hackvidia 11.0, babak penyisihan)
Dinilai 23–24 Okt 2026 dengan protokol `..\..\03-MEGA-PROMPT-JURI-90.md`. Panel simulasi, bukan juri asli. Skor 0–10 per kriteria, total = rata-rata berbobot (×10).

## 1. Rubrik resmi
| Penyisihan | Bobot | Final (24 jam) | Bobot |
|---|---|---|---|
| Masalah & relevansi tema | 20 | Fungsionalitas prototipe | 25 |
| Inovasi + kualitas wireframe | 20 | Implementasi AI | 20 |
| Rancangan AI | 20 | Tema & validasi dampak | 15 |
| Kelayakan bisnis | 15 | Bisnis & operasional | 15 |
| Potensi dampak | 15 | Konsistensi dengan proposal | 10 |
| Penyampaian & format | 10 | Pitching & tanya-jawab | 15 |

Panel: **J1** profesor HCI/AI (AI berpusat manusia, lansia) · **J2** kepala pencegahan fraud bank/e-wallet Indonesia · **J3** investor fintech/insurtech Asia Tenggara · **J4** skeptis (kelayakan Android, privasi/UU PDP), punya veto: satu fatal flaw terbuka = maksimal 80.

## 2. Skor awal → akhir (per juri, per kriteria)
| Kriteria (bobot) | J1 | J2 | J3 | J4 |
|---|---|---|---|---|
| Masalah & tema (20) | 8,5 → 9,0 | 8,5 → 9,0 | 8,5 → 9,0 | 8,0 → 8,8 |
| Inovasi + wireframe (20) | 7,5 → 8,5 | 7,0 → 8,3 | 7,0 → 8,2 | 6,5 → 8,0 |
| Rancangan AI (20) | 7,5 → 8,8 | 7,5 → 8,7 | 7,5 → 8,3 | 7,0 → 8,5 |
| Bisnis (15) | 6,5 → 7,5 | 6,5 → 7,8 | 6,0 → 8,0 | 6,0 → 7,5 |
| Dampak (15) | 7,5 → 8,3 | 7,0 → 8,0 | 7,5 → 8,2 | 6,5 → 7,8 |
| Penyampaian & format (10) | 8,5 → 8,5 | 8,0 → 8,5 | 8,5 → 8,7 | 8,0 → 8,0 |
| **Total** | **76,5 → 84,8** | **74,3 → 84,2** | **74,8 → 84,0** | **69,8 → 81,6** |

**Rata-rata panel: 73,9 → 83,7.** (Simulasi 9 Okt memberi ±85 dengan panel 3 juri yang lebih lunak; panel 4 juri ini lebih keras, jadi angka awalnya turun ke 73,9.)

### Alasan singkat dan "apa yang membuat 10/10"
| Juri | Alasan skor akhir | Yang membuat 10/10 |
|---|---|---|
| J1 | Keputusan desain kini terkait bukti (James 2014, Czaja 2019, Akhawe & Felt 2013, Anderson 2015, Amershi 2019); ambang, ablasi, dan *teach-back* jelas. Belum ada satu pun data lansia asli. | Hasil S2/S3 asli (dengan SK95%) dan satu iterasi wireframe yang terbukti memperbaiki pemahaman |
| J2 | Posisi terhadap Google jujur; anggaran alarm, aturan monoton, injeksi prompt, dan Pendamping jahat sudah ditangani. Asumsi 300 notifikasi/bulan dan porsi L2 10% belum diukur. | Log uji 50 pesan *red team*, kurva presisi-recall pada data Indonesia, serta satu bank yang mau berdiskusi |
| J3 | Ekonomi unit eksplisit (±Rp90 LLM, margin ±73%/±61%), titik masuk lewat bank penyalur pensiun, dan diakui bahwa di Indonesia kerugian ditanggung korban. Harga Rp4.000 belum diuji ke pembeli. | LOI atau surat minat dari satu BPR/bank penyalur pensiun; data kesediaan bayar (Q13) |
| J4 | Fatal flaw F1 sudah ditutup. Sisa: semua validasi masih rencana, diagram arsitektur kecil terbaca, `[ISI]` dan video lama masih ada. | Validasi asli; video direkam ulang; tidak ada satu pun klaim usang |

## 3. Fatal flaw (veto J4) dan cara menutupnya
| # | Fatal flaw | Status | Cara menutup |
|---|---|---|---|
| F1 | Tabel pembeda menulis Google "tidak mencakup WhatsApp". Faktanya, Scam Detection Pixel sudah menilai notifikasi chat termasuk WhatsApp (AS, Nov 2025), dan Google mengumumkan 12 mitra OEM (14 Okt 2026) | ✅ **Ditutup** | Tabel 1 ditulis ulang dengan sumber; posisi "tidak bersaing di deteksi, membangun lapisan manusia"; Lean Canvas dan Q&A #23 ikut dikoreksi |
| F2 | Rujukan dataset SMS salah isi ("normal/penipuan/promo"; faktanya 569 normal + 574 spam) | ✅ Ditutup | PDF JTIKA dibaca; rujukan dan kalimat diperbaiki |
| F3 | Skenario "Rp420 juta per 1.000 keluarga" berasal dari asumsi tanpa dasar | ✅ Ditutup di proposal, Lean Canvas, naskah video, dan Q&A | Diganti rencana ukur dampak + pembanding Rp32,9 jt/laporan *fake call* |
| F4 | `[ISI: ...]` di cover/surat; surat belum ditandatangani | ⛔ **Terbuka (manusia)** | Isi `config_tim.json`, lalu jalankan `build_all.py` tanpa `--draft`. Berkas tidak lengkap = gugur |
| F5 | Video MP4 lama masih memuat "10 detik", "Rp420 juta", "dompet digital wajib", dan narasi TTS tanpa perkenalan tim | ⛔ **Terbuka (manusia)** | Rekam ulang sesuai `04_Video/REKAM_ULANG.md` + `Naskah_Video.md` (naskah sudah dikoreksi). `build/video.py` sudah diperbarui, tetapi ffmpeg tidak ada di mesin ini |

Selama F4 dan F5 terbuka, skor efektif kiriman dibatasi **≤80** (F4 bahkan bisa menggugurkan).

## 4. Daftar perubahan (23–24 Okt malam)
**Proposal** (`build/proposal.py` → `02_Proposal/JagaOrtu_Proposal.pdf`, 10 halaman teks termasuk Daftar Pustaka):
1. Ringkasan eksekutif dengan ide inti: "deteksi sudah menjadi fitur OS; yang belum ada adalah orang kedua pada menit kritis".
2. Kuantifikasi tajam: rata-rata kerugian per laporan menurut modus (*fake call* Rp32,9 jt, 2× belanja daring), ±11,6 juta lansia daring.
3. **Tabel 1** pembanding terverifikasi (Google Scam Detection/Messages/OEM, Truecaller, IASC/aduannomor/cekrekening, bank) + "di mana kami kalah".
4. **Tabel 2** protokol validasi pra-registrasi (S1 survei, S2 wawancara, S3 uji wireframe) dengan kriteria keputusan yang ditulis sebelum data. Kolom hasil dan keputusan terisi otomatis dari CSV, termasuk SK95% Wilson.
5. **Tabel 4** bukti → keputusan desain (gerontechnology, habituasi peringatan, pedoman manusia-AI, preseden *trusted contact* FINRA).
6. **Tabel 5** lapis L0–L3 dengan ambang 0,40/0,70, tingkat Kuning/Merah, fail-safe Kuning, dan dua aturan monoton anti-manipulasi.
7. **Tabel 6** protokol evaluasi: pemisahan waktu/sumber, target recall/alarm palsu, latensi, ablasi, pembanding IndoBERT, set *red team* 50 pesan, *teach-back*.
8. §4.4 UU PDP (Pasal 4(2), 10, 34(2)) + **Tabel 7** penyalahgunaan (injeksi prompt, peniruan JagaOrtu, Pendamping jahat, penghindaran).
9. **Tabel 9** ekonomi unit dengan asumsi tertulis (harga API Gemini terverifikasi) + logika B2B2C (POJK 12/2024, bank penyalur pensiun/Taspen 46 mitra bayar, tren PSR UK dan SRF Singapura) + urutan kanal.
10. §8.2 rencana ukur dampak (keluaran → hasil → dampak; pilot daftar tunggu 15+15) tanpa proyeksi kerugian yang tidak berdasar.
11. Konsistensi MVP: L1 linear di MVP lalu TFLite di pilot; ambang sama dengan `07_Final_24Jam/ARSITEKTUR_MVP.md`.
12. Sistem sitasi otomatis; 35 rujukan, semuanya dicek (`02_Proposal/CATATAN_CEK_FAKTA.md` #20–41).

**Lainnya:** Lean Canvas diperbarui dan tetap 1 halaman. Wireframe A3 (label Merah, koreksi "Ini aman"), A7 (persetujuan lansia, maks. 1×/minggu), dan A8 (kendali Pendamping oleh lansia) diperbarui. Diagram arsitektur kini memuat ambang. `olah_hasil.py` menghitung `survei_pct_bayar_min15rb` (Q13). Naskah video dan `video.py` dikoreksi. Q&A #11, #12, #20, #22, dan #23, pitch, serta arsitektur MVP diselaraskan. Surat dibangun ulang.

**Arsip sebelum ditimpa:** `_arsip_23okt_malam\` (PDF/DOCX, PNG wireframe, skrip build lama, dokumen).

## 5. Verifikasi
| Cek | Hasil |
|---|---|
| `build_all.py --draft --only wireframes diagram leancanvas proposal surat` | sukses (Edge + Word) |
| Halaman teks proposal (cover dan Lampiran A tidak dihitung; Daftar Pustaka **dihitung**) | **10/10** ✅; ±⅔ halaman 10 masih kosong |
| Proposal dengan data validasi FIKTIF terisi penuh (uji di scratchpad, tidak ditulis ke proyek) | **10/10** ✅ |
| Lean Canvas | **1 halaman** ✅, tidak ada teks terpotong (dicek visual) |
| Format | A4, TNR 12, spasi 1,5 untuk teks; tabel/keterangan/pustaka 1,0; margin 1 inci |
| Header tabel yatim di akhir halaman | diperbaiki (*keep-with-next*) |
| `olah_hasil.py --data contoh_FIKTIF` | jalan; keluaran memuat SK95% dan kunci baru; penolakan `--tulis` untuk data fiktif tetap berlaku |
| Kode aplikasi | **tidak ada** (aturan final). Skrip hanya membangun dokumen |

## 6. Sisa gap dan siapa yang menutup
| Gap | Dampak skor | Siapa |
|---|---|---|
| Isi nama/NIM, tanda tangan surat + meterai (F4) | wajib, atau gugur | Tim |
| Rekam ulang video dengan wajah/suara tim; naskah sudah dikoreksi (F5) | membuka veto; +0,5–1 penyampaian | Tim |
| Jalankan S1–S3 (≥30 survei, 8–10 wawancara, 5 uji wireframe) sebelum 25 Nov; `olah_hasil.py --tulis`; build ulang | +2–3 (masalah, inovasi, dampak) | Tim (UX/bisnis) |
| Satu percakapan atau surat minat dari BPR/bank penyalur pensiun (tanpa mengarang) | +1–1,5 bisnis | Ketua + mentor |
| Penutur asli memeriksa kalimat Sunda (video seg. 12, persetujuan) | risiko kredibilitas | Tim |
| Cek ulang 1 Des: ketersediaan Google Scam Detection di Indonesia, harga Gemini, angka Taspen | jaga F1 tetap tertutup | Tim |
| Daftarkan protokol Tabel 2 ke OSF/Google Drive bertanggal (bukti "pra-registrasi") | +0,3 J1/J4 | Tim (opsional) |
| Diagram arsitektur kecil terbaca pada lebar 6 inci | −0,2 penyampaian | Bisa dirapikan kemudian (ubah tata letak `diagram.py` menjadi 2 baris) |
| Tanyakan ke panitia: apakah Daftar Pustaka masuk batas 10 halaman, dan bagaimana dokumen berbantuan AI diperlakukan | kepatuhan | Ketua (CP Abel) |

## 7. Plafon
| Kondisi | Perkiraan skor penyisihan |
|---|---|
| Dikirim seperti sekarang (tanpa aksi manusia) | `[ISI]` = tidak lengkap → **gugur**; kalaupun lolos administrasi, veto F5 membatasi **≤80** |
| **Plafon sekarang** (dokumen ini + F4/F5 ditutup, tanpa data validasi asli) | **±84** |
| **Plafon setelah aksi manusia** (validasi asli S1–S3 + video asli + 1 surat minat bank/BPR) | **±88–90** |

Proyeksi final (bila lolos 10 besar, belum dinilai ulang malam ini): ±84–86. Penentunya adalah demo yang tidak gagal (25%) dan konsistensi MVP dengan proposal (lihat `07_Final_24Jam/ARSITEKTUR_MVP.md` §6).
