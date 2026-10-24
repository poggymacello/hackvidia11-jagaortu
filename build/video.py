"""Video penjelasan proposal (<= 5 menit) -> 04_Video/<Tim>_Video_Hackvidia.mp4 + .srt + naskah.

Narasi memakai TTS neural (edge-tts). Untuk versi final, tim dapat merekam suara sendiri:
taruh file build/audio/custom/segNN.mp3 dengan nomor segmen yang sama, lalu jalankan ulang skrip ini.
"""
import asyncio
import json
import re
import subprocess
from pathlib import Path

from common import BUILD, ROOT, find_tool, load_config, render, write

FFMPEG = find_tool("ffmpeg")
FFPROBE = find_tool("ffprobe")

NARR = "id-ID-GadisNeural"
ANDI = "id-ID-ArdiNeural"
SUNDA = "su-ID-TutiNeural"
WF = (BUILD / "wf").resolve().as_uri()

# (scene, voice, say, show)
SEG = [
    ("hook", ANDI, "Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer lima juta sekarang, ya. Jangan bilang Papa dulu.",
     "\"Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer 5 juta sekarang, ya. Jangan bilang Papa dulu.\""),
    ("hook", NARR, "Pesan seperti ini datang setiap hari ke ponsel orang tua di Indonesia. Dan kini, suaranya pun bisa dipalsukan. Riset McAfee menunjukkan, tiga detik rekaman sudah cukup untuk membuat tiruan suara yang mirip.",
     "Pesan seperti ini datang setiap hari ke ponsel orang tua di Indonesia. Kini suaranya pun bisa dipalsukan: 3 detik rekaman cukup untuk tiruan suara yang mirip (McAfee, 2023)."),
    ("team", NARR, "Kami Tim JagaOrtu, peserta Hackvidia Arkavidia sebelas. Pertanyaan kami sederhana: bagaimana melindungi orang tua dari penipuan digital, tanpa merampas kemandirian mereka?",
     "Kami Tim JagaOrtu. Pertanyaan kami: bagaimana melindungi orang tua dari penipuan digital, tanpa merampas kemandirian mereka?"),
    ("data", NARR, "Indonesia Anti-Scam Centre OJK menerima lebih dari tujuh ratus dua ribu laporan penipuan sejak November dua ribu dua puluh empat.",
     "IASC OJK menerima 702.342 laporan penipuan (Nov 2024 - Sep 2026)."),
    ("data", NARR, "Modus penipu yang menyamar sebagai keluarga atau petugas menimbulkan kerugian terlapor terbesar, dua koma nol sembilan triliun rupiah.",
     "Modus fake call (menyamar keluarga/petugas): kerugian terlapor terbesar, Rp2,09 triliun."),
    ("data", NARR, "Lansia paling rentan. Literasi keuangan usia lima puluh satu hingga tujuh puluh sembilan tahun hanya lima puluh empat persen, sementara lansia yang online naik dari empat belas menjadi tiga puluh empat persen dalam empat tahun.",
     "Literasi keuangan usia 51-79 tahun hanya 54,55%; lansia yang online naik dari 14,10% (2021) menjadi 34,13% (2025)."),
    ("data", NARR, "Dan Jawa Barat mencatat laporan terbanyak di Indonesia, lebih dari seratus tiga puluh satu ribu laporan.",
     "Jawa Barat: laporan penipuan terbanyak di Indonesia (131.445 laporan)."),
    ("insight", NARR, "Kami menemukan pola yang sama. Penipu menang ketika korbannya panik, ditekan oleh sosok yang tampak berwenang, dan diminta merahasiakan. Keputusan diambil sendirian.",
     "Penipu menang ketika korban panik, ditekan sosok \"berwenang\", dan diminta merahasiakan. Keputusan diambil sendirian."),
    ("insight", NARR, "Edukasi itu penting, tetapi tidak hadir tepat di momen itu. Yang dibutuhkan lansia adalah jeda, dan orang kedua yang dipercaya.",
     "Edukasi penting, tetapi tidak hadir di momen itu. Yang dibutuhkan: jeda, dan orang kedua yang dipercaya."),
    ("concept", NARR, "Karena itu kami membangun JagaOrtu, aturan dua orang berbasis AI. Prinsip yang dipakai bank untuk transaksi berisiko, kini untuk keluarga.",
     "JagaOrtu: aturan dua orang berbasis AI. Prinsip bank untuk transaksi berisiko, kini untuk keluarga."),
    ("A1", NARR, "Anak memasang JagaOrtu di ponsel orang tuanya dalam tiga langkah: izin terbatas, memilih Pendamping, dan menyepakati kata sandi keluarga.",
     "Dipasang oleh anak dalam 3 langkah: izin terbatas, pilih Pendamping, kata sandi keluarga."),
    ("A3", NARR, "Saat pesan berisiko masuk ke WhatsApp, JagaOrtu langsung memberi jeda, dan membacakan tanda-tandanya dalam bahasa yang dipahami Ibu.",
     "Pesan berisiko masuk: JagaOrtu memberi jeda dan membacakan tanda-tandanya dalam bahasa Ibu."),
    ("A3", SUNDA, "Antosan heula, Bu. Pesen ieu menta transfer buru-buru, sareng menta dirasiahkeun. Mangga taros heula ka Rina.",
     "(Sunda) \"Antosan heula, Bu...\" = \"Tunggu dulu, Bu. Pesan ini minta transfer cepat dan minta dirahasiakan. Tanya Rina dulu, ya.\""),
    ("A6", NARR, "Dengan satu ketukan, Ibu memanggil Rina. Rina menerima ringkasan risikonya, bukan isi chat, lalu menelepon Ibu. Jika Rina tidak menjawab dalam sepuluh menit, pendamping cadangan dihubungi.",
     "Satu ketukan memanggil Rina: ia menerima ringkasan risiko (bukan isi chat) dan menelepon Ibu. 10 menit tanpa respons, pendamping cadangan dihubungi."),
    ("A4", NARR, "Untuk hal yang lebih rumit, Ibu cukup menekan Tanya Dulu dan bercerita. JagaOrtu menjelaskan modusnya dan langkah yang aman, dengan bahasa sederhana.",
     "\"Tanya Dulu\": Ibu cukup bercerita; JagaOrtu menjelaskan modus dan langkah aman dengan bahasa sederhana."),
    ("A5", NARR, "Untuk telepon, JagaOrtu tidak merekam percakapan. Ia mengingatkan Ibu untuk menanyakan kata sandi keluarga, cara yang tetap ampuh walau suara dikloning AI.",
     "Telepon tidak direkam. JagaOrtu mengingatkan kata sandi keluarga: tetap ampuh walau suara dikloning AI."),
    ("A7", NARR, "Lewat Latihan Waspada, keluarga dapat mengirim simulasi penipuan yang aman, agar kewaspadaan Ibu terlatih sebelum penipu sungguhan datang.",
     "Latihan Waspada: simulasi penipuan yang aman agar kewaspadaan terlatih sebelum penipu sungguhan datang."),
    ("arch", NARR, "Bagaimana AI-nya bekerja? Kami memakai AI secukupnya.",
     "Bagaimana AI-nya bekerja? AI secukupnya."),
    ("arch", NARR, "Aturan pasti menyaring nomor, rekening, dan file berbahaya. Model kecil di perangkat menilai risiko secara offline. Model bahasa besar hanya dipanggil untuk kasus yang ambigu, dengan data yang sudah disamarkan.",
     "L0 aturan pasti  >  L1 model di perangkat (offline)  >  L2 LLM hanya untuk kasus ambigu, data disamarkan."),
    ("arch", NARR, "Keputusan akhir selalu di tangan manusia, yaitu Ibu dan keluarganya. Isi pesan tidak disimpan, sesuai Undang-Undang Pelindungan Data Pribadi.",
     "L3: keputusan di tangan manusia. Isi pesan tidak disimpan (UU No. 27/2022 PDP)."),
    ("biz", NARR, "Semua komponen memakai API Android resmi dan model yang sudah tersedia, sehingga MVP-nya dapat dibangun dalam dua puluh empat jam.",
     "Memakai API Android resmi dan model yang tersedia: MVP dapat dibangun dalam 24 jam."),
    ("biz", NARR, "Model bisnisnya B2B2C, dimulai dari bank dan BPR penyalur pensiun yang wajib menjalankan strategi anti-fraud sesuai POJK dua belas tahun dua ribu dua puluh empat. Biaya model bahasanya sekitar sembilan puluh rupiah per pengguna per bulan.",
     "B2B2C: bank & BPR penyalur pensiun (POJK 12/2024). Biaya LLM ±Rp90/pengguna/bulan (asumsi)."),
    ("biz", NARR, "Pilot tiga puluh keluarga di Bandung memakai desain daftar tunggu, dengan kriteria keberhasilan yang kami tetapkan sebelum data dikumpulkan. Satu penipuan fake call yang tercegah menghindari rata-rata tiga puluh tiga juta rupiah.",
     "Pilot 30 keluarga (desain daftar tunggu, kriteria ditetapkan sebelum data). 1 fake call tercegah = rata-rata Rp32,9 jt."),
    ("close", NARR, "Penipu menang ketika korbannya panik dan sendirian. JagaOrtu memastikan, tidak ada lansia yang harus menghadapi penipu sendirian.",
     "Tidak ada lansia yang harus menghadapi penipu sendirian."),
    ("close", NARR, "JagaOrtu. Sebelum transfer, tanya dulu.",
     "JagaOrtu. Sebelum transfer, tanya dulu."),
]

