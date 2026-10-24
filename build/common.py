"""Shared helpers: config loading, tool discovery, and HTML -> PNG/PDF rendering via Playwright.

Browser: memakai browser yang sudah terpasang (Edge atau Chrome) lewat Playwright "channel", sehingga tidak perlu
mengunduh Chromium. Urutan: env JAGAORTU_BROWSER (mis. "chrome" / "msedge" / "chromium") -> msedge -> chrome ->
chromium bawaan Playwright (perlu `python -m playwright install chromium`).
"""
import asyncio
import glob
import json
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"


def load_config():
    return json.loads((ROOT / "config_tim.json").read_text(encoding="utf-8"))


def find_tool(name):
    """Cari executable (mis. ffmpeg/ffprobe) tanpa path hardcode.

    Urutan: env <NAME>_PATH (path lengkap ke exe) -> env FFMPEG_DIR (folder bin) -> PATH (shutil.which)
    -> lokasi umum WinGet/Chocolatey/Scoop di Windows. Mengembalikan string path atau None.
    """
    exe = name + (".exe" if os.name == "nt" else "")
    direct = os.environ.get(f"{name.upper()}_PATH")
    if direct and Path(direct).is_file():
        return direct
    d = os.environ.get("FFMPEG_DIR")
    if d and (Path(d) / exe).is_file():
        return str(Path(d) / exe)
    hit = shutil.which(name)
    if hit:
        return hit
    if os.name == "nt":
        pats = []
        la = os.environ.get("LOCALAPPDATA")
        if la:
            pats.append(os.path.join(la, "Microsoft", "WinGet", "Packages", "*FFmpeg*", "**", "bin", exe))
            pats.append(os.path.join(la, "Microsoft", "WinGet", "Links", exe))
        pats += [os.path.join(os.environ.get("ProgramData", r"C:\ProgramData"), "chocolatey", "bin", exe),
                 os.path.join(os.path.expanduser("~"), "scoop", "shims", exe),
                 os.path.join(r"C:\ffmpeg", "bin", exe)]
        for pat in pats:
            found = sorted(glob.glob(pat, recursive=True))
            if found:
                return found[-1]
    if name == "ffmpeg":
        # Cadangan: binary ffmpeg dari paket pip imageio-ffmpeg (tanpa ffprobe; durasi lewat video.dur()).
        try:
            import imageio_ffmpeg
            return imageio_ffmpeg.get_ffmpeg_exe()
        except Exception:
            pass
    return None


async def _launch(p):
    order = [os.environ["JAGAORTU_BROWSER"]] if os.environ.get("JAGAORTU_BROWSER") else ["msedge", "chrome", "chromium"]
    last = None
    for ch in order:
        try:
            if ch == "chromium":
                return await p.chromium.launch()
            return await p.chromium.launch(channel=ch)
        except Exception as e:  # browser/channel tidak tersedia -> coba berikutnya
            last = e
    raise RuntimeError("Tidak ada browser untuk render HTML. Pasang Edge/Chrome atau jalankan "
                       "`python -m playwright install chromium`.") from last


async def _render(jobs):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await _launch(p)
        for job in jobs:
            page = await browser.new_page(
                viewport={"width": job.get("width", 1280), "height": job.get("height", 800)},
                device_scale_factor=job.get("scale", 2),
            )
            html_path = job["html"]
            await page.goto(Path(html_path).resolve().as_uri())
            await page.wait_for_timeout(job.get("wait", 300))
            if job["type"] == "png":
                if job.get("selector"):
                    await page.locator(job["selector"]).screenshot(path=str(job["out"]))
                else:
                    await page.screenshot(path=str(job["out"]), full_page=job.get("full_page", True))
            elif job["type"] == "pdf":
                await page.pdf(path=str(job["out"]), print_background=True,
                               prefer_css_page_size=True)
            await page.close()
        await browser.close()


def render(jobs):
    asyncio.run(_render(jobs))


def docx_to_pdf(docx_path, pdf_path):
    """DOCX -> PDF. Coba Microsoft Word (docx2pdf, Windows/macOS), lalu LibreOffice (soffice) bila ada.

    Mengembalikan True bila PDF berhasil dibuat; False (dengan pesan) bila tidak ada konverter.
    """
    docx_path, pdf_path = Path(docx_path), Path(pdf_path)
    try:
        from docx2pdf import convert
        convert(str(docx_path), str(pdf_path))
        if pdf_path.exists():
            return True
    except Exception as e:  # Word tidak terpasang / COM gagal
        print("  docx2pdf (MS Word) gagal:", e)
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice and os.name == "nt":
        for c in (r"C:\Program Files\LibreOffice\program\soffice.exe", r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"):
            if Path(c).is_file():
                soffice = c
    if soffice:
        import subprocess
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(pdf_path.parent), str(docx_path)], check=True)
        produced = pdf_path.parent / (docx_path.stem + ".pdf")
        if produced != pdf_path and produced.exists():
            produced.replace(pdf_path)
        return pdf_path.exists()
    print("  PERINGATAN: tidak ada MS Word maupun LibreOffice; hanya DOCX yang dibuat:", docx_path)
    return False


def write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path
