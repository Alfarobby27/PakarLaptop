from typing import List, Dict, Any

# ================= DATA =================

FAULTS = {
    "K1": {
        "name": "Kerusakan kabel fleksibel LCD",
        "solution": "Memeriksa dan membersihkan kabel fleksibel LCD yang terhubung ke panel LCD dan mainboard. Jika kondisi tidak berubah, dilakukan penggantian kabel fleksibel LCD."
    },
    "K2": {
        "name": "Kerusakan prosesor",
        "solution": "Melepas prosesor dari soket, membersihkan bagian prosesor dan soketnya, kemudian memasang kembali. Jika laptop tetap tidak menyala, kemungkinan terjadi kerusakan pada mainboard."
    },
    "K3": {
        "name": "Kerusakan modul RAM",
        "solution": "Membersihkan modul RAM dan soket RAM, kemudian melakukan pengujian ulang. Jika diperlukan, dilakukan pengujian dengan monitor eksternal."
    },
    "K4": {
        "name": "Kerusakan DVD RW/Combo",
        "solution": "Melepas perangkat DVD RW/Combo dan membersihkan bagian konektor. Jika perangkat tidak dapat membaca/menulis CD/DVD, dilakukan penggantian."
    },
    "K5": {
        "name": "Kerusakan keyboard",
        "solution": "Membersihkan bagian keyboard yang bermasalah serta memeriksa kabel/soket keyboard yang terhubung ke mainboard."
    },
    "K6": {
        "name": "Gangguan driver VGA atau komponen grafis",
        "solution": "Melakukan instalasi ulang/pembaruan driver VGA. Jika tampilan masih tidak normal, periksa kabel LCD, komponen VGA, atau mainboard."
    },
    "K7": {
        "name": "Kerusakan power switch",
        "solution": "Memeriksa dan membersihkan komponen power switch. Jika laptop tetap tidak dapat menyala, kemungkinan terdapat gangguan pada rangkaian daya di mainboard."
    },
    "K8": {
        "name": "Kerusakan motherboard",
        "solution": "Jika setelah pemeriksaan komponen lain laptop tetap tidak berfungsi, disimpulkan kerusakan motherboard dan disarankan diperiksa teknisi."
    }
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

    facts = set(selected_symptoms)
    used_rules = set()
    log = []

    step = 1

    while True:
        new_fact = False

        for rule_code in sorted(RULES.keys()):
            if rule_code in used_rules:
                continue

            conditions = RULES[rule_code]
            facts_before = sorted(facts)

            satisfied = (
                all(c in facts for c in conditions)
                if mode == "AND"
                else any(c in facts for c in conditions)
            )

            log.append({
                "step": step,
                "rule": rule_code,
                "status": satisfied,
                "if_condition": conditions,
                "then_code": rule_code,
                "then_name": FAULTS[rule_code]["name"],
                "facts_before": facts_before,
                "facts_after": sorted(facts)
            })

            step += 1

            if satisfied:
                used_rules.add(rule_code)
                if rule_code not in facts:
                    facts.add(rule_code)
                    new_fact = True

        if not new_fact:
            break

    final_faults = [
        {
            "code": f,
            "name": FAULTS[f]["name"],
            "solution": FAULTS[f]["solution"]
        }
        for f in facts if f in FAULTS
    ]

    return {
        "facts_initial": selected_symptoms,
        "log": log,
        "final_faults": final_faults,
        "mode": mode
    }
