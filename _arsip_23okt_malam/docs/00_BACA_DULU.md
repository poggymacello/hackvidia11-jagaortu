# Paket Hackvidia Arkavidia 11.0 — JagaOrtu
Tenggat kumpul karya: **6 Des 2026, 23.59 WIB**. Daftar Batch 1 s.d. **31 Okt** (Rp160.000/tim).
Pembaruan terakhir: **23 Okt 2026** (cek fakta + §4.5 batasan Android di proposal, build portabel, kit riset, rencana final 24 jam).

## Isi folder
| Folder / file | Isi | Status |
|---|---|---|
| `ISI_DATA_TIM.md` + `config_tim.json` | Data tim (nama, NIM, dll.) → semua dokumen | ⚠️ **isi `[ISI: ...]`** |
| `00_Penilaian` | Simulasi skor juri: v1 ±71 → v2 ±85 (±87–88 dengan data validasi asli); perbandingan dengan 5 ide lain | ✅ |
| `01_LeanCanvas` | `JagaOrtu_LeanCanvas.pdf` (1 halaman, 9 komponen wajib) | ✅ (dibangun ulang 23 Okt) |
| `02_Proposal` | `JagaOrtu_Proposal.pdf/.docx`: cover + **10 halaman teks** (batas maks. 10) + Lampiran A wireframe; A4, TNR 12, spasi 1,5, margin 1 inci. `CATATAN_CEK_FAKTA.md` | ✅ draf (nama masih `[ISI]`) |
| `03_Wireframe` | 8 layar low-fi (A1–A8) + 4 lembar lampiran | ✅ |
| `04_Video` | `JagaOrtu_Video_Hackvidia.mp4` (**4:36**, narasi TTS), .srt, `Naskah_Video.md`, **`REKAM_ULANG.md`** | ⚠️ perlu rekam ulang (perkenalan tim + koreksi klaim "10 detik") |
| `05_Surat_Orisinalitas` | Surat 1 halaman, siap ditandatangani | ⚠️ isi nama/NIM, tanda tangan + meterai |
| `06_Riset_Pengguna` | `README_RISET.md`, form survei siap tempel, persetujuan, skrip wawancara + uji wireframe, template CSV, `olah_hasil.py` | ⚠️ perlu dijalankan |
| `07_Final_24Jam` | Rencana 24 jam, arsitektur MVP, bank 25 Q&A, naskah pitch 5 menit, skenario demo, checklist peralatan | ✅ (tanpa kode aplikasi) |
| `08_Registrasi` | `CHECKLIST_REGISTRASI.md`: akun, tim, follow, twibbon, bayar, bukti, surat orisinalitas, berkas karya | ⚠️ tenggat 31 Okt |
| `_arsip_23okt` | Salinan PDF/DOCX sebelum dibangun ulang 23 Okt | arsip |

## Cara pakai (urutan)
1. **Registrasi ≤31 Okt**: ikuti `08_Registrasi/CHECKLIST_REGISTRASI.md`.
2. Isi `config_tim.json` sesuai `ISI_DATA_TIM.md`.
3. Jalankan riset pengguna (`06_Riset_Pengguna/README_RISET.md`), lalu `olah_hasil.py --tulis`. **Jangan mengarang angka.**
4. Bangun ulang: `.venv\Scripts\python build_all.py` (lihat **Cara build**). Pastikan output `halaman teks: N (batas 10) -> OK`.
5. Rekam ulang video sesuai `04_Video/REKAM_ULANG.md`; unggah ke YouTube (**unlisted**) dengan judul `<NamaTim> - JagaOrtu - Hackvidia 11.0`.
6. Surat orisinalitas: pakai template resmi s.hmif.dev bila bisa dibuka; ketua tanda tangan di atas meterai Rp10.000 (e-meterai boleh menurut FAQ).
7. Kirim lewat tautan panitia (1–6 Des): `<Tim>_LeanCanvas.pdf`, `<Tim>_Proposal.pdf`, tautan video, `<Tim>_SuratOrisinalitas.pdf`.

## Cara build
Pipeline membangun Lean Canvas, wireframe/diagram (PNG), proposal & surat (DOCX → PDF), dan video dari `config_tim.json`. Tidak ada path yang di-hardcode.

