# Simulasi penilaian juri Hackvidia 11.0 — JagaOrtu
### 9 Okt 2026 · memakai rubrik resmi guidebook (babak penyisihan & final)

> **Catatan jujur:** juri sebenarnya belum diumumkan. Skor di bawah adalah simulasi dari tiga persona juri yang umum di hackathon kampus ITB (akademisi AI, praktisi produk/engineering, praktisi bisnis/inkubator). Skor dihitung dengan bobot resmi, dan dikalibrasi terhadap karya yang pernah menang di Arkavidia (SpeakUp, Go Vision, BIMA, SEDAYA). Ini perkiraan untuk mengambil keputusan, bukan janji hasil.

## 1. Rubrik resmi babak penyisihan
| Aspek | Bobot | Yang dicari juri |
|---|---|---|
| Pemahaman masalah & relevansi tema | 20% | Masalah jelas dan mendesak, didukung data; prinsip human-centered |
| Inovasi & kualitas solusi | 20% | Pembeda dari produk yang ada; kualitas wireframe |
| Rancangan implementasi AI | 20% | Alasan memilih domain AI; arsitektur logis; strategi data |
| Kelayakan bisnis | 15% | Operasional, pelanggan, biaya, pendapatan yang realistis |
| Potensi dampak | 15% | Besarnya manfaat yang diproyeksikan |
| Penyampaian & kelengkapan | 10% | Narasi proposal, efektivitas video, kepatuhan format |

## 2. Skor solusi SEKARANG (JagaOrtu v1, versi 9 Okt pagi)
v1 = lansia **meneruskan** pesan mencurigakan ke JagaOrtu → aturan + LLM → jawaban suara → notifikasi ke anak, kata sandi keluarga, model B2B2C umum.

| Aspek (bobot) | Juri A: dosen AI | Juri B: praktisi produk | Juri C: bisnis/inkubator |
|---|---|---|---|
| Masalah & tema (20) | 82 | 85 | 85 |
| Inovasi & solusi (20) | 65 | 62 | 68 |
| Rancangan AI (20) | 68 | 70 | 70 |
| Bisnis (15) | 60 | 62 | 55 |
| Dampak (15) | 75 | 75 | 78 |
| Penyampaian (10) | 70 | 70 | 70 |
| **Total berbobot** | **70,3** | **71,0** | **71,6** |

**Rata-rata: ±71/100.** Masalahnya kuat, tetapi solusinya belum terasa "harus menang".

### Kenapa juri tidak memberi nilai tinggi (ini yang akan mereka tanyakan)
1. **Lubang fatal: "pull" bukan "push."** Lansia harus curiga dulu baru meneruskan pesan. Padahal inti penipuan adalah korban *tidak sadar* sedang ditipu. Juri B pasti bertanya, *"Kalau Ibu tidak curiga, kapan JagaOrtu bekerja?"*
2. **"Apa bedanya dengan Google?"** Google merilis Fake Call Detection dan Scam Detection (Juni 2026). Truecaller/Getcontact sudah dikenal. Tanpa tabel pembeda, inovasi dinilai rendah.
3. **Telepon:** "Aplikasimu mendengarkan telepon?" Tidak bisa: Android tidak mengizinkan aplikasi pihak ketiga merekam isi panggilan. Kalau ini tidak dijawab, juri A menilai tim tidak paham platform.
4. **Privasi:** membaca chat WhatsApp lalu mengirimnya ke LLM di cloud memunculkan pertanyaan UU PDP.
5. **Data & evaluasi AI:** dari mana data latihnya? Bagaimana menguji akurasinya? Bahasa daerah?
6. **Siapa yang membayar?** "Bank B2B2C" tanpa alasan regulasi, harga, dan biaya per pengguna terdengar seperti angan-angan.
7. **Tanpa bukti pengguna:** tidak ada survei, wawancara, atau uji wireframe.
8. **Ketergantungan pada keluarga:** bagaimana kalau anak tidak membalas atau lansia tinggal sendiri?
9. **Alarm palsu** bisa membuat lansia jenuh dan mengabaikan peringatan.
10. **Deepfake:** kalau mengklaim bisa mendeteksi suara palsu, juri A akan "menyerang" soal akurasinya.

