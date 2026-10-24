# A. Survei anak dewasa: teks siap tempel ke Google Form

Cara pakai:
1. Buka forms.google.com → formulir kosong. Settings → Responses: **matikan "Collect email addresses"** (survei anonim). Matikan "Limit to 1 response" (tidak perlu login).
2. Salin teks di bawah **persis**, termasuk awalan `Q01.`, `Q02.`, dst. Awalan itu dipakai `olah_hasil.py` untuk mengenali kolom saat CSV diunduh. Opsi jawaban juga harus sama persis (huruf besar/kecil boleh beda).
3. Tipe pertanyaan tertulis di `[...]`. Tanda `*` = wajib diisi. **Jangan memakai koma di teks opsi kotak centang**: Google Form menggabungkan pilihan dengan koma, jadi koma di dalam opsi membuat hitungan salah.
4. Setelah selesai: tab Responses → ⋮ → **Download responses (.csv)** → simpan sebagai `06_Riset_Pengguna/data/survei.csv`.
5. Uji isi formulir sendiri 1 kali, lalu **hapus respons uji** sebelum disebar.

Target: **≥30 responden yang lolos Q02**. Sebar ke grup angkatan, grup keluarga anggota tim, dan teman kampus lain.

---

**Judul formulir:**
Survei singkat: melindungi orang tua dari penipuan digital (3 menit, anonim)

**Deskripsi formulir:**
Halo! Kami tim mahasiswa peserta Hackvidia Arkavidia 11.0 (ITB) yang sedang merancang JagaOrtu, solusi untuk membantu orang tua lanjut usia terhindar dari penipuan lewat HP.
Survei ini anonim: kami tidak meminta nama, email, atau nomor telepon. Jawaban hanya dipakai dalam bentuk angka gabungan untuk proposal lomba dan akan dihapus setelah kompetisi selesai (Januari 2027). Anda boleh berhenti kapan saja.
Dengan menekan "Berikutnya", Anda menyatakan bersedia ikut serta.
Kontak tim: [ISI: email tim]

---

### Bagian 1: Tentang Anda

**Q01. Usia Anda** `[Pilihan ganda]*`
- 18–24
- 25–34
- 35–44
- 45 ke atas

**Q02. Apakah Anda memiliki orang tua atau mertua yang berusia 60 tahun ke atas?** `[Pilihan ganda]*`
- Ya
- Tidak

> Pengaturan percabangan: klik ⋮ → "Go to section based on answer". **Ya → Bagian 2**, **Tidak → Submit form**.

### Bagian 2: Orang tua Anda

Deskripsi bagian: *Jika ada lebih dari satu orang tua berusia 60+, jawab untuk yang paling sering memakai HP.*

**Q03. Apakah orang tua tersebut tinggal serumah dengan Anda?** `[Pilihan ganda]*`
- Ya
- Tidak

**Q04. Aplikasi apa saja yang dipakai orang tua Anda?** `[Kotak centang]*`
- WhatsApp
- Mobile banking
- E-wallet
- Media sosial
- Tidak memakai ponsel pintar

**Q05. Dalam 12 bulan terakhir, apakah orang tua Anda pernah menerima pesan atau telepon yang Anda yakini penipuan?** `[Pilihan ganda]*`
- Ya
- Tidak
- Tidak tahu

**Q06. Jika ya, modus apa saja?** `[Kotak centang]` (tidak wajib)
- Mengaku anak/keluarga butuh uang
- Mengaku polisi/bank/BPJS/CS
- Link atau file .apk (undangan/resi/tagihan)
- Hadiah atau undian
- Investasi
- Salah transfer atau refund
- Lainnya

**Q07. Apakah orang tua Anda pernah sampai mengirim uang atau memberikan data (OTP/PIN) karena penipuan?** `[Pilihan ganda]*`
- Ya
- Tidak
- Tidak tahu

**Q08. Seberapa khawatir Anda orang tua Anda tertipu?** `[Skala linier 1–5]*`
- Label 1: Tidak khawatir
- Label 5: Sangat khawatir

**Q09. Saat ini, apa yang Anda lakukan untuk melindungi orang tua dari penipuan?** `[Paragraf]` (tidak wajib)

### Bagian 3: Ide solusi

Deskripsi bagian (tempel apa adanya):
*Bayangkan sebuah aplikasi di HP orang tua Anda yang: (1) memberi peringatan bersuara saat ada pesan atau telepon berisiko, dalam bahasa yang dipahami orang tua; (2) dengan satu ketukan menghubungi Anda sebelum orang tua mentransfer uang; (3) TIDAK membuat Anda bisa membaca seluruh isi chat orang tua, Anda hanya menerima ringkasan risikonya.*

**Q10. Apakah Anda bersedia menjadi "Pendamping" orang tua Anda di aplikasi seperti ini?** `[Pilihan ganda]*`
- Ya
- Mungkin
- Tidak

**Q11. Bagian mana yang paling penting menurut Anda? (pilih maksimal 2)** `[Kotak centang]*`
> Pengaturan: ⋮ → Response validation → "Select at most" → 2
- Peringatan otomatis
- Penjelasan bersuara dalam bahasa daerah
- Notifikasi ke anak
- Kata sandi keluarga untuk telepon
- Latihan simulasi penipuan
- Privasi (anak tidak membaca isi chat)

**Q12. Apa kekhawatiran Anda terhadap aplikasi seperti ini?** `[Kotak centang]` (tidak wajib)
- Privasi
- Orang tua sulit memakai
- Terlalu sering memberi peringatan
- Biaya
- Lainnya

**Q13. Berapa biaya per bulan yang wajar untuk melindungi hingga 2 orang tua?** `[Pilihan ganda]*`
- Gratis saja
- Maksimal Rp15.000
- Rp15.000–30.000
- Lebih dari Rp30.000

**Q14. Bolehkah tim menghubungi Anda untuk mewawancarai orang tua Anda (dengan izin beliau)? Jika boleh, tulis nomor WA atau email. Kosongkan jika tidak.** `[Jawaban singkat]` (tidak wajib)

> Q14 adalah satu-satunya data pribadi. Saat analisis, `olah_hasil.py` mengabaikan kolom ini. Pindahkan kontak ke lembar terpisah dan hapus dari CSV sebelum dibagikan ke siapa pun.

**Pesan konfirmasi (Settings → Presentation):**
Terima kasih! Jawaban Anda membantu kami merancang perlindungan yang menghormati orang tua. Tips singkat: sepakati "kata sandi keluarga" dengan orang tua Anda hari ini, untuk dipakai bila ada telepon yang mengaku keluarga dan meminta uang.

---

## Kaitan pertanyaan ↔ angka di proposal
| Angka di proposal | Rumus (`olah_hasil.py`) |
|---|---|
| `survei_n` | jumlah respons dengan Q02 = Ya |
| `survei_pct_ortu_pernah_jadi_target` | % Q05 = Ya (dari `survei_n`) |
| `survei_pct_khawatir` | % Q08 bernilai 4 atau 5 |
| `survei_pct_mau_jadi_pendamping` | % Q10 = Ya ("Mungkin" **tidak** dihitung) |
| `survei_pct_bayar_min15rb` | % Q13 = "Rp15.000–30.000" atau "Lebih dari Rp30.000" (uji asumsi harga Paket Keluarga; kriteria keputusan S1 di proposal Tabel 2) |
| (bahan pitch, tidak masuk otomatis) | Q06 modus terbanyak, Q07 % pernah rugi, Q11 fitur prioritas, Q12 kekhawatiran |
