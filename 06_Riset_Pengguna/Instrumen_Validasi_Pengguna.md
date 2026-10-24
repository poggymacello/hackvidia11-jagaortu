# Instrumen validasi pengguna — JagaOrtu
> **Pembaruan 23 Okt 2026:** gunakan `README_RISET.md` + file `A_`, `B_`, `C_` (siap tempel ke Google Form, selaras dengan CSV di `data/`). Bagian D di bawah kini dikerjakan otomatis oleh `olah_hasil.py --tulis`. Pilihan jawaban Q06 versi baru tidak memakai koma.
Tujuan: membuktikan masalah dan desain dengan data asli sebelum 6 Des 2026, lalu memasukkan hasilnya ke proposal lewat `config_tim.json`.
**Jangan mengarang angka.** Kalau target responden tidak tercapai, tulis angka yang benar-benar didapat.

| Langkah | Target | Waktu | Hasil untuk proposal |
|---|---|---|---|
| A. Survei anak dewasa | ≥30 responden | 1–2 minggu (Okt–Nov) | `survei_*` |
| B. Wawancara lansia | 8–10 orang | 1–2 minggu | `wawancara_lansia_n`, `kutipan_lansia` |
| C. Uji wireframe | 5 lansia | 2–3 hari | `uji_wireframe_n`, `uji_wireframe_pct_paham` |

Tempat merekrut di Bandung: keluarga sendiri dan teman (orang tua anggota tim), grup angkatan, posyandu lansia, pengajian/majelis taklim, gereja, karang werda, PKK.

---

## A. Survei anak dewasa (salin ke Google Form)
**Judul:** Survei singkat: perlindungan orang tua dari penipuan digital (3 menit, anonim)
**Pembuka:** Kami mahasiswa yang sedang merancang solusi untuk membantu lansia terhindar dari penipuan digital. Survei ini anonim; kami tidak meminta nama atau nomor telepon.

1. Usia Anda: 18–24 / 25–34 / 35–44 / 45+
2. Apakah orang tua/mertua Anda berusia 60 tahun ke atas? Ya / Tidak (*jika tidak, akhiri*)
3. Apakah orang tua Anda tinggal serumah dengan Anda? Ya / Tidak
4. Aplikasi apa yang dipakai orang tua Anda? (boleh lebih dari satu) WhatsApp / m-banking / e-wallet / media sosial / tidak memakai ponsel pintar
5. **Dalam 12 bulan terakhir, apakah orang tua Anda pernah menerima pesan atau telepon yang Anda yakini penipuan?** Ya / Tidak / Tidak tahu → `survei_pct_ortu_pernah_jadi_target` (= % "Ya")
6. Jika ya, modus apa saja? (boleh lebih dari satu) mengaku anak/keluarga butuh uang · mengaku polisi/bank/BPJS/CS · link atau file .apk (undangan/resi/tagihan) · hadiah/undian · investasi · salah transfer · lainnya
7. Apakah orang tua Anda pernah sampai mengirim uang atau data (OTP/PIN) karena penipuan? Ya / Tidak / Tidak tahu
8. **Seberapa khawatir Anda orang tua Anda tertipu?** (1 = tidak khawatir, 5 = sangat khawatir) → `survei_pct_khawatir` (= % yang menjawab 4–5)
9. Saat ini, apa yang Anda lakukan untuk melindungi orang tua? (bebas)
10. Bayangkan sebuah aplikasi yang: memberi peringatan bersuara di HP orang tua saat ada pesan berisiko, lalu menghubungi Anda dengan satu ketukan sebelum orang tua mentransfer uang, **tanpa** membuat Anda membaca seluruh isi chat. **Apakah Anda bersedia menjadi "Pendamping" orang tua Anda?** Ya / Mungkin / Tidak → `survei_pct_mau_jadi_pendamping` (= % "Ya")
11. Bagian mana yang paling penting? (pilih 2) peringatan otomatis · penjelasan bersuara bahasa daerah · notifikasi ke anak · kata sandi keluarga · latihan simulasi · privasi
12. Kekhawatiran Anda terhadap aplikasi seperti ini? (boleh lebih dari satu) privasi · orang tua sulit memakai · terlalu sering alarm · biaya · lainnya
13. Berapa yang wajar dibayar per bulan untuk melindungi hingga 2 orang tua? Gratis saja / ≤Rp15.000 / Rp15.000–30.000 / >Rp30.000 *(untuk menguji asumsi harga Rp25.000)*

