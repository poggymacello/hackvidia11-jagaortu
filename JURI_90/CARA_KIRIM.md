# CARA_KIRIM — Hackvidia 11.0, babak penyisihan
**Jendela kirim: 1–6 Des 2026, batas 6 Des 23.59 WIB.** Tidak ada toleransi keterlambatan; berkas tidak lengkap langsung gugur. Targetkan kirim **5 Des malam**.
Dokumen ini tidak mengirim apa pun. Semua langkah dilakukan oleh tim.

## 1. Mekanisme (status verifikasi)
- Halaman https://arkavidia.com/competitions/hackvidia (dicek 23 Okt 2026) **tidak** menjelaskan cara unggah karya; FAQ "What do teams need to submit…" belum berisi jawaban.
- Ringkasan guidebook (9 Okt) menyebut karya dikumpulkan 1–6 Des. Kemungkinan besar lewat **dashboard tim di arkavidia.com** (login → tim Hackvidia → menu pengumpulan/submission) atau **tautan formulir dari panitia** di grup WA peserta.
- **Sebelum 1 Des, wajib konfirmasi:** baca bagian "Pengumpulan Karya" di *Guidebook Hackvidia Arkavidia 11.0.pdf* (folder Drive resmi: https://drive.google.com/drive/folders/1PbPEl1K5HOUgyOV-b3t6eofMMG4ZT5rD), cek dashboard tim, dan baca pengumuman grup WA. Bila masih ragu, tanyakan ke CP Hackvidia (Abel / Levina, nomor tertera di arkavidia.com).
- Yang dikirim: 3 PDF + 1 tautan YouTube (lihat §2). Bila formulir meminta tautan (bukan unggahan), unggah PDF ke Google Drive tim, atur aksesnya ke "Siapa saja yang memiliki link → Viewer", lalu uji dari jendela incognito.

## 2. Berkas dan nama file
`<Nama Tim>` = nilai `nama_tim` di `config_tim.json` dan harus **sama persis** dengan nama tim di arkavidia.com (huruf besar/kecil dan spasi). Contoh di bawah memakai `JagaOrtu`.

| # | Berkas | Nama file / format | Sumber di folder | Syarat |
|---|---|---|---|---|
| 1 | Lean Canvas | `JagaOrtu_LeanCanvas.pdf` | `01_LeanCanvas\` | Tepat 1 halaman, 9 komponen |
| 2 | Proposal | `JagaOrtu_Proposal.pdf` | `02_Proposal\` | ≤10 halaman teks (di luar cover & lampiran wireframe), A4, TNR 12, spasi 1,5, margin 1 inci; lampiran wireframe low-fi |
| 3 | Video | Tautan YouTube **Unlisted**; judul **`JagaOrtu - JagaOrtu - Hackvidia 11.0`** (format: `<Nama Tim> - <Nama Solusi> - Hackvidia 11.0`) | rekam ulang, lihat `04_Video\REKAM_ULANG.md` | ≤5:00; perkenalan tim + masalah, cara kerja AI, *walkthrough* wireframe, kelayakan & dampak |
| 4 | Surat orisinalitas | `JagaOrtu_SuratOrisinalitas.pdf` | `05_Surat_Orisinalitas\` (lebih baik pakai template resmi s.hmif.dev) | Ditandatangani semua anggota; ketua di atas meterai Rp10.000 (e-meterai boleh menurut FAQ); judul sama dengan proposal |

Bangun berkas final (tanpa `--draft`) setelah `config_tim.json` terisi:
```
.venv\Scripts\python 06_Riset_Pengguna\olah_hasil.py --tulis      # hanya bila data riset asli sudah ada
.venv\Scripts\python build_all.py --skip video
```
Pastikan keluaran menampilkan `halaman teks: N (batas 10) -> OK`.

## 3. Unggah YouTube (langkah)
1. Gunakan akun YouTube milik tim. Klik **Create → Upload video**.
2. Judul: `JagaOrtu - JagaOrtu - Hackvidia 11.0` (ganti bagian pertama bila nama tim berbeda).
3. Deskripsi singkat: nama tim, anggota, satu kalimat solusi, dan pernyataan bahwa narasi suara Sunda dibuat dengan TTS (jika masih dipakai).
4. Audience: "No, it's not made for kids".
5. Visibility: **Unlisted**, bukan Private dan bukan Public.
6. Tunggu sampai pemrosesan HD selesai. Buka tautan di jendela incognito atau dari akun lain, lalu pastikan video bisa diputar, durasi ≤5:00, dan suara jelas.
7. Salin tautan `https://youtu.be/...` ke formulir pengumpulan.

## 4. Checklist H-1 (5 Des)
- [ ] `config_tim.json` tidak berisi `[ISI:`; build final berjalan tanpa `--draft`.
- [ ] Cover proposal memuat nama lengkap & prodi semua anggota; urutan anggota sama dengan data di arkavidia.com.
- [ ] Proposal: `halaman teks ≤ 10`; buka PDF di HP untuk mengecek font, tabel, dan Lampiran A (4 halaman wireframe).
- [ ] Bagian 2.4 berisi **angka riset asli**, atau status "dijadwalkan" yang jujur. Tidak ada angka dari `contoh_FIKTIF`.
- [ ] Cek ulang fakta yang bisa berubah (lihat `02_Proposal\CATATAN_CEK_FAKTA.md` #21, #36, #40): ketersediaan Google Scam Detection di Indonesia, angka mitra bayar Taspen, harga Gemini. Bangun ulang bila ada perubahan.
- [ ] Lean Canvas 1 halaman; angka sama dengan proposal (Rp32,9 jt; ±Rp90; Rp4.000; margin ±73%).
- [ ] Video: Unlisted, ≤5:00, ada wajah/suara tim, tidak ada klaim "10 detik" atau "Rp420 juta".
- [ ] Surat: tanda tangan semua anggota, meterai terbaca, satu PDF berwarna, judul sama dengan proposal.
- [ ] Nama file persis `<Nama Tim>_LeanCanvas.pdf`, `<Nama Tim>_Proposal.pdf`, `<Nama Tim>_SuratOrisinalitas.pdf`.
- [ ] Semua anggota sudah membaca proposal dan sanggup menjawab bank Q&A (`07_Final_24Jam\BANK_QnA_25.md`).
- [ ] Simpan salinan berkas yang dikirim ke `_terkirim_<tanggal>\` (jangan ditimpa lagi).

## 5. Saat dan setelah kirim
- [ ] Kirim paling lambat 5 Des 21.00 WIB. Sisakan cadangan waktu untuk gangguan jaringan atau portal.
- [ ] Screenshot halaman sukses dan simpan email konfirmasi.
- [ ] Jangan mengubah video atau tautan Drive setelah mengirim.
- [ ] Jadwal berikutnya: penilaian 14 Des–8 Jan, pengumuman 10 finalis 16 Jan, technical meeting 18 Jan, final 29–31 Jan 2027 di ITB.
