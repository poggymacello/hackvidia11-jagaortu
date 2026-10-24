"""Bangun ulang semua berkas dari config_tim.json.

Pemakaian (dari folder ini, sebaiknya di dalam .venv — lihat README.md bagian "Cara build"):
    python build_all.py                      # semua langkah; video dilewati otomatis bila ffmpeg tidak ada
    python build_all.py --only proposal surat
    python build_all.py --skip video

Tidak ada path yang di-hardcode: ffmpeg dicari lewat env FFMPEG_DIR / FFMPEG_PATH, lalu PATH, lalu lokasi umum
WinGet/Chocolatey/Scoop (lihat build/common.py:find_tool).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
B = ROOT / "build"
sys.path.insert(0, str(B))
from common import find_tool  # noqa: E402

STEPS = ["wireframes", "diagram", "journey", "leancanvas", "proposal", "surat", "video"]

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--only", nargs="*", choices=STEPS, help="hanya jalankan langkah ini")
ap.add_argument("--skip", nargs="*", choices=STEPS, default=[], help="lewati langkah ini")
ap.add_argument("--draft", action="store_true", help="tetap bangun walau config masih berisi [ISI: ...] (untuk pratinjau)")
args = ap.parse_args()
steps = [s for s in (args.only or STEPS) if s not in args.skip]

def _strip_notes(o):  # abaikan kunci petunjuk ("_petunjuk") saat mencari isian kosong
    if isinstance(o, dict):
        return {k: _strip_notes(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [_strip_notes(v) for v in o]
    return o


cfg_text = json.dumps(_strip_notes(json.loads((ROOT / "config_tim.json").read_text(encoding="utf-8"))), ensure_ascii=False)
holes = sorted(set(re.findall(r"\[ISI:[^\]]*\]", cfg_text)))
if holes:
    print(f"!! config_tim.json masih berisi {cfg_text.count('[ISI:')} isian kosong, mis.: {', '.join(holes[:4])}")
    if not args.draft:
        sys.exit("   Isi dulu (lihat ISI_DATA_TIM.md), atau jalankan dengan --draft untuk pratinjau.")
    print("   --draft: tetap dibangun. JANGAN kirim berkas ini ke panitia.")

env = dict(os.environ)
ff = find_tool("ffmpeg")
if ff:
    env["PATH"] = str(Path(ff).parent) + os.pathsep + env.get("PATH", "")
elif "video" in steps:
    print("!! ffmpeg/ffprobe tidak ditemukan -> langkah video DILEWATI. Pasang ffmpeg atau set FFMPEG_DIR, lalu jalankan:"
          "\n   python build_all.py --only video")
    steps.remove("video")

for step in steps:
    print(">>", step)
    subprocess.run([sys.executable, f"{step}.py"], cwd=B, env=env, check=True)
print("Selesai:", ", ".join(steps))
