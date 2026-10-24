"""Lean Canvas (1 page, A4 landscape) -> 01_LeanCanvas/<Tim>_LeanCanvas.pdf (+ PNG for video)"""
from common import BUILD, ROOT, load_config, render, write

def html(cfg):
    tim = cfg["nama_tim"]
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>
@page {{ size: A4 landscape; margin: 9mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Segoe UI', Arial, sans-serif; color: #15202b; }}
#lc {{ width: 279mm; height: 192mm; display: flex; flex-direction: column; }}
.hd {{ display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 3px solid #23395d; padding-bottom: 4px; margin-bottom: 5px; }}
.hd h1 {{ margin: 0; font-size: 21px; color: #23395d; }}
.hd .m {{ font-size: 11px; color: #444; text-align: right; line-height: 1.35; }}
.g {{ flex: 1; display: grid; grid-template-columns: repeat(10, 1fr); grid-template-rows: 1fr 0.92fr 0.58fr; gap: 4px; }}
.b {{ border: 1.8px solid #23395d; border-radius: 6px; padding: 5px 7px; overflow: hidden; background: #fff; }}
.b h2 {{ margin: 0 0 4px; font-size: 13.5px; color: #fff; background: #23395d; display: inline-block; padding: 1px 7px; border-radius: 4px; }}
.b ul {{ margin: 2px 0 0; padding-left: 14px; font-size: 12.4px; line-height: 1.34; }}
.b li {{ margin-bottom: 2px; }}
.b p {{ margin: 2px 0; font-size: 12.4px; line-height: 1.34; }}
.sub {{ margin-top: 4px; border-top: 1.2px dashed #8a99b3; padding-top: 3px; }}
.sub b {{ font-size: 12.4px; color: #23395d; }}
.uvp p.big {{ font-size: 17px; font-weight: 800; color: #23395d; line-height: 1.25; margin: 4px 0; }}
.p {{ grid-column: 1 / 3; grid-row: 1 / 3; }}
.s {{ grid-column: 3 / 5; grid-row: 1 / 2; }}
.k {{ grid-column: 3 / 5; grid-row: 2 / 3; }}
.u {{ grid-column: 5 / 7; grid-row: 1 / 3; background: #f3f6fb; }}
.a {{ grid-column: 7 / 9; grid-row: 1 / 2; }}
.c {{ grid-column: 7 / 9; grid-row: 2 / 3; }}
.cs {{ grid-column: 9 / 11; grid-row: 1 / 3; }}
.co {{ grid-column: 1 / 6; grid-row: 3 / 4; }}
.r {{ grid-column: 6 / 11; grid-row: 3 / 4; }}
.ft {{ font-size: 9.3px; color: #555; margin-top: 3px; }}
</style></head><body><div id='lc'>
<div class='hd'><h1>Lean Canvas - JagaOrtu: Aturan Dua Orang Berbasis AI untuk Melindungi Lansia dari Penipuan Digital</h1>
<div class='m'>Tim: <b>{tim}</b> &middot; Hackvidia Arkavidia 11.0<br>Subtema: {cfg['subtema']}</div></div>
<div class='g'>
<div class='b p'><h2>Problem</h2><ul>
<li>Lansia diminta uang/data dalam situasi <b>mendesak dan sendirian</b>: telepon/WA mengaku anak, polisi, petugas bank; link &amp; file .apk; undian. IASC OJK: <b>702.342 laporan</b> (Nov 2024-Sep 2026); <i>fake call</i> 63.517 laporan.</li>
<li><b>Kloning suara AI</b> (3 detik rekaman cukup; McAfee 2023) membuat cara lama "kenali suara anak sendiri" tidak lagi aman. Laporan penipuan berbasis AI: 13 (akhir 2024), 1.379 (total s.d. Jun 2026).</li>
<li>Keluarga baru tahu setelah uang hilang; edukasi umum tidak hadir di momen kritis.</li></ul>
<div class='sub'><b>Existing alternatives</b><p>Edukasi OJK/Komdigi; aplikasi caller ID (Truecaller, Getcontact); Google Fake Call Detection (perlu Phone by Google, tidak mencakup WhatsApp); cek manual cekrekening.id; peringatan generik aplikasi bank.</p></div></div>
<div class='b s'><h2>Solution</h2><ul>
<li><b>Penjaga otomatis</b> WA/SMS di perangkat: jeda + peringatan bersuara (Indonesia/Sunda/Jawa).</li>
<li><b>Tanya Dulu</b>: cerita lewat suara atau bagikan pesan.</li>
<li><b>Aturan Dua Orang</b>: 1 ketuk ke Pendamping + kata sandi keluarga.</li>
<li><b>Latihan Waspada</b>: simulasi penipuan aman.</li></ul></div>
<div class='b k'><h2>Key Metrics</h2><ul>
<li>Lansia aktif mingguan &amp; momen berisiko tertangkap</li>
<li>Check-in Pendamping selesai &lt; 10 menit</li>
<li>Recall modus berisiko tinggi (target &ge;90%) &amp; alarm palsu (target &le;10%)</li>
<li>Tingkat lulus Latihan Waspada; retensi keluarga 3 bulan</li></ul></div>
<div class='b u uvp'><h2>Unique Value Proposition</h2>
<p class='big'>"Saat diminta uang, Ibu tidak lagi sendirian."</p>
<p>Jeda tepat waktu + penjelasan bersuara dalam bahasa lansia + keluarga hadir dalam satu ketukan, <b>sebelum</b> uang berpindah, tanpa membaca seluruh chat.</p>
<div class='sub'><b>High-level concept</b><p>"Aturan dua orang" ala bank (maker-checker), untuk keluarga.</p></div>
<div class='sub'><b>Prinsip AI secukupnya</b><p>Aturan pasti &rarr; model di perangkat &rarr; LLM hanya untuk kasus ambigu (data disamarkan) &rarr; manusia memutuskan.</p></div></div>
<div class='b a'><h2>Unfair Advantage</h2><ul>
<li>Korpus modus penipuan lokal (termasuk bahasa daerah) yang tumbuh dari laporan komunitas</li>
<li>Efek jaringan keluarga (1 lansia mengikat 2-3 pendamping)</li>
<li>Desain khusus lansia + tim berlatar keamanan siber</li></ul></div>
<div class='b c'><h2>Channels</h2><ul>
<li>Anak memasang di HP orang tua (onboarding 3 langkah)</li>
<li>Komunitas: posyandu lansia, pengajian, PKK, karang werda</li>
<li>Mitra bank/BPR/e-wallet; acara literasi keuangan OJK</li></ul></div>
<div class='b cs'><h2>Customer Segments</h2><ul>
<li><b>Pengguna:</b> lansia 60+ pengguna WA/m-banking (&plusmn;34 juta lansia; 34,13% mengakses internet, 2025)</li>
<li><b>Pembayar keluarga:</b> anak dewasa sebagai Pendamping</li>
<li><b>B2B2C:</b> bank &amp; BPR (wajib strategi anti-fraud, POJK 12/2024), e-wallet, operator seluler</li></ul>
<div class='sub'><b>Early adopters</b><p>Keluarga urban di Jawa Barat (provinsi dengan laporan penipuan terbanyak: 131.445) yang orang tuanya tinggal terpisah.</p></div></div>
<div class='b co'><h2>Cost Structure</h2><ul>
<li>API LLM hanya untuk kasus ambigu (estimasi &lt; Rp10 per analisis; &lt; Rp1.000/pengguna/bulan)*</li>
<li>Text-to-speech/speech-to-text, server &amp; basis data laporan, moderasi taksonomi</li>
<li>Pengembangan aplikasi, akuisisi via komunitas, kepatuhan &amp; keamanan data (UU PDP)</li></ul></div>
<div class='b r'><h2>Revenue Streams</h2><ul>
<li><b>B2B2C:</b> lisensi per pengguna terlindungi untuk bank/BPR/e-wallet (asumsi Rp4.000/pengguna/bulan)*</li>
<li><b>Paket Keluarga:</b> gratis untuk perlindungan dasar; premium Rp25.000/bulan (2 lansia, 3 pendamping, Latihan Waspada)*</li>
<li>Hibah/CSR program literasi digital lansia</li></ul>
<div class='ft'>*Angka harga &amp; biaya adalah asumsi awal untuk divalidasi melalui survei dan pilot.</div></div>
</div></div></body></html>"""


def main():
    cfg = load_config()
    h = write(BUILD / "leancanvas.html", html(cfg))
    out = ROOT / "01_LeanCanvas" / f"{cfg['nama_tim']}_LeanCanvas.pdf"
    render([
        {"type": "pdf", "html": h, "out": out},
        {"type": "png", "html": h, "out": BUILD / "leancanvas.png", "selector": "#lc", "width": 1200, "height": 900, "scale": 2},
    ])
    print("lean canvas ok ->", out)


if __name__ == "__main__":
    main()
