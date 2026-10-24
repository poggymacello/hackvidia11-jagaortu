"""Low-fidelity wireframes for JagaOrtu (grayscale), rendered to PNG.

Outputs:
  build/wf/A1.png ... A8.png        single screens (for video)
  03_Wireframe/Lampiran_A_*.png      annotated sheets (for proposal appendix)
"""
from common import BUILD, ROOT, render, write

CSS = """
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Arial, sans-serif; color: #1d1d1d; background: #fff; }
.phone { width: 360px; height: 760px; border: 3px solid #2b2b2b; border-radius: 38px; padding: 14px 16px;
         position: relative; background: #fff; overflow: hidden; }
.notch { width: 110px; height: 18px; border-radius: 0 0 12px 12px; background: #2b2b2b; margin: -14px auto 6px; }
.sb { display: flex; justify-content: space-between; font-size: 12px; color: #777; margin-bottom: 10px; }
h1 { font-size: 23px; margin: 4px 0 10px; line-height: 1.2; }
h2 { font-size: 19px; margin: 6px 0; }
.sub { font-size: 15px; color: #555; margin: 0 0 10px; }
.card { border: 2px solid #3a3a3a; border-radius: 14px; padding: 11px 12px; margin: 8px 0; background: #fff; }
.card.soft { border-color: #9a9a9a; background: #f3f3f3; }
.btn { display: block; width: 100%; border: 2.5px solid #222; border-radius: 14px; padding: 12px; font-size: 19px;
       font-weight: 700; text-align: center; margin: 8px 0; background: #fff; }
.btn.pri { background: #2b2b2b; color: #fff; }
.btn.sm { font-size: 15px; padding: 8px; font-weight: 600; }
.link { text-align: center; font-size: 14px; text-decoration: underline; color: #555; margin-top: 6px; }
.row { display: flex; gap: 8px; align-items: center; }
.av { width: 40px; height: 40px; border-radius: 50%; border: 2px solid #333; display: flex; align-items: center;
      justify-content: center; font-weight: 700; background: #e6e6e6; flex: none; }
.ph { background: repeating-linear-gradient(45deg,#eee,#eee 6px,#ddd 6px,#ddd 12px); border: 2px dashed #999; border-radius: 10px; }
.tog { width: 44px; height: 24px; border-radius: 12px; border: 2px solid #333; position: relative; flex: none; background: #bbb; }
.tog::after { content: ''; position: absolute; top: 2px; right: 2px; width: 16px; height: 16px; border-radius: 50%; background: #222; }
.tog.off { background: #fff; } .tog.off::after { left: 2px; right: auto; background: #999; }
.big { font-size: 20px; line-height: 1.35; }
.mic { width: 190px; height: 190px; border-radius: 50%; border: 4px solid #222; margin: 14px auto 6px; display: flex;
       flex-direction: column; align-items: center; justify-content: center; background: #ececec; font-weight: 800; font-size: 22px; }
.wave { height: 46px; margin: 10px 0; background: repeating-linear-gradient(90deg,#333 0 3px,transparent 3px 9px);
        mask: linear-gradient(#000,#000); clip-path: polygon(0 40%,5% 10%,10% 60%,15% 20%,20% 70%,25% 30%,30% 80%,35% 15%,40% 65%,45% 25%,50% 90%,55% 20%,60% 70%,65% 35%,70% 85%,75% 25%,80% 60%,85% 15%,90% 55%,95% 30%,100% 50%,100% 100%,0 100%); }
.bubble { border: 2px solid #8a8a8a; border-radius: 14px 14px 14px 4px; padding: 9px 11px; font-size: 15px; background: #f5f5f5; margin: 6px 0; }
.bubble.me { border-radius: 14px 14px 4px 14px; margin-left: 40px; background: #fff; }
.sheet { position: absolute; left: 0; right: 0; bottom: 0; border-top: 3px solid #222; border-radius: 22px 22px 0 0;
         padding: 14px 16px 16px; background: #fff; box-shadow: 0 -8px 0 rgba(0,0,0,.08); }
.dim { position: absolute; inset: 0; background: rgba(0,0,0,.28); }
.tag { display: inline-block; border: 1.5px solid #333; border-radius: 8px; padding: 1px 7px; font-size: 12px; font-weight: 700; }
ul.r { padding-left: 20px; margin: 6px 0; font-size: 17px; line-height: 1.45; }
.mk { position: absolute; width: 30px; height: 30px; border-radius: 50%; background: #111; color: #fff; font-weight: 800;
      display: flex; align-items: center; justify-content: center; font-size: 15px; border: 2px solid #fff; z-index: 9; }
.small { font-size: 13px; color: #555; }
"""