CSS = """
*{box-sizing:border-box} body{margin:0;width:1920px;height:1080px;font-family:'Segoe UI',Arial,sans-serif;overflow:hidden;background:#fff;color:#14213d}
.wrap{position:absolute;inset:0;padding:70px 90px 210px;display:flex;flex-direction:column;justify-content:center}
.cap{position:absolute;left:0;right:0;bottom:0;height:178px;background:rgba(18,30,52,.93);color:#fff;display:flex;align-items:center;
     justify-content:center;padding:0 120px;text-align:center;font-size:37px;line-height:1.3;font-weight:600}
.brand{position:absolute;top:30px;right:50px;font-weight:800;font-size:30px;color:#23395d}
.brand span{color:#ef6c00}
h1{font-size:74px;margin:0 0 20px;color:#23395d} h2{font-size:50px;margin:0 0 18px;color:#23395d}
.dark{background:#101826;color:#fff} .dark h1{color:#fff}
.grid4{display:grid;grid-template-columns:1fr 1fr;gap:34px}
.stat{border:4px solid #23395d;border-radius:28px;padding:30px 36px;background:#f4f7fc}
.stat .n{font-size:82px;font-weight:900;color:#ef6c00;line-height:1} .stat .t{font-size:32px;margin-top:10px;line-height:1.25}
.src{position:absolute;left:90px;bottom:190px;font-size:22px;color:#666}
.on{outline:8px solid #ef6c00}
.row{display:flex;gap:46px;align-items:center}
.pill{border:4px solid #23395d;border-radius:26px;padding:30px;font-size:40px;font-weight:800;text-align:center;flex:1;background:#f4f7fc}
.big{font-size:56px;font-weight:800;line-height:1.25}
"""