## 3. Keputusan: pertahankan JagaOrtu, tapi rombak menjadi v2
Saya membandingkan JagaOrtu dengan 5 ide lain memakai rubrik yang sama, dengan asumsi kualitas eksekusi setara:

| Ide | Masalah | Inovasi | AI | Bisnis | Dampak | Penyampaian | Total | Catatan juri |
|---|---|---|---|---|---|---|---|---|
| **JagaOrtu v2** (dipilih) | 90 | 84 | 85 | 77 | 85 | 88 | **±85** | Data resmi terkuat, tema "AI secukupnya" terjawab, cocok dengan latar keamananmu |
| Asisten kader posyandu (stunting) | 88 | 72 | 80 | 70 | 88 | 85 | ±80 | Topik ramai; butuh pakar gizi |
| Asisten layanan publik bersuara (bansos/BPJS) | 85 | 75 | 80 | 65 | 85 | 85 | ±79 | Bisnis lemah |
| Penerjemah bahasa isyarat (BISINDO) | 85 | 70 | 80 | 60 | 85 | 85 | ±77 | Sangat berisiko gagal demo di final 24 jam |
| Laporan banjir komunitas | 82 | 70 | 78 | 65 | 82 | 85 | ±77 | Sudah banyak tim membuat ide serupa |
| Teman curhat lansia (kesehatan mental) | 80 | 65 | 75 | 65 | 80 | 85 | ±74 | Risiko etika/klinis; sangat ramai |

**Kenapa JagaOrtu v2 menang di atas kertas:**
1. Datanya resmi dan sangat baru:
   - IASC 702.342 laporan.
   - *Fake call* menimbulkan kerugian terlapor terbesar, Rp2,09 T.
   - Jawa Barat provinsi tertinggi, dan ITB ada di sana (lokasi pilot).
   - Literasi keuangan usia 51–79 tahun hanya 54,55%.
2. Kalimat kunci tema ("kapan, bagaimana, sejauh mana AI perlu digunakan") dijawab langsung oleh desain empat lapis.
3. Polanya cocok dengan karya yang pernah menang: kelompok rentan, AI multimodal, presentasi kuat.
4. Kredibel untuk timmu: anak Elektro berlatar keamanan siber membahas anti-penipuan.

### Perubahan v1 → v2 (setiap perubahan menutup satu kelemahan)
| Kelemahan | Perbaikan di v2 |
|---|---|
| 1. Pull | **Penjaga Otomatis**: membaca notifikasi WA/SMS (NotificationListenerService) di perangkat, tanpa perlu curiga lebih dulu |
| 2. Google/Truecaller | **Tabel pembeda**: Google Fake Call Detection bergantung pada Phone by Google dan tidak mencakup WhatsApp; v2 juga satu-satunya yang melibatkan orang kedua |
| 3. Telepon | **CallScreeningService** + pengingat kata sandi + pertanyaan setelah telepon; ditegaskan *tidak merekam* |
| 4. Privasi | Proses di perangkat lebih dulu, PII disamarkan sebelum ke cloud, isi tidak disimpan, kontak keluarga tidak dibaca, Pendamping hanya melihat ringkasan, mengacu UU 27/2022 |
| 5. Data & evaluasi | 4 sumber data, taksonomi 8 modus selaras IASC, dua anotator + kappa, target recall/alarm palsu, uji *teach-back* |
| 6. Bisnis | Pemicu regulasi **POJK 12/2024** (bank wajib punya strategi anti-fraud), harga asumsi, biaya LLM <Rp1.000/pengguna/bulan, kanal komunitas |
| 7. Bukti pengguna | Instrumen survei, wawancara, dan uji wireframe siap pakai (folder 06); proposal otomatis memasukkan hasilnya |
| 8. Keluarga tak merespons | Pendamping cadangan + eskalasi 10 menit + kader komunitas |
| 9. Alarm palsu | Ambang yang bisa disetel, tombol "ini aman" sebagai umpan balik, target ≤10% |
| 10. Deepfake | Sengaja **tidak** mengklaim deteksi; memakai verifikasi prosedural (kata sandi, telepon balik). Ini justru poin kematangan berpikir |
| (bonus) Inovasi | **Latihan Waspada** (simulasi aman, prinsip *inoculation*) + konsep "Aturan Dua Orang" yang mudah diingat |