## B. Panduan wawancara lansia (20–30 menit)
**Persetujuan (dibacakan):** "Kami mahasiswa yang sedang membuat aplikasi untuk membantu orang tua terhindar dari penipuan lewat HP. Kami ingin mendengar pengalaman Bapak/Ibu. Tidak ada jawaban benar atau salah, nama tidak akan dicatat, dan Bapak/Ibu boleh berhenti kapan saja. Bolehkah kami mencatat jawaban Bapak/Ibu?"
Jangan merekam nomor rekening, nomor HP, atau data sensitif lain.

1. Pembuka: sehari-hari HP dipakai untuk apa? Siapa yang mengajari?
2. Pernah dapat pesan/telepon yang aneh atau minta uang? Ceritakan. (gali: perasaan saat itu, apa yang dilakukan, siapa yang dihubungi)
3. Apa yang membuat Bapak/Ibu percaya atau curiga?
4. Kalau ragu, biasanya bertanya ke siapa? Apa yang membuat sungkan bertanya?
5. Lebih nyaman membaca tulisan atau mendengar suara? Bahasa apa yang paling enak didengar?
6. Bagaimana perasaan Bapak/Ibu kalau HP memberi peringatan "Tunggu dulu, Bu"? Apa yang membuatnya terasa menolong dan bukan menggurui?
7. Kalau anak bisa diberi tahu saat ada pesan berbahaya, setuju? Apa yang **tidak** boleh dilihat anak?
8. Apa pendapat tentang "kata sandi keluarga" untuk telepon yang mengaku keluarga?
9. Penutup: kalau boleh minta satu hal dari aplikasi ini, apa?

Catat 1–2 kutipan yang paling kuat (anonim), misalnya kalimat tentang panik atau sungkan → `kutipan_lansia`.

## C. Uji wireframe dengan lansia (10–15 menit per orang)
Bahan: cetak atau tampilkan di HP `03_Wireframe/A3.png`, `A4.png`, `A5.png`, `A8.png`. Jangan membantu, cukup amati.

| Tugas | Instruksi | Berhasil jika |
|---|---|---|
| T1 | (Tunjukkan A3) "Bapak/Ibu menerima pesan ini dan muncul layar ini. Apa yang Bapak/Ibu lakukan?" | Memilih "Tanya Rina dulu" atau "Telepon Andi (nomor lama)" |
| T2 | "Menurut Bapak/Ibu, kenapa pesan itu berbahaya?" (*teach-back*) | Menyebut minimal 2 tanda bahaya |
| T3 | (Tunjukkan A5) "Ada telepon mengaku anak Bapak/Ibu minta uang. Apa yang dilakukan?" | Menyebut kata sandi keluarga atau telepon balik |
| T4 | (Tunjukkan A8) "Apa yang dibaca aplikasi ini dari HP Bapak/Ibu?" | Menjelaskan dengan benar minimal 1 hal |

**Paham** = berhasil T1 dan T2 → `uji_wireframe_pct_paham` = (jumlah yang paham ÷ jumlah peserta) × 100.
Tanyakan juga (skala wajah 1–3): mudah dibaca? suara membantu? merasa dihargai, bukan digurui?
Catat perubahan desain yang diminta, misalnya teks terlalu kecil atau istilah yang membingungkan. Sebut perubahan itu dalam video atau proposal ("setelah uji, kami mengganti …"); juri menyukai iterasi.

## D. Memasukkan hasil ke proposal
Buka `config_tim.json` → bagian `validasi`, contoh pengisian (angka **contoh**, ganti dengan hasil asli):
```json
"validasi": {
  "survei_n": 34,
  "survei_pct_ortu_pernah_jadi_target": 62,
  "survei_pct_khawatir": 79,
  "survei_pct_mau_jadi_pendamping": 85,
  "wawancara_lansia_n": 9,
  "uji_wireframe_n": 5,
  "uji_wireframe_pct_paham": 80,
  "kutipan_lansia": "Kalau sudah dengar 'anak kecelakaan', saya langsung lemas, tidak kepikiran tanya siapa-siapa."
}
```
Lalu jalankan `python build_all.py`. Paragraf "Validasi pengguna" di proposal otomatis berubah menjadi "Validasi awal" berisi angka tersebut. Cek lagi bahwa proposal tetap ≤10 halaman teks.
