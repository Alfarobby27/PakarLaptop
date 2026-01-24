from typing import List, Dict, Any

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

def forward_chaining(selected_symptoms: List[str], mode: str = "AND") -> Dict[str, Any]:
    mode = mode.upper()
    if mode not in ("AND", "OR"):
        mode = "AND"

    selected_symptoms = list(dict.fromkeys(selected_symptoms))
    facts = set(selected_symptoms)
    log = []
    step = 1
    used_rules = set()

    while True:
        new_facts = set()  # Fakta baru yang muncul di iterasi ini

        for conclusion in sorted(RULES.keys()):
            if conclusion in used_rules:
                continue

            conditions = RULES[conclusion]
            facts_before = sorted(facts)

            if mode == "AND":
                satisfied = all(c in facts for c in conditions)
            else:  # OR
                satisfied = any(c in facts for c in conditions)

            if satisfied:
                if conclusion not in facts:
                    new_facts.add(conclusion)  # Tambahkan ke new_facts

                used_rules.add(conclusion)
                log.append({
                    "step": step,
                    "rule": conclusion,
                    "status": True,
                    "operator": mode,
                    "if_condition": conditions,
                    "then_code": conclusion,
                    "then_name": FAULTS[conclusion]["name"],
                    "facts_before": facts_before,
                    "facts_after": sorted(facts | new_facts),
                    "new_fact_added": conclusion not in facts
                })
                step += 1
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
                    "facts_after": facts_before,
                    "new_fact_added": False
                })
                step += 1

        if not new_facts:  # Tidak ada fakta baru di iterasi ini → berhenti
            break

        facts |= new_facts  # Tambahkan semua fakta baru ke facts

    final_faults = [
        {"code": f, "name": FAULTS[f]["name"], "solution": FAULTS[f]["solution"]}
        for f in facts if f in FAULTS
    ]

    return {
        "mode": mode,
        "facts_initial": selected_symptoms,
        "log": log,
        "final_faults": final_faults
    }