def mk(n, top, left):
    return f'<div class="mk" style="top:{top}px;left:{left}px">{n}</div>'

SCREENS = {}

SCREENS["A1"] = ("Pemasangan oleh anak (3 langkah)", f"""
<div class="notch"></div><div class="sb"><span>09.41</span><span>JagaOrtu</span></div>
<h1>Pasang JagaOrtu untuk Ibu</h1>
<div class="row" style="gap:6px;margin-bottom:6px"><span class="tag">1 Izin</span><span class="tag">2 Pendamping</span><span class="tag">3 Kata sandi</span></div>
<div class="card"><h2>1. Izin baca notifikasi</h2>
<div class="row" style="justify-content:space-between"><span style="font-size:15px">WhatsApp &amp; SMS dari nomor tak dikenal</span><div class="tog"></div></div>
<div class="small">Hanya untuk mendeteksi pesan berisiko. Isi pesan tidak disimpan.</div></div>
<div class="card"><h2>2. Pilih Pendamping</h2>
<div class="row"><div class="av">R</div><div style="font-size:16px"><b>Rina</b> (anak) - utama</div></div>
<div class="row" style="margin-top:6px"><div class="av">A</div><div style="font-size:16px"><b>Andi</b> (anak) - cadangan</div></div>
<div class="small" style="margin-top:6px">+ Tambah pendamping</div></div>
<div class="card"><h2>3. Kata sandi keluarga</h2>
<div style="font-size:16px">Kata sandi: <b>"nasi liwet"</b></div>
<div style="font-size:16px;margin-top:4px">Bahasa suara: <b>Sunda</b> &#9662;</div></div>
<div class="btn pri">Selesai - Ibu terlindungi</div>
{mk(1,150,318)}{mk(2,268,318)}{mk(3,430,318)}
""", ["Izin eksplisit dan terbatas: hanya notifikasi berisiko, isi tidak disimpan.",
      "Pendamping cadangan dipanggil bila pendamping utama tidak menjawab.",
      "Kata sandi keluarga untuk memverifikasi telepon 'darurat' (anti kloning suara)."])

SCREENS["A2"] = ("Beranda lansia", f"""
<div class="notch"></div><div class="sb"><span>07.30</span><span>JagaOrtu</span></div>
<h1>Selamat pagi,<br>Bu Rukmini</h1>
<div class="card soft"><div class="row"><div class="av" style="width:46px;height:46px">&#10003;</div>
<div><div style="font-size:20px;font-weight:800">Ibu terlindungi</div><div style="font-size:15px">Rina siap membantu</div></div></div></div>
<div class="mic">&#127908;<div>TANYA DULU</div></div>
<div style="text-align:center;font-size:16px;color:#444;margin-bottom:6px">Tekan lalu ceritakan,<br>atau bagikan pesan ke sini</div>
<div class="btn">&#128222; Telepon Rina</div>
<div class="btn">&#128222; Telepon Andi</div>
<div class="card soft" style="font-size:15px">Latihan hari ini: 1 pesan &#8250;</div>
{mk(1,270,292)}{mk(2,150,300)}{mk(3,520,300)}
""", ["Satu tombol utama yang besar: 'Tanya Dulu' (bicara atau bagikan pesan).",
      "Teks besar, kontras tinggi, maksimal dua aksi utama per layar.",
      "Pendamping dapat dihubungi dalam satu ketukan."])