def scene_body(scene, idx, cfg):
    if scene == "hook":
        return """<div class='wrap dark' style='position:absolute;inset:0;background:#101826'>
<div style='display:flex;gap:80px;align-items:center'>
<div style='width:560px;border:6px solid #8aa0c0;border-radius:56px;padding:40px 34px;background:#1b2638'>
<div style='font-size:30px;color:#aab'>WhatsApp &middot; nomor baru</div>
<div style='margin-top:26px;background:#fff;color:#111;border-radius:26px 26px 26px 8px;padding:26px;font-size:34px;line-height:1.35'>Ma, ini Andi. HP-ku rusak, ini nomor baru. Tolong transfer 5 juta sekarang ya. Jangan bilang Papa dulu.</div></div>
<div><div style='font-size:150px;font-weight:900;color:#ef6c00;line-height:1'>3 detik</div>
<div style='font-size:46px;color:#fff;margin-top:16px;line-height:1.3'>rekaman cukup untuk tiruan suara<br>dengan kecocokan &plusmn;85%</div>
<div style='font-size:24px;color:#aab;margin-top:20px'>Sumber: McAfee, <i>The Artificial Imposter</i> (Mei 2023)</div></div></div></div>"""
    if scene == "team":
        names = "".join(f"<div style='font-size:40px;margin:10px 0'><b>{m['nama']}</b> &middot; {m['prodi']}, {m['kampus']}</div>" for m in cfg["anggota"])
        return f"""<div class='wrap'><div style='font-size:120px;font-weight:900;color:#23395d'>Jaga<span style='color:#ef6c00'>Ortu</span></div>
<div style='font-size:44px;margin:4px 0 40px'>Aturan Dua Orang Berbasis AI untuk Melindungi Lansia dari Penipuan Digital</div>
<div style='font-size:34px;color:#555;margin-bottom:14px'>Tim {cfg['nama_tim']} &middot; Hackvidia Arkavidia 11.0</div>{names}</div>"""
    if scene == "data":
        on = idx  # which stat to highlight
        cards = [("702.342", "laporan penipuan ke IASC OJK<br>(Nov 2024 - Sep 2026)"),
                 ("Rp2,09 T", "kerugian modus <i>fake call</i>,<br>terbesar di antara modus"),
                 ("54,55%", "literasi keuangan usia 51-79 th<br>(lansia online: 14% &rarr; 34%)"),
                 ("131.445", "laporan dari Jawa Barat,<br>provinsi tertinggi")]
        html = "".join(f"<div class='stat {'on' if i == on else ''}'><div class='n'>{n}</div><div class='t'>{t}</div></div>" for i, (n, t) in enumerate(cards))
        return f"""<div class='wrap'><h2>Masalahnya nyata dan membesar</h2><div class='grid4'>{html}</div>
<div class='src'>Sumber: IASC OJK via Kontan (Okt 2026) &amp; JPNN (Agu 2026); SNLIK 2025 OJK-BPS; BPS via GoodStats</div></div>"""
    if scene == "insight":
        return """<div class='wrap'><h2>Mengapa lansia tertipu?</h2>
<div class='row' style='margin-top:40px'><div class='pill'>Panik<br><span style='font-size:30px;font-weight:500'>"anak kecelakaan"</span></div>
<div class='pill'>Otoritas<br><span style='font-size:30px;font-weight:500'>"ini dari polisi/bank"</span></div>
<div class='pill'>Isolasi<br><span style='font-size:30px;font-weight:500'>"jangan bilang siapa-siapa"</span></div></div>
<div class='big' style='margin-top:70px;text-align:center'>Yang dibutuhkan: <span style='color:#ef6c00'>jeda</span> + <span style='color:#ef6c00'>orang kedua yang dipercaya</span></div></div>"""
    if scene == "concept":
        return """<div class='wrap'><h1>JagaOrtu = Aturan Dua Orang</h1>
<div class='row' style='margin-top:40px'>
<div class='pill' style='font-size:44px'>Lansia<br><span style='font-size:30px;font-weight:500'>menerima permintaan uang</span></div>
<div style='font-size:90px;color:#ef6c00;font-weight:900'>+</div>
<div class='pill' style='font-size:44px'>Pendamping<br><span style='font-size:30px;font-weight:500'>keluarga yang dipercaya</span></div>
<div style='font-size:90px;color:#ef6c00;font-weight:900'>=</div>
<div class='pill' style='font-size:44px;background:#e8f5e9;border-color:#2e7d32'>Keputusan aman<br><span style='font-size:30px;font-weight:500'>sebelum uang berpindah</span></div></div>
<div style='font-size:34px;margin-top:50px;color:#444;text-align:center'>Prinsip <i>maker-checker</i> perbankan, untuk keluarga</div></div>"""
    if scene in ("A1", "A3", "A4", "A5", "A6", "A7"):
        titles = {"A1": ("Pemasangan oleh anak", ["3 langkah, 5 menit", "Izin terbatas: hanya pesan berisiko", "Pendamping utama + cadangan", "Kata sandi keluarga & bahasa suara"]),
                  "A3": ("Peringatan otomatis", ["Muncul sebelum uang berpindah", "Dibacakan dalam bahasa Ibu (Sunda/Jawa/Indonesia)", "Tanda bahaya konkret, bukan vonis", "Aksi utama: tanya orang kedua"]),
                  "A6": ("Aplikasi Pendamping", ["Ringkasan risiko, bukan isi chat", "Satu ketuk: telepon Ibu", "Eskalasi otomatis 10 menit"]),
                  "A4": ("Tanya Dulu", ["Cukup bercerita lewat suara", "Penjelasan modus + langkah aman", "Tanpa istilah teknis"]),
                  "A5": ("Telepon masuk", ["Tidak merekam percakapan", "Pengingat kata sandi keluarga", "Ampuh melawan kloning suara"]),
                  "A7": ("Latihan Waspada", ["Simulasi aman atas izin keluarga", "Pelajaran suara 30 detik", "Kemajuan terlihat keluarga"])}
        t, pts = titles[scene]
        lis = "".join(f"<li style='margin:14px 0'>{p}</li>" for p in pts)
        return f"""<div class='wrap' style='flex-direction:row;gap:90px;align-items:center;justify-content:flex-start;padding-top:40px'>
<img src='{WF}/{scene}.png' style='height:780px;border-radius:24px'>
<div><div style='font-size:30px;color:#ef6c00;font-weight:800'>WIREFRAME {scene}</div><h1 style='font-size:68px'>{t}</h1>
<ul style='font-size:42px;line-height:1.3;padding-left:40px'>{lis}</ul></div></div>"""
    if scene == "arch":
        return f"""<div class='wrap' style='padding-top:40px;align-items:center'><img src='{(BUILD / 'arch.png').resolve().as_uri()}' style='width:1740px'></div>"""
    if scene == "biz":
        return """<div class='wrap'><h2>Layak dibangun, layak dibiayai, berdampak</h2><div class='grid4'>
<div class='stat'><div class='n' style='font-size:64px'>MVP 24 jam</div><div class='t'>API Android resmi + model yang sudah tersedia</div></div>
<div class='stat'><div class='n' style='font-size:64px'>B2B2C</div><div class='t'>bank &amp; BPR penyalur pensiun (POJK 12/2024); LLM &plusmn;Rp90/pengguna/bulan (asumsi)</div></div>
<div class='stat'><div class='n' style='font-size:64px'>Pilot Bandung</div><div class='t'>30 keluarga (Feb-Apr 2027), lalu komunitas lansia</div></div>
<div class='stat'><div class='n' style='font-size:64px'>Rp32,9 jt</div><div class='t'>rata-rata kerugian per laporan <i>fake call</i> (IASC, Nov 2024-Jun 2026; perhitungan tim)</div></div></div></div>"""
    if scene == "close":
        return """<div class='wrap dark' style='position:absolute;inset:0;background:#101826;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center'>
<div style='font-size:130px;font-weight:900;color:#fff'>Jaga<span style='color:#ef6c00'>Ortu</span></div>
<div style='font-size:58px;color:#fff;margin-top:20px'>Sebelum transfer, tanya dulu.</div>
<div style='font-size:36px;color:#aab;margin-top:40px'>Tidak ada lansia yang harus menghadapi penipu sendirian.</div></div>"""
    raise ValueError(scene)