## 4. Skor JagaOrtu v2 (paket berkas di folder ini)
| Aspek (bobot) | Juri A | Juri B | Juri C |
|---|---|---|---|
| Masalah & tema (20) | 90 | 90 | 90 |
| Inovasi & solusi (20) | 84 | 86 | 83 |
| Rancangan AI (20) | 87 | 84 | 82 |
| Bisnis (15) | 72 | 75 | 80 |
| Dampak (15) | 85 | 85 | 88 |
| Penyampaian (10) | 88 | 88 | 88 |
| **Total** | **84,6** | **84,8** | **85,0** |

**Rata-rata: ±85/100** (tanpa data validasi pengguna).
- **Dengan data survei, wawancara, dan uji wireframe yang asli: ±87–88.** Masalah, inovasi, dan dampak naik karena tervalidasi.
- **Video dengan suara/wajah tim asli** (bukan TTS) menambah sekitar +1 di penyampaian.

### Proyeksi babak final (kalau lolos 10 besar)
| Aspek final | Bobot | Perkiraan | Penentu |
|---|---|---|---|
| Fungsionalitas & kualitas prototipe | 25% | 80–88 | Demo live: kirim WA penipuan ke HP "Ibu" → peringatan bersuara → HP "Rina" bergetar |
| Implementasi AI | 20% | 85 | Empat lapis benar-benar jalan; LLM dipanggil hanya saat ambigu (tunjukkan log) |
| Kesesuaian tema & validasi dampak | 15% | 88 | Bawa kutipan/angka dari wawancara lansia |
| Bisnis & operasional | 15% | 78 | POJK 12/2024 + biaya per pengguna |
| Konsistensi karya | 10% | 90 | MVP sama dengan proposal (lihat rencana 24 jam) |
| Pitching & tanya-jawab | 15% | 85 | Latih 25 pertanyaan di bank tanya-jawab |
| **Total** | | **±84** | |

## 5. Peluang (perkiraan kualitatif)
- **Lolos 10 besar:** tinggi, *jika* semua berkas dikirim lengkap sesuai format, nama/NIM terisi, dan data validasi asli dimasukkan.
- **Juara 1:** sangat ditentukan oleh 24 jam final dan demo yang tidak boleh gagal. Lihat `07_Final_24Jam`.
- **Best Presentation:** peluang realistis. Konsepnya mudah diceritakan dan ada momen suara bahasa Sunda.

## 6. Yang masih harus dikerjakan tim (tidak bisa saya lakukan untukmu)
1. Isi nama, NIM, prodi, dan kampus di `config_tim.json`, lalu jalankan `python build_all.py`.
2. **Jalankan validasi asli** (folder 06). Isi angkanya ke `config_tim.json`. **Jangan mengarang angka.**
3. Minta penutur asli bahasa Sunda mengecek kalimat peringatan di video (segmen 12).
4. Opsional tapi disarankan: rekam ulang narasi dengan suara anggota tim (`build/audio/custom/segNN.mp3`), lalu tambahkan cuplikan wajah tim di bagian perkenalan.
5. Tanda tangan surat orisinalitas: ketua di atas meterai Rp10.000, anggota lain boleh digital.
6. Isi dokumen ini disusun dengan bantuan AI. Pastikan seluruh tim memahami dan menyetujui setiap klaim. Kalau ragu soal aturan "bantuan pihak luar" (guidebook, aturan umum Hackvidia nomor 7), tanyakan ke panitia (Abel, WA +62 813 3334 5625).
