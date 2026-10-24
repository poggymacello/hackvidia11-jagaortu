# Riset pengguna JagaOrtu: urutan kerja

Target selesai **≤ 25 Nov 2026**, supaya ada waktu membangun ulang proposal dan video sebelum 1–6 Des.

| # | Langkah | File | Hasil | Siapa |
|---|---|---|---|---|
| 1 | Buat Google Form, uji sendiri, hapus respons uji, sebar | `A_FORM_SURVEI_GOOGLE.md` | ≥30 responden (anak dewasa yang orang tuanya 60+) | UX/bisnis |
| 2 | Cetak lembar persetujuan & wireframe A3/A5/A8 | `B_PERSETUJUAN_PARTISIPAN.md`, `03_Wireframe/` | — | UX |
| 3 | Wawancara 8–10 lansia; 5 di antaranya ikut uji wireframe | `C_SKRIP_WAWANCARA_DAN_UJI_WIREFRAME.md` | baris di `data/wawancara.csv`, `data/uji_wireframe.csv` | 2 orang per sesi |
| 4 | Unduh CSV Google Form → `data/survei.csv` (timpa file template) | — | — | UX |
| 5 | Hitung & cek angka | `olah_hasil.py` | angka + paragraf proposal | siapa saja |
| 6 | Tulis ke config, bangun ulang proposal | `olah_hasil.py --tulis`, lalu `build_all.py --only proposal` | proposal versi tervalidasi | siapa saja |
| 7 | Catat 1–3 perubahan desain dari uji wireframe | — | bahan video & pitch ("setelah uji, kami mengganti …") | UX |

## Perintah (jalankan dari folder `Hackvidia11-JagaOrtu`)
```
.venv\Scripts\python 06_Riset_Pengguna\olah_hasil.py                 # lihat angka & paragraf
.venv\Scripts\python 06_Riset_Pengguna\olah_hasil.py --tulis         # simpan ke config_tim.json -> validasi
.venv\Scripts\python build_all.py --only proposal                     # bangun ulang proposal (cek "halaman teks <= 10")
```
Untuk mencoba skrip tanpa data asli: `--data 06_Riset_Pengguna\contoh_FIKTIF`. Data di folder itu **fiktif**, dan skrip menolak menulisnya ke config.

## Aturan data
- **Jangan mengarang atau "membulatkan ke atas".** Kalau responden hanya 18, tulis 18. Juri lebih menghargai angka kecil yang jujur daripada angka besar yang tidak bisa dipertanggungjawabkan saat tanya-jawab.
- CSV tidak boleh berisi nama, nomor HP, rekening, atau OTP. Kolom kontak Q14 di survei diabaikan skrip; pindahkan ke file terpisah, lalu hapus dari CSV sebelum dibagikan.
- Simpan bukti mentah (CSV, lembar persetujuan) sampai final. Juri bisa meminta bukti.
- Hapus data mentah setelah kompetisi selesai (Jan 2027), sesuai janji di teks persetujuan.

## Angka yang masuk otomatis ke proposal
`survei_n`, `survei_pct_ortu_pernah_jadi_target`, `survei_pct_khawatir`, `survei_pct_mau_jadi_pendamping`, `survei_pct_bayar_min15rb` (baru 23 Okt malam, dari Q13), `wawancara_lansia_n`, `wawancara_temuan`, `uji_wireframe_n`, `uji_wireframe_pct_paham`, `kutipan_lansia`.
Bagian yang datanya belum ada tetap `null`, dan kalimatnya tidak muncul. Rumus lengkap ada di `A_FORM_SURVEI_GOOGLE.md` (tabel akhir) dan `olah_hasil.py`.
Sudah diuji (23 Okt malam, data FIKTIF di luar folder proyek): dengan semua bagian terisi, proposal tetap 10 halaman teks. Proposal kini memuat **protokol pra-registrasi** (Tabel 2) dengan kriteria keputusan; kolom "Hasil" dan keputusannya (mis. "Pendamping 85% → inti tetap") terisi otomatis dari angka asli. Angka persen ditulis dengan selang kepercayaan 95% Wilson. **Jangan ubah kriteria keputusan setelah melihat data**; kalau ingin mengubah, catat alasannya di proposal.

`Instrumen_Validasi_Pengguna.md` adalah versi awal (9 Okt). Pakai file A–C di folder ini; isinya sama tetapi sudah siap tempel dan selaras dengan CSV.