**Kebutuhan:**
| Komponen | Untuk | Catatan |
|---|---|---|
| Python 3.10+ | semua | |
| Paket Python (`requirements.txt`) | semua | dipasang di `.venv` proyek |
| Microsoft Edge **atau** Google Chrome | render HTML → PDF/PNG (Playwright) | memakai browser terpasang; bisa dipaksa dengan env `JAGAORTU_BROWSER=chrome`. Tanpa keduanya: `.venv\Scripts\python -m playwright install chromium` |
| Microsoft Word **atau** LibreOffice | DOCX → PDF (proposal, surat) | Word via `docx2pdf`; kalau tidak ada, `soffice` dipakai otomatis; kalau tidak ada keduanya, hanya DOCX yang dibuat |
| ffmpeg + ffprobe | video saja | dicari otomatis: env `FFMPEG_PATH`/`FFPROBE_PATH` → env `FFMPEG_DIR` (folder `bin`) → `PATH` → lokasi umum WinGet/Chocolatey/Scoop. Kalau tidak ketemu, langkah video **dilewati** dengan pesan |
| Internet | narasi TTS video (`edge-tts`) | tidak perlu bila memakai rekaman sendiri di `build/audio/custom/segNN.mp3` |

**Sekali saja (Windows, dari folder `Hackvidia11-JagaOrtu`):**
```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```
(macOS/Linux: `python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt`; konversi PDF memakai LibreOffice.)

**Membangun:**
```
.venv\Scripts\python build_all.py                          # semua (video dilewati bila ffmpeg tidak ada)
.venv\Scripts\python build_all.py --only proposal surat     # sebagian: wireframes diagram journey leancanvas proposal surat video
.venv\Scripts\python build_all.py --skip video
.venv\Scripts\python build_all.py --draft --only proposal   # pratinjau walau config masih berisi [ISI: ...]
set FFMPEG_DIR=C:\path\ke\ffmpeg\bin  &&  .venv\Scripts\python build_all.py --only video
```
`build_all.py` menolak membangun berkas final selama `config_tim.json` masih berisi `[ISI: ...]` (kecuali `--draft`). Sebelum menimpa PDF/DOCX/MP4 yang sudah dikirim ke orang lain, salin dulu ke folder arsip.

Status di mesin penyusun (23 Okt): Lean Canvas, proposal, dan surat **berhasil dibangun ulang** (Edge + Word). Video **tidak** dibangun ulang karena ffmpeg tidak terpasang. `build/video.py` sudah memuat naskah terkoreksi, jadi jalankan `--only video` di komputer yang punya ffmpeg, atau rekam ulang.

## Registrasi (arkavidia.com)
Ringkasnya: daftar akun → `/team/choose` → buat tim Hackvidia → follow IG & TikTok @arkavidia → twibbon (feed) + poster (story) → bayar Rp160.000 → unggah bukti → tunggu verifikasi → masuk grup WA. Detail & tabel berkas: `08_Registrasi/CHECKLIST_REGISTRASI.md`.
- Tim 2–4 mahasiswa aktif D3/D4/S1, boleh lintas kampus. **Bukan anggota biasa HMIF ITB.** Satu orang hanya boleh di satu tim dan satu cabang.
- File twibbon/poster/caption: https://drive.google.com/drive/folders/1cmWw_L80ha2tt1aZUo34qt4woWy08q1b

## Catatan penting
- Template surat orisinalitas resmi (https://s.hmif.dev/TemplateOrisinalitasHackvidia11.0) gagal dibuka dari mesin ini (error TLS). Kalau bisa kamu buka, salin isi pernyataan kita ke template resmi tersebut.
- Kalimat bahasa Sunda (video segmen 12, teks persetujuan Sunda di folder 06) **wajib dicek penutur asli**.
- Video saat ini masih memuat klaim lama "10 detik rekaman"; versi benar = McAfee 2023, 3 detik (lihat `02_Proposal/CATATAN_CEK_FAKTA.md`).
- Final 24 jam: **semua kode produk harus dibuat saat Hacking Day.** Folder ini sengaja tidak berisi kode aplikasi; skrip di `build/` dan `06_Riset_Pengguna/olah_hasil.py` hanya untuk membuat dokumen.
- Semua dokumen disusun dengan bantuan AI. Pastikan tim memahami setiap klaim, dan tanyakan ke panitia kalau ragu soal aturan "bantuan pihak luar".
