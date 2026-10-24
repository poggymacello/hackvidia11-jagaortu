"""Architecture diagram for JagaOrtu -> build/arch.png"""
from common import BUILD, render, write

HTML = """<!doctype html><html><head><meta charset='utf-8'><style>
*{box-sizing:border-box} body{margin:0;font-family:'Segoe UI',Arial,sans-serif;background:#fff;color:#1b1b1b}
#d{width:1560px;padding:26px 28px 22px;position:relative}
.cols{display:grid;grid-template-columns:1.22fr 118px 1fr 118px 0.86fr;gap:8px;position:relative;z-index:2}
.cn{display:flex;flex-direction:column;justify-content:center;gap:34px}
.ar{text-align:center;font-size:14px;line-height:1.25;color:#23395d}
.ar .g{font-size:40px;line-height:1;font-weight:700}
.col{border:3px solid #23395d;border-radius:18px;padding:14px 14px 12px;background:#f7f9fc}
.col h3{margin:0 0 10px;font-size:23px;color:#23395d;text-align:center}
.box{border:2px solid #4a5b78;border-radius:12px;background:#fff;padding:8px 11px;margin:9px 0;font-size:17px;line-height:1.3}
.box b{font-size:18px}
.l0{border-left:10px solid #2e7d32}.l1{border-left:10px solid #1565c0}.l2{border-left:10px solid #ef6c00}.l3{border-left:10px solid #6a1b9a}
.src{background:#eef2f7}
.small{font-size:14.5px;color:#444}
.lg{display:flex;gap:18px;justify-content:center;margin-top:14px;font-size:16px}
.lg span{display:flex;align-items:center;gap:6px}.sw{width:16px;height:16px;border-radius:4px;display:inline-block}
.dec{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-top:6px}
.dec div{border:2px dashed #777;border-radius:10px;padding:6px;font-size:14.5px;text-align:center;background:#fff}
svg{position:absolute;inset:0;z-index:1}
.ttl{font-size:26px;font-weight:800;text-align:center;margin-bottom:12px;color:#23395d}
</style></head><body><div id='d'>
<div class='ttl'>Arsitektur JagaOrtu: "AI secukupnya", keputusan tetap di tangan manusia</div>
<div class='cols'>
 <div class='col' id='c1'><h3>HP Lansia (Android)</h3>
  <div class='box src'><b>Sumber sinyal</b><br>Notifikasi WA/SMS (NotificationListenerService) · Panggilan masuk (CallScreeningService) · "Tanya Dulu": suara, teks, tangkapan layar</div>
  <div class='box l0'><b>L0 Aturan pasti</b> (tanpa AI)<br><span class='small'>daftar nomor/rekening/domain terlapor, file .apk, permintaan OTP/PIN, kata kunci transfer mendesak</span></div>
  <div class='box l1'><b>L1 Model di perangkat</b><br><span class='small'>klasifikasi teks ringan + OCR on-device; skor risiko s &lt; 100 ms, offline</span></div>
  <div class='dec'><div><b>s &lt; 0,40</b><br>Hijau: diam</div><div><b>0,40&ndash;0,70</b><br>tanya L2</div><div><b>s &ge; 0,70 / L0</b><br>Merah: jeda + suara</div></div>
  <div class='box' style='margin-top:10px'><b>Antarmuka lansia</b><br><span class='small'>Merah: layar jeda dibacakan (TTS perangkat + audio templat Sunda/Jawa); Kuning: notifikasi bersuara; "Ini aman" = koreksi</span></div>
 </div>
 <div class='cn'><div class='ar'><div class='g'>&#10230;</div>hanya kasus ambigu<br>(teks disamarkan)</div><div class='ar'><div class='g'>&#10229;</div>modus + tanda bahaya<br>+ penjelasan</div></div>
 <div class='col' id='c2'><h3>Layanan JagaOrtu (cloud)</h3>
  <div class='box'><b>Gerbang privasi</b><br><span class='small'>penyamaran nomor, nama, rekening sebelum dikirim; tanpa penyimpanan isi pesan</span></div>
  <div class='box l2'><b>L2 Model bahasa besar</b> (hanya kasus ambigu)<br><span class='small'>JSON tervalidasi: risiko, modus (8 kelas), &le;3 tanda bahaya, penjelasan; gagal/timeout &rarr; Kuning; tidak bisa menurunkan putusan L0</span></div>
  <div class='box'><b>Suara</b><br><span class='small'>speech-to-text untuk cerita lansia (Tanya Dulu)</span></div>
  <div class='box'><b>Basis laporan &amp; taksonomi</b><br><span class='small'>laporan komunitas (opt-in, anonim), pembaruan aturan mingguan</span></div>
  <div class='box'><b>Penjadwal Latihan Waspada</b><br><span class='small'>simulasi aman atas izin keluarga</span></div>
 </div>
 <div class='cn'><div class='ar'><div class='g'>&#10230;</div>ringkasan risiko<br>(bukan isi chat)</div><div class='ar'><div class='g'>&#10229;</div>keputusan &amp;<br>telepon balik</div></div>
 <div class='col' id='c3'><h3>Pendamping (keluarga)</h3>
  <div class='box l3'><b>L3 Manusia memutuskan</b><br><span class='small'>lansia memutuskan; AI dan Pendamping tidak pernah mentransfer, memblokir, atau menyetujui</span></div>
  <div class='box'><b>Notifikasi ringkasan risiko</b><br><span class='small'>modus, nominal, tanda bahaya (bukan isi chat)</span></div>
  <div class='box'><b>Aksi 1 ketukan</b><br><span class='small'>telepon lansia · "jangan transfer" · tandai aman</span></div>
  <div class='box'><b>Eskalasi</b><br><span class='small'>10 menit tanpa respons, pendamping cadangan dihubungi</span></div>
  <div class='box' style='border-style:dashed'><b>Mitra (peta jalan)</b><br><span class='small'>API "Jeda Transfer" bank/e-wallet</span></div>
 </div>
</div>
<div class='lg'><span><i class='sw' style='background:#2e7d32'></i>L0 aturan</span><span><i class='sw' style='background:#1565c0'></i>L1 di perangkat</span><span><i class='sw' style='background:#ef6c00'></i>L2 cloud (seperlunya)</span><span><i class='sw' style='background:#6a1b9a'></i>L3 manusia</span></div>
</div></body></html>"""


def main():
    h = write(BUILD / "arch.html", HTML)
    render([{"type": "png", "html": h, "out": BUILD / "arch.png", "selector": "#d", "width": 1560, "height": 980, "scale": 2}])
    print("arch ok")


if __name__ == "__main__":
    main()