SCREENS["A3"] = ("Peringatan otomatis atas pesan WhatsApp", f"""
<div class="notch"></div><div class="sb"><span>13.05</span><span>WhatsApp</span></div>
<div class="row"><div class="av">?</div><div><b>+62 813-xxxx-2190</b><div class="small">nomor baru</div></div></div>
<div class="bubble">Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer 5 juta ke rek BRI 1234-xxxx, cepat ya. Jangan bilang Papa dulu.</div>
<div class="dim"></div>
<div class="sheet">
<div class="row" style="justify-content:space-between"><span class="tag" style="background:#222;color:#fff">MERAH &middot; risiko tinggi</span><span class="tag">&#128266; Sunda</span></div>
<h1 style="margin:6px 0 0">Tunggu dulu, Bu.</h1>
<div style="font-size:16px;margin:4px 0 2px">Pesan ini punya 3 tanda penipuan:</div>
<ul class="r"><li>Nomor baru mengaku anak</li><li>Minta transfer cepat</li><li>Minta dirahasiakan</li></ul>
<div class="btn pri">Tanya Rina dulu</div>
<div class="btn">Telepon Andi (nomor lama)</div>
<div class="link">Ini aman (beri tahu JagaOrtu)</div>
</div>
{mk(1,420,232)}{mk(2,548,318)}{mk(3,630,326)}
""", ["Tingkat Merah: muncul otomatis dan dibacakan dalam bahasa pilihan lansia (Kuning hanya notifikasi bersuara).",
      "Alasan konkret (tanda-tanda), bukan vonis 'pasti penipuan'.",
      "Aksi utama adalah orang kedua; 'Ini aman' mengoreksi AI dan lansia tetap memutuskan."])

SCREENS["A4"] = ("Tanya Dulu dengan suara", f"""
<div class="notch"></div><div class="sb"><span>16.12</span><span>JagaOrtu</span></div>
<h1>Ceritakan saja, Bu</h1>
<div class="wave"></div>
<div class="bubble me">"Tadi ada yang telepon, ngaku polisi. Katanya Andi ditahan, minta uang damai 10 juta."</div>
<div class="card"><div style="font-size:17px;font-weight:800">Ini pola penipuan "keluarga ditahan polisi".</div>
<div style="font-size:16px;margin-top:4px">Polisi tidak meminta uang damai lewat telepon.</div>
<div style="font-size:16px;margin-top:8px"><b>Yang sebaiknya Ibu lakukan:</b></div>
<ol style="font-size:16px;padding-left:22px;margin:4px 0;line-height:1.45"><li>Tutup teleponnya.</li><li>Telepon Andi di nomor tersimpan.</li><li>Kabari Rina.</li></ol></div>
<div class="btn pri">&#128222; Telepon Andi</div>
<div class="btn">Kabari Rina</div>
{mk(1,92,300)}{mk(2,236,318)}{mk(3,372,318)}
""", ["Ucapan lansia diubah menjadi teks (speech-to-text).",
      "Penjelasan bahasa sederhana + langkah konkret, tanpa istilah teknis.",
      "Jawaban juga dibacakan; tombol langsung ke tindakan aman."])

SCREENS["A5"] = ("Panggilan masuk dari nomor tak dikenal", f"""
<div class="notch"></div><div class="sb"><span>20.47</span><span>Telepon</span></div>
<div style="text-align:center;margin-top:18px"><div class="av" style="width:84px;height:84px;margin:0 auto;font-size:30px">?</div>
<div style="font-size:22px;font-weight:800;margin-top:8px">+62 812-xxxx-7781</div><div class="small">Nomor tidak dikenal</div></div>
<div class="card" style="margin-top:16px"><div style="font-size:15px;font-weight:800">JagaOrtu mengingatkan:</div>
<div style="font-size:16px">Jika penelepon mengaku keluarga atau polisi dan minta uang, <b>tanyakan kata sandi keluarga</b>.</div></div>
<div class="row" style="margin-top:6px"><div class="btn" style="margin:0">Tolak</div><div class="btn pri" style="margin:0">Angkat</div></div>
<div class="card soft" style="margin-top:18px"><div class="small">Setelah telepon ditutup:</div>
<div style="font-size:17px;font-weight:700">Tadi penelepon minta uang?</div>
<div class="row"><div class="btn sm">Ya, minta</div><div class="btn sm">Tidak</div></div></div>
{mk(1,40,300)}{mk(2,250,318)}{mk(3,470,318)}
""", ["Memakai CallScreeningService Android: hanya identitas panggilan, tidak merekam isi.",
      "Pengingat kata sandi keluarga, karena suara kini bisa dikloning AI.",
      "Pertanyaan pasca-telepon memicu Tanya Dulu bila ada permintaan uang."])

