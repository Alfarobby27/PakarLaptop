from typing import List, Dict, Any

# ============================
# DATA KERUSAKAN
# ============================

FAULTS = {
    "K1": {"name": "Kerusakan kabel fleksibel LCD", "solution": "Memeriksa dan membersihkan kabel fleksibel LCD yang terhubung ke panel LCD dan mainboard. Apabila kondisi tidak berubah, dilakukan penggantian kabel fleksibel LCD."},
    "K2": {"name": "Kerusakan prosesor", "solution": "Melepas prosesor dari soket, membersihkan bagian prosesor dan soketnya, kemudian memasang kembali. Jika laptop tetap tidak menyala, kemungkinan terjadi kerusakan pada mainboard."},
    "K3": {"name": "Kerusakan modul RAM", "solution": "Membersihkan modul RAM dan soket RAM, kemudian melakukan pengujian ulang. Jika diperlukan, dilakukan pengujian dengan monitor eksternal."},
    "K4": {"name": "Kerusakan DVD RW/Combo", "solution": "Melepas perangkat DVD RW/Combo dan membersihkan bagian konektor. Apabila perangkat tidak dapat membaca atau menulis data, dilakukan penggantian DVD RW/Combo."},
    "K5": {"name": "Kerusakan keyboard", "solution": "Membersihkan bagian keyboard yang bermasalah serta memeriksa kabel dan soket keyboard yang terhubung ke mainboard."},
    "K6": {"name": "Gangguan driver VGA atau komponen grafis", "solution": "Melakukan instalasi ulang atau pembaruan (update) driver VGA. Jika tampilan masih tidak normal, dilakukan pemeriksaan pada kabel LCD, komponen VGA, atau mainboard."},
    "K7": {"name": "Kerusakan power switch", "solution": "Memeriksa dan membersihkan komponen power switch. Jika laptop tetap tidak dapat menyala, kemungkinan terdapat gangguan pada rangkaian daya di mainboard."},
    "K8": {"name": "Kerusakan motherboard", "solution": "Apabila setelah dilakukan pemeriksaan komponen lain laptop tetap tidak berfungsi, maka disimpulkan terjadi kerusakan pada motherboard dan disarankan dilakukan pemeriksaan lanjutan oleh teknisi."}
}

# ============================
# DATA GEJALA
# ============================

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

# ============================
# RULE BASE (NETRAL)
# ============================

RULES = {
    "K1": ["G1", "G2", "G3", "G6"],
    "K2": ["G4"],
    "K3": ["G5"],
    "K4": ["G7", "G8"],
    "K5": ["G9"],
    "K6": ["G10"],
    "K7": ["G11"]
}

# ============================
# FORWARD CHAINING
# mode = "AND" | "OR"
# ============================

def forward_chaining(
    selected_symptoms: List[str],
    mode: str = "AND"
) -> Dict[str, Any]:

    selected_symptoms = list(dict.fromkeys(selected_symptoms))
    facts = set(selected_symptoms)
    log = []
    step = 1
    used_rules = set()

    while True:
        rule_applied = False

        for conclusion, conditions in RULES.items():
            if conclusion in used_rules:
                continue

            # Evaluasi aturan
            if mode == "AND":
                satisfied = all(c in facts for c in conditions)
            else:  # OR
                satisfied = any(c in facts for c in conditions)

            facts_before = sorted(facts)

            if satisfied:
                facts.add(conclusion)
                used_rules.add(conclusion)
                rule_applied = True

                log.append({
                    "step": step,
                    "rule": conclusion,
                    "status": True,
                    "operator": mode,
                    "if_condition": conditions,
                    "then_code": conclusion,
                    "then_name": FAULTS[conclusion]["name"],
                    "facts_before": facts_before,
                    "facts_after": sorted(facts)
                })

                step += 1
                break
            else:
                log.append({
                    "step": step,
                    "rule": conclusion,
                    "status": False,
                    "operator": mode,
                    "if_condition": conditions,
                    "then_code": conclusion,
                    "then_name": FAULTS[conclusion]["name"],
                    "facts_before": facts_before,
                    "facts_after": facts_before
                })
                step += 1

        if not rule_applied:
            break

    # ============================
    # KESIMPULAN
    # ============================

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
        "facts_initial": selected_symptoms,
        "log": log,
        "final_faults": final_faults
    }
