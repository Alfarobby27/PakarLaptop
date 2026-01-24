from typing import List, Dict, Any

# ================= DATA =================

FAULTS = {
    "K1": {"name": "Kerusakan kabel fleksibel LCD", "solution": "Memeriksa dan membersihkan kabel fleksibel LCD yang terhubung ke panel LCD dan mainboard. Jika kondisi tidak berubah, dilakukan penggantian kabel fleksibel LCD."},
    "K2": {"name": "Kerusakan prosesor", "solution": "Melepas prosesor dari soket, membersihkan bagian prosesor dan soketnya, kemudian memasang kembali. Jika laptop tetap tidak menyala, kemungkinan terjadi kerusakan pada mainboard."},
    "K3": {"name": "Kerusakan modul RAM", "solution": "Membersihkan modul RAM dan soket RAM, kemudian melakukan pengujian ulang. Jika diperlukan, dilakukan pengujian dengan monitor eksternal."},
    "K4": {"name": "Kerusakan DVD RW/Combo", "solution": "Melepas perangkat DVD RW/Combo dan membersihkan bagian konektor. Jika perangkat tidak dapat membaca/menulis CD/DVD, dilakukan penggantian."},
    "K5": {"name": "Kerusakan keyboard", "solution": "Membersihkan bagian keyboard yang bermasalah serta memeriksa kabel/soket keyboard yang terhubung ke mainboard."},
    "K6": {"name": "Gangguan driver VGA atau komponen grafis", "solution": "Melakukan instalasi ulang/pembaruan driver VGA. Jika tampilan masih tidak normal, periksa kabel LCD, komponen VGA, atau mainboard."},
    "K7": {"name": "Kerusakan power switch", "solution": "Memeriksa dan membersihkan komponen power switch. Jika laptop tetap tidak dapat menyala, kemungkinan terdapat gangguan pada rangkaian daya di mainboard."},
    "K8": {"name": "Kerusakan motherboard", "solution": "Jika setelah pemeriksaan komponen lain laptop tetap tidak berfungsi, disimpulkan kerusakan motherboard dan disarankan diperiksa teknisi."}
}

SYMPTOMS = {
    "G1": "Layar laptop menampilkan warna putih",
    "G2": "Tampilan gambar bergetar",
    "G3": "Layar berkedip",
    "G4": "Lampu indikator menyala lalu mati kembali",
    "G5": "Lampu indikator menyala tetapi layar tidak menampilkan gambar",
    "G6": "LCD kadang menyala dan kadang mati",
    "G7": "DVD RW/Combo tidak terdeteksi",
    "G8": "DVD RW/Combo tidak dapat membaca atau menulis CD/DVD",
    "G9": "Keyboard tidak berfungsi",
    "G10": "Tampilan gambar tidak normal atau muncul garis",
    "G11": "Laptop sulit dinyalakan"
}

RULES = {
    "K1": ["G1", "G2", "G3", "G6"],
    "K2": ["G4"],
    "K3": ["G5"],
    "K4": ["G7", "G8"],
    "K5": ["G9"],
    "K6": ["G10"],
    "K7": ["G11"]
}

# ================= FORWARD CHAINING =================

def forward_chaining(selected_symptoms: List[str], mode: str = "AND") -> Dict[str, Any]:
    mode = mode.upper()
    if mode not in ("AND", "OR"):
        mode = "AND"

    # Hilangkan duplikasi gejala
    facts = set(dict.fromkeys(selected_symptoms))
    log = []
    used_rules = set()

    step = 1
    inference_finished_at = 0

    while True:
        new_fact_added = False

        for conclusion in sorted(RULES.keys()):
            if conclusion in used_rules:
                continue

            conditions = RULES[conclusion]
            facts_before = sorted(facts)

            # Evaluasi rule
            if mode == "AND":
                satisfied = all(c in facts for c in conditions)
            else:
                satisfied = any(c in facts for c in conditions)

            if satisfied:
                used_rules.add(conclusion)

                if conclusion not in facts:
                    facts.add(conclusion)
                    new_fact_added = True
                    inference_finished_at = step

                log.append({
                    "step": step,
                    "rule": conclusion,
                    "status": True,
                    "operator": mode,
                    "if_condition": conditions,
                    "then_code": conclusion,
                    "then_name": FAULTS[conclusion]["name"],
                    "facts_before": facts_before,
                    "facts_after": sorted(facts),
                    "new_fact_added": conclusion not in facts_before
                })

                step += 1

        # 🔴 TIDAK ADA FAKTA BARU → STOP INFERENSI
        if not new_fact_added:
            break

    # Ambil kesimpulan akhir
    final_faults = [
        {
            "code": f,
            "name": FAULTS[f]["name"],
            "solution": FAULTS[f]["solution"]
        }
        for f in facts if f in FAULTS
    ]

    return {
        "mode": mode,
        "facts_initial": sorted(selected_symptoms),
        "log": log,
        "final_faults": final_faults,
        "inference_finished_at": inference_finished_at
    }
