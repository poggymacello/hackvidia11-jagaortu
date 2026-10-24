# Skenario demo: HP "Ibu" → HP "Rina"

**Perangkat:** 3 HP + 1 laptop.
| Label (stiker di casing) | Peran | Isi |
|---|---|---|
| **HP-IBU** | Bu Rukmini (67) | Android 13–15, WhatsApp + SIM aktif, JagaOrtu Ibu (akses notifikasi aktif), volume 80%, huruf sistem besar |
| **HP-RINA** | Rina, anak di Jakarta | Chrome + PWA Pendamping terpasang, izin notifikasi aktif, getar aktif |
| **HP-PENIPU** | "Andi palsu" | WhatsApp dengan nomor yang **tidak** tersimpan di HP-IBU; draf 3 pesan disiapkan (lihat di bawah) |
| **LAPTOP** | Operator | Deck, mirroring HP-IBU & HP-RINA (scrcpy/kamera dokumen), log keputusan backend, tab simulasi web, video cadangan |

Kontak "Andi (asli)" dan "Rina" tersimpan di HP-IBU dengan nomor yang berbeda dari HP-PENIPU.

## Pesan yang disiapkan di HP-PENIPU (salin persis)
1. **Jelas penipuan → L0:** `Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer 5 juta sekarang ke rek BRI 1234xxxx a.n. Budi, buat bayar rumah sakit. Jangan bilang Papa dulu ya.`
2. **Ambigu → L2 (LLM):** `Bu, saya dari kantor pos, paketnya tertahan. Mohon dicek dulu ya bu biar bisa dikirim hari ini, nanti saya bantu prosesnya` (tanpa kata "transfer"/"OTP" agar tidak tertangkap L0)
3. **Aman → tidak ada peringatan:** dikirim dari **kontak tersimpan** (HP-RINA atau HP lain): `Bu, nanti sore aku telepon ya. Jangan lupa makan.`

> Uji ketiganya ≥5× pada H+18–20 dan catat lapis yang memutuskan. Kalau pesan 2 ternyata tertangkap L0/L1 dengan yakin, ubah redaksinya sampai benar-benar ambigu, atau pilih pesan ambigu lain dari set evaluasi. Jangan memalsukan log.

## Alur (1:30 menit)
| # | Detik | Aksi operator | Yang terlihat/terdengar | Narasi P1 |
|---|---|---|---|---|
| 1 | 0–20 | HP-PENIPU kirim **pesan 1** | Notifikasi WA masuk di HP-IBU → < 2 dtk heads-up "Tunggu dulu, Bu" + **suara** "Tunggu dulu, Bu. Pesan ini minta transfer cepat dan minta dirahasiakan. Tanya Rina dulu, ya." | "Ibu tidak menyentuh apa pun. JagaOrtu yang lebih dulu bicara." |
| 2 | 20–45 | Ketuk notifikasi → layar besar A3 → tekan **Tanya Rina dulu** | HP-IBU: "Rina sudah diberi tahu". **HP-RINA bergetar**: "Ibu butuh bantuan: kemungkinan penipuan mengaku keluarga, minta transfer, minta dirahasiakan" | "Rina tidak membaca chat ibunya. Ia hanya tahu risikonya, lalu satu ketukan untuk menelepon." |
| 3 | 45–60 | HP-RINA tekan **Telepon Ibu** | HP-IBU berdering dari "Rina" | "Keputusan tidak lagi diambil sendirian." (tolak/akhiri panggilan setelah 2 dering) |
| 4 | 60–80 | HP-PENIPU kirim **pesan 2** | Log di laptop: L0 tidak yakin → L1 skor [x] → **L2 dipanggil**, teks tampak tersamar → peringatan dengan penjelasan "modus paket/kurir" | "Baru di kasus ambigu seperti ini AI besar dipanggil, dengan data yang disamarkan." |
| 5 | 80–90 | Kirim **pesan 3** dari kontak tersimpan | Tidak ada peringatan; log: "dilewati: kontak tersimpan" | "Pesan keluarga biasa tidak diganggu. Alarm palsu adalah musuh kami." |
| (P1) | +20 | Bila eskalasi aktif: diamkan notifikasi Rina 30 dtk (mode demo) | HP cadangan menerima push | "Kalau Rina sibuk, pendamping cadangan dihubungi." |

## Jalur cadangan (latih juga)
| Gagal di | Gejala | Pindah ke |
|---|---|---|
| WA tidak masuk / sinyal | Tidak ada notifikasi 10 dtk | Kirim **SMS** berisi pesan 1 dari HP-PENIPU (SIM) |
| Android app crash | — | **Simulasi web**: ketik pesan 1 di chat web → backend yang sama → push ke HP-RINA tetap sungguhan |
| Internet total mati | LLM & push gagal | Pesan 1 tetap memicu L0 + suara offline di HP-IBU; lalu putar **video demo** untuk bagian Rina |
| Semua gagal | — | Video demo (≤5 menit, sudah diunggah dan diunduh offline) |

## Persiapan 30 menit sebelum pitch
1. Semua HP terisi ≥80%, mode pesawat **mati**, hotspot cadangan menyala, Wi-Fi panitia diuji.
2. HP-IBU: Jangan Ganggu **mati**; notifikasi WA untuk chat HP-PENIPU **tidak dibisukan**; pratinjau pesan aktif; aplikasi JagaOrtu terbuka di latar (foreground service berjalan).
3. Hapus riwayat chat dan event demo sebelumnya (supaya layar bersih), tetapi **jangan** menghapus izin.
4. HP-RINA: layar menyala (timeout 10 menit), PWA terbuka di tab, getar aktif.
5. Kirim 1 pesan uji 10 menit sebelumnya; pastikan berhasil; bersihkan lagi.
6. Laptop: tab deck, tab log, tab simulasi web, file video cadangan, semuanya terbuka; notifikasi laptop dimatikan.
