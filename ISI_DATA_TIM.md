# Mengisi data tim (sekali saja, lalu satu perintah)

Semua dokumen dibangun dari **`config_tim.json`**. Setiap teks berbentuk **`[ISI: ...]`** adalah isian kosong yang **wajib** diganti dengan data asli. Jangan menebak atau memakai nama contoh. `build_all.py` menolak membangun berkas final selama masih ada `[ISI:`.

## Kolom yang harus diisi
| Kolom | Contoh format (bukan data asli) | Muncul di |
|---|---|---|
| `nama_tim` | `JagaOrtu` (boleh diganti) | semua nama file (`<NamaTim>_Proposal.pdf`, dll.), cover, surat, video. **Harus sama** dengan nama tim di arkavidia.com |
| `anggota[].nama` | nama lengkap sesuai KTM | cover proposal, surat orisinalitas, slide tim di video |
| `anggota[].kampus` | `Institut Teknologi Bandung` | cover, surat |
| `anggota[].prodi` | `Teknik Elektro` | cover, surat |
| `anggota[].angkatan` | `2023` | (cadangan, untuk form registrasi) |
| `anggota[].nim` | NIM lengkap | surat orisinalitas |
| `anggota[].peran` | `Ketua` hanya untuk satu orang (baris pertama), sisanya `Anggota` | cover, surat (ketua = kolom meterai) |
| `anggota[].fokus` | sudah terisi; sesuaikan dengan pembagian kerja nyata | (referensi internal) |
| `tanggal_ttd` | `5 Desember 2026` | surat orisinalitas |
| `kota_ttd` | `Bandung` | surat orisinalitas |
| `validasi.*` | **jangan diisi manual**; pakai `06_Riset_Pengguna\olah_hasil.py --tulis` | paragraf "Validasi awal" di proposal |

Catatan:
- Baris ketua sudah berisi `Institut Teknologi Bandung` / `Teknik Elektro` (dari analisis awal). **Ubah bila salah.**
- Tim hanya 2 atau 3 orang? **Hapus seluruh baris** `{...}` anggota yang tidak ada (termasuk komanya). Tata letak surat tanda tangan mendukung 2–4 orang.
- Simpan file sebagai UTF-8 (Notepad/VS Code biasa sudah benar). Tanda kutip `"` di dalam nama ditulis `\"`.

## Lalu jalankan satu perintah
Dari folder `Hackvidia11-JagaOrtu` (PowerShell atau CMD):
```
.venv\Scripts\python build_all.py
```
Output: Lean Canvas, Proposal (DOCX+PDF), Surat (DOCX+PDF), dan video (kalau ffmpeg terpasang; kalau tidak, video otomatis dilewati dengan pesan). Lihat baris `halaman teks: N (batas 10)`. Harus **OK**.

Belum punya `.venv`? Lihat `00_BACA_DULU.md` → **Cara build**.

Hanya ingin dokumen tertentu:
```
.venv\Scripts\python build_all.py --only proposal surat leancanvas
```
Pratinjau sebelum data lengkap (berkas berisi `[ISI: ...]`, **jangan dikirim**):
```
.venv\Scripts\python build_all.py --draft --only proposal
```