SCREENS["A6"] = ("Aplikasi Pendamping: notifikasi ke anak", f"""
<div class="notch"></div><div class="sb"><span>13.06</span><span>JagaOrtu Pendamping</span></div>
<h1>Hai Rina</h1>
<div class="card"><div style="font-size:17px;font-weight:800">&#9888; Ibu butuh bantuanmu</div><div class="small">2 menit lalu</div>
<div style="font-size:16px;margin-top:6px"><b>Modus:</b> mengaku anak (nomor baru)<br><b>Permintaan:</b> transfer Rp5.000.000<br><b>Tanda lain:</b> minta dirahasiakan</div>
<div style="font-size:15px;margin-top:6px">Ibu menekan <b>"Tanya Rina dulu"</b></div></div>
<div class="btn pri">&#128222; Telepon Ibu sekarang</div>
<div class="btn">Kirim: "Jangan transfer, Bu"</div>
<div class="btn">Tandai aman</div>
<div class="small" style="text-align:center">Isi pesan lengkap hanya terlihat jika Ibu mengizinkan.</div>
<div class="card soft small">Belum dijawab 10 menit &rarr; Andi (cadangan) dihubungi otomatis.</div>
{mk(1,130,318)}{mk(2,330,318)}{mk(3,478,318)}
""", ["Ringkasan risiko, bukan isi chat: privasi lansia tetap terjaga.",
      "Satu ketukan untuk menelepon atau mengirim pesan penenang.",
      "Eskalasi ke pendamping cadangan bila tidak ada respons."])

SCREENS["A7"] = ("Latihan Waspada (simulasi aman)", f"""
<div class="notch"></div><div class="sb"><span>19.00</span><span>JagaOrtu Pendamping</span></div>
<h1>Latihan Waspada untuk Ibu</h1>
<div class="card soft"><div style="font-size:18px;font-weight:800">Bulan ini: 3 dari 4 dikenali &#10003;</div></div>
<div class="card" style="font-size:16px;line-height:1.7">
&#10003; Hadiah undian palsu<br>&#10003; Undangan nikah berisi file .apk<br>&#10007; CS bank palsu <span class="small">(pelajaran suara dikirim)</span><br>&#10003; "Anak" minta transfer</div>
<div class="btn pri">Jadwalkan latihan berikutnya</div>
<div class="card soft small">Disetujui Ibu &middot; maks. 1 latihan per minggu. Selalu diakhiri penjelasan yang menenangkan. Tidak ada uang atau data yang terlibat.</div>
{mk(3,95,318)}{mk(2,250,318)}{mk(1,300,326)}
""", ["Simulasi aman atas persetujuan lansia ('imunisasi' kewaspadaan), dijadwalkan bersama keluarga.",
      "Saat keliru, lansia menerima pelajaran suara 30 detik, tanpa menyalahkan.",
      "Hasil dibagikan ke keluarga hanya atas persetujuan lansia; frekuensi dibatasi."])