def slide_html(i, seg, cfg):
    scene, voice, say, show = seg
    data_idx = {3: 0, 4: 1, 5: 2, 6: 3}.get(i, -1)
    body = scene_body(scene, data_idx, cfg)
    brand = "" if scene in ("hook", "close") else "<div class='brand'>Jaga<span>Ortu</span></div>"
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}{brand}<div class='cap'>{show}</div></body></html>"


async def tts(segs, outdir):
    import edge_tts
    for i, (scene, voice, say, show) in enumerate(segs):
        out = outdir / f"seg{i:02d}.mp3"
        custom = outdir / "custom" / f"seg{i:02d}.mp3"
        if custom.exists():
            out.write_bytes(custom.read_bytes()); continue
        rate = "+12%" if voice == ANDI else "+10%"
        key = voice + rate + say
        if out.exists() and out.with_suffix(".txt").exists() and out.with_suffix(".txt").read_text(encoding="utf-8") == key:
            continue
        rate = "+12%" if voice == ANDI else "+10%"
        await edge_tts.Communicate(say, voice, rate=rate).save(str(out))
        out.with_suffix(".txt").write_text(key, encoding="utf-8")


def dur(path):
    if not FFPROBE:
        # Tanpa ffprobe (mis. ffmpeg dari imageio-ffmpeg): baca "Duration: hh:mm:ss.xx" dari stderr ffmpeg -i.
        r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
        h, m, s = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", r.stderr).groups()
        return int(h) * 3600 + int(m) * 60 + float(s)
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)],
                       capture_output=True, text=True)
    return float(json.loads(r.stdout)["format"]["duration"])


