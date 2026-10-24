"""Olah hasil riset pengguna (CSV) -> angka validasi + paragraf proposal.

Pemakaian (dari folder proyek):
    .venv\\Scripts\\python 06_Riset_Pengguna\\olah_hasil.py            # hanya tampilkan angka & paragraf
    .venv\\Scripts\\python 06_Riset_Pengguna\\olah_hasil.py --tulis    # + tulis ke config_tim.json -> validasi
    .venv\\Scripts\\python 06_Riset_Pengguna\\olah_hasil.py --data 06_Riset_Pengguna\\contoh_FIKTIF   # uji skrip

Masukan (folder --data, default 06_Riset_Pengguna/data):
    survei.csv        unduhan Google Form (kolom dikenali dari awalan "Q01.", "Q02.", ...)
    wawancara.csv     satu baris per lansia (lihat C_SKRIP_WAWANCARA_DAN_UJI_WIREFRAME.md)
    uji_wireframe.csv satu baris per lansia yang ikut uji wireframe
File yang kosong (hanya header) dilewati; nilai di config untuk bagian itu dibiarkan null.
Skrip ini tidak pernah mengarang angka: semua angka dihitung dari baris CSV.
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
YA = {"ya", "y", "yes", "1", "true", "berhasil"}


def read_rows(path):
    if not path.exists():
        return [], []
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f)]
    rows = [r for r in rows if any((v or "").strip() for v in r.values())]
    return rows, (list(rows[0].keys()) if rows else [])


def col(header, prefix):
    for h in header:
        if h and h.strip().upper().startswith(prefix.upper()):
            return h
    raise SystemExit(f"Kolom berawalan '{prefix}' tidak ditemukan di survei.csv. Pastikan judul pertanyaan di Google Form diawali '{prefix}.'")


def is_ya(v):
    return (v or "").strip().lower() in YA


def pct(a, n):
    return round(100 * a / n) if n else None


def survei(rows, header):
    if not rows:
        return {}, []
    q02, q05, q07, q08, q10 = (col(header, p) for p in ("Q02", "Q05", "Q07", "Q08", "Q10"))
    elig = [r for r in rows if is_ya(r[q02])]
    n = len(elig)
    if not n:
        return {}, ["survei: tidak ada responden dengan Q02 = Ya"]
    def score(v):
        m = re.match(r"\s*(\d)", v or "")
        return int(m.group(1)) if m else None
    out = {
        "survei_n": n,
        "survei_pct_ortu_pernah_jadi_target": pct(sum(is_ya(r[q05]) for r in elig), n),
        "survei_pct_khawatir": pct(sum((score(r[q08]) or 0) >= 4 for r in elig), n),
        "survei_pct_mau_jadi_pendamping": pct(sum(is_ya(r[q10]) for r in elig), n),
    }
    try:  # Q13 kesediaan bayar: "Rp15.000–30.000" atau "Lebih dari Rp30.000" = mau membayar >= Rp15.000
        q13 = col(header, "Q13")
        out["survei_pct_bayar_min15rb"] = pct(sum((r[q13] or "").strip().lower().startswith(("rp15", "lebih"))
                                                  for r in elig), n)
    except SystemExit:
        pass
    notes = [f"survei: {len(rows)} respons total, {n} lolos Q02 (punya orang tua/mertua 60+)"]
    if n < 30:
        notes.append(f"PERINGATAN: survei_n = {n} (< 30 yang direncanakan). Angka tetap ditulis apa adanya; sebut jujur di proposal/pitch.")
    notes.append(f"  Q07 pernah rugi uang/data: {pct(sum(is_ya(r[q07]) for r in elig), n)}%")
    for p, label in (("Q06", "modus"), ("Q11", "fitur terpenting"), ("Q12", "kekhawatiran"), ("Q13", "kesediaan bayar")):
        try:
            c = col(header, p)
        except SystemExit:
            continue
        cnt = Counter()
        for r in elig:
            for part in (r[c] or "").split(", ") if p != "Q13" else [r[c]]:  # opsi tidak boleh berisi koma
                if part.strip():
                    cnt[part.strip()] += 1
        top = "; ".join(f"{k} ({v}/{n})" for k, v in cnt.most_common(4))
        notes.append(f"  {p} {label}: {top or '-'}")
    return out, notes


def wawancara(rows):
    rows = [r for r in rows if (r.get("kode") or "").strip()]
    n = len(rows)
    if not n:
        return {}, []
    def count(k):
        return sum(is_ya(r.get(k)) for r in rows)
    items = [
        (count("pernah_target"), "pernah menjadi sasaran pesan atau telepon penipuan"),
        (count("reaksi_panik"), "menggambarkan rasa panik atau terburu-buru saat itu"),
        (count("sungkan_bertanya"), "sungkan atau bingung harus bertanya ke siapa"),
        (count("pilih_suara"), "lebih memilih penjelasan lewat suara daripada tulisan"),
    ]
    parts = [f"{a} dari {n} {t}" for a, t in items if a > 0]  # hanya temuan yang benar-benar muncul
    temuan = (", ".join(parts[:-1]) + (", dan " if len(parts) > 1 else "") + parts[-1]) if parts else None
    out = {"wawancara_lansia_n": n, "wawancara_temuan": temuan}
    quotes = [r for r in rows if is_ya(r.get("kutipan_utama")) and is_ya(r.get("boleh_dikutip")) and (r.get("kutipan") or "").strip()]
    notes = [f"wawancara: {n} lansia; setuju anak diberi tahu: {count('setuju_anak_diberitahu')}/{n}"]
    if len(quotes) > 1:
        notes.append("PERINGATAN: lebih dari satu baris kutipan_utama=Ya; dipakai yang pertama.")
    if quotes:
        out["kutipan_lansia"] = quotes[0]["kutipan"].strip().strip('"')
    else:
        cand = [r["kutipan"] for r in rows if is_ya(r.get("boleh_dikutip")) and (r.get("kutipan") or "").strip()]
        notes.append("  (belum ada kutipan_utama=Ya; kandidat: " + (" | ".join(cand[:3]) or "-") + ")")
    bahasa = Counter((r.get("bahasa_pilihan") or "-").strip() for r in rows)
    notes.append("  bahasa pilihan: " + ", ".join(f"{k} {v}" for k, v in bahasa.most_common()))
    return out, notes


def uji(rows):
    rows = [r for r in rows if (r.get("kode") or "").strip()]
    n = len(rows)
    if not n:
        return {}, []
    paham = sum(is_ya(r.get("T1_tindakan_aman")) and is_ya(r.get("T2_teach_back")) for r in rows)
    notes = [f"uji wireframe: {n} lansia, {paham} berhasil T1+T2"]
    for k in ("T3_telepon", "T4_privasi"):
        notes.append(f"  {k}: {sum(is_ya(r.get(k)) for r in rows)}/{n}")
    for k in ("skor_mudah_dibaca", "skor_suara_membantu", "skor_merasa_dihargai"):
        vals = [int(r[k]) for r in rows if (r.get(k) or "").strip().isdigit()]
        if vals:
            notes.append(f"  {k}: rata-rata {sum(vals) / len(vals):.1f} dari 3")
    usul = [r["usulan_perubahan"] for r in rows if (r.get("usulan_perubahan") or "").strip()]
    if usul:
        notes.append("  usulan perubahan: " + " | ".join(usul))
    return {"uji_wireframe_n": n, "uji_wireframe_pct_paham": pct(paham, n)}, notes


def paragraph(v):
    sys.path.insert(0, str(ROOT / "build"))
    try:
        from proposal import validation_paragraph
        return validation_paragraph(v)
    except Exception as e:  # python-docx belum terpasang dsb.
        return f"(tidak bisa memuat build/proposal.py: {e})"


def write_config(new):
    path = ROOT / "config_tim.json"
    text = path.read_text(encoding="utf-8")
    cfg = json.loads(text)
    if list(cfg.keys())[-1] != "validasi":
        raise SystemExit("config_tim.json: 'validasi' harus menjadi kunci terakhir.")
    v = cfg["validasi"]
    v.update(new)
    i = text.index('"validasi"')
    block = json.dumps(v, ensure_ascii=False, indent=2).replace("\n", "\n  ")
    path.write_text(text[:i] + '"validasi": ' + block + "\n}\n", encoding="utf-8")
    json.loads(path.read_text(encoding="utf-8"))  # validasi ulang


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(HERE / "data"))
    ap.add_argument("--tulis", action="store_true", help="tulis hasil ke config_tim.json -> validasi")
    a = ap.parse_args()
    d = Path(a.data)
    s_rows, s_head = read_rows(d / "survei.csv")
    new, notes = {}, []
    for res in (survei(s_rows, s_head), wawancara(read_rows(d / "wawancara.csv")[0]), uji(read_rows(d / "uji_wireframe.csv")[0])):
        new.update({k: v for k, v in res[0].items() if v is not None})
        notes += res[1]
    if not new:
        print("Belum ada data di", d, "(CSV masih kosong). Config tidak diubah.")
        return
    print("== Ringkasan ==")
    print("\n".join(notes))
    print("\n== Nilai untuk config_tim.json -> validasi ==")
    print(json.dumps(new, ensure_ascii=False, indent=2))
    cfg_v = json.loads((ROOT / "config_tim.json").read_text(encoding="utf-8"))["validasi"]
    merged = {**cfg_v, **new}
    print("\n== Paragraf yang akan muncul di proposal (bagian 2.4) ==")
    print(paragraph(merged))
    if a.tulis:
        if "FIKTIF" in d.name.upper():
            raise SystemExit("\nDitolak: data contoh FIKTIF tidak boleh ditulis ke config.")
        write_config(new)
        print("\nconfig_tim.json diperbarui. Lanjutkan: .venv\\Scripts\\python build_all.py --only proposal  (cek tetap <= 10 halaman teks)")
    else:
        print("\n(Belum ditulis. Tambahkan --tulis untuk menyimpan ke config_tim.json.)")


if __name__ == "__main__":
    main()