SCREENS["A8"] = ("Privasi dan kendali di tangan lansia", f"""
<div class="notch"></div><div class="sb"><span>10.15</span><span>JagaOrtu</span></div>
<h1>Yang dibaca JagaOrtu</h1>
<div class="card"><div class="row" style="justify-content:space-between"><span style="font-size:16px">Pesan dari nomor tak dikenal</span><div class="tog"></div></div></div>
<div class="card"><div class="row" style="justify-content:space-between"><span style="font-size:16px">Pesan berisi uang, tautan, atau file</span><div class="tog"></div></div></div>
<div class="card"><div class="row" style="justify-content:space-between"><span style="font-size:16px">Pesan dari kontak keluarga</span><div class="tog off"></div></div></div>
<div class="card soft" style="font-size:16px">Diproses di HP Ibu. Isi pesan tidak disimpan. Rina hanya melihat ringkasan risiko.</div>
<div class="card"><div class="row" style="justify-content:space-between"><span style="font-size:16px"><b>Pendamping:</b> Rina, Andi</span><span class="tag">Ubah</span></div>
<div class="small">Pendamping tidak bisa membaca chat, menyetujui, atau memindahkan uang.</div></div>
<div class="btn">Jeda perlindungan 1 jam</div>
<div class="btn">Hapus semua riwayat</div>
{mk(1,100,318)}{mk(2,330,318)}{mk(3,420,318)}
""", ["Minimisasi data sesuai UU No. 27 Tahun 2022 (Pelindungan Data Pribadi).",
      "Pemrosesan di perangkat terlebih dahulu; cloud hanya untuk kasus ambigu.",
      "Lansia memilih atau mengganti Pendamping, menjeda, dan menghapus riwayat kapan saja."])


def screen_html(key):
    title, body, _ = SCREENS[key]
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS} body{{padding:20px}}</style></head><body><div class='phone' id='p'>{body}</div></body></html>"


def sheet_html(keys, sheet_title):
    cells = []
    for k in keys:
        title, body, notes = SCREENS[k]
        notes_html = "".join(f"<div class='nt'><span class='nn'>{i+1}</span>{n}</div>" for i, n in enumerate(notes))
        cells.append(f"<div class='cell'><div class='cap'>Gambar {k}. {title}</div><div class='phone'>{body}</div><div class='notes'>{notes_html}</div></div>")
    extra = """
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:28px 36px;padding:26px 30px}
    .cell{display:flex;flex-direction:column;align-items:center}
    .cap{font-family:'Times New Roman',serif;font-size:21px;font-weight:700;margin-bottom:10px;text-align:center}
    .notes{width:360px;margin-top:10px}
    .nt{font-size:15px;line-height:1.35;margin:4px 0;display:flex;gap:8px}
    .nn{flex:none;width:22px;height:22px;border-radius:50%;background:#111;color:#fff;font-weight:800;font-size:13px;display:flex;align-items:center;justify-content:center}
    .ttl{font-family:'Times New Roman',serif;font-size:26px;font-weight:700;text-align:center;padding-top:22px}
    """
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body id='s'>"
            f"<div class='ttl'>{sheet_title}</div><div class='grid'>{''.join(cells)}</div></body></html>")


def main():
    wf = BUILD / "wf"
    jobs = []
    for k in SCREENS:
        h = write(wf / f"{k}.html", screen_html(k))
        jobs.append({"type": "png", "html": h, "out": wf / f"{k}.png", "selector": "#p", "width": 420, "height": 820, "scale": 3})
    out = ROOT / "03_Wireframe"
    sheets = [
        (["A1", "A2"], "Lampiran A - Wireframe (1/4): pemasangan oleh anak dan beranda lansia", "Lampiran_A1"),
        (["A3", "A4"], "Lampiran A - Wireframe (2/4): peringatan otomatis dan Tanya Dulu", "Lampiran_A2"),
        (["A5", "A6"], "Lampiran A - Wireframe (3/4): telepon masuk dan aplikasi Pendamping", "Lampiran_A3"),
        (["A7", "A8"], "Lampiran A - Wireframe (4/4): Latihan Waspada dan privasi", "Lampiran_A4"),
    ]
    for keys, ttl, name in sheets:
        h = write(BUILD / f"{name}.html", sheet_html(keys, ttl))
        jobs.append({"type": "png", "html": h, "out": out / f"{name}.png", "width": 900, "height": 1200, "scale": 2, "full_page": True})
    render(jobs)
    # copy single screens to deliverable folder too
    import shutil
    for k in SCREENS:
        shutil.copy(wf / f"{k}.png", out / f"{k}.png")
    print("wireframes ok")


if __name__ == "__main__":
    main()