def srt_time(t):
    h, rem = divmod(t, 3600); m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def mmss(t):
    """Detik -> 'm:ss (m menit s detik)'. Bulatkan ke detik dulu, baru dipecah (bug lama: t/60 dibulatkan -> 4,6 jadi '5 menit')."""
    m, s = divmod(int(round(t)), 60)
    return f"{m}:{s:02d} ({m} menit {s} detik)"


def main():
    if not FFMPEG:
        raise SystemExit("ffmpeg/ffprobe tidak ditemukan. Pasang ffmpeg dan masukkan ke PATH, atau set env FFMPEG_DIR "
                         "ke folder bin ffmpeg. Lihat README.md bagian 'Cara build'.")
    cfg = load_config()
    audio = BUILD / "audio"; audio.mkdir(exist_ok=True); (audio / "custom").mkdir(exist_ok=True)
    slides = BUILD / "slides"; slides.mkdir(exist_ok=True)
    asyncio.run(tts(SEG, audio))
    jobs = []
    for i, seg in enumerate(SEG):
        h = write(slides / f"s{i:02d}.html", slide_html(i, seg, cfg))
        jobs.append({"type": "png", "html": h, "out": slides / f"s{i:02d}.png", "width": 1920, "height": 1080, "scale": 1, "full_page": False, "wait": 500})
    render(jobs)
    parts, t, srt = [], 0.0, []
    PAD = 0.35
    for i, seg in enumerate(SEG):
        a = audio / f"seg{i:02d}.mp3"
        d = dur(a) + PAD
        part = slides / f"p{i:02d}.mp4"
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", str(slides / f"s{i:02d}.png"), "-i", str(a),
                        "-af", f"apad=pad_dur={PAD}", "-t", f"{d:.3f}", "-r", "30", "-c:v", "libx264", "-tune", "stillimage",
                        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", str(part)], check=True)
        parts.append(part)
        srt.append(f"{i + 1}\n{srt_time(t)} --> {srt_time(t + d - 0.1)}\n{seg[3]}\n")
        t += d
    lst = slides / "list.txt"
    # Path relatif: ffmpeg concat membaca path relatif terhadap lokasi list.txt, jadi portabel antar-komputer.
    lst.write_text("".join(f"file '{p.name}'\n" for p in parts), encoding="utf-8")
    out_dir = ROOT / "04_Video"
    mp4 = out_dir / f"{cfg['nama_tim']}_Video_Hackvidia.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(mp4)], check=True)
    (out_dir / f"{cfg['nama_tim']}_Video_Hackvidia.srt").write_text("\n".join(srt), encoding="utf-8")
    naskah = ["# Naskah Video Hackvidia - " + cfg["nama_tim"], "",
              f"Judul YouTube (unlisted): {cfg['nama_tim']} - {cfg['nama_solusi']} - Hackvidia 11.0", f"Durasi: {mmss(t)}", "",
              "| # | Adegan | Suara | Narasi |", "|---|---|---|---|"]
    for i, (scene, voice, say, show) in enumerate(SEG):
        naskah.append(f"| {i:02d} | {scene} | {voice.split('-')[2].replace('Neural', '')} | {say} |")
    (out_dir / "Naskah_Video.md").write_text("\n".join(naskah) + "\n", encoding="utf-8")
    print(f"video ok -> {mp4}  durasi {t:.1f} detik")


if __name__ == "__main__":
    main()
