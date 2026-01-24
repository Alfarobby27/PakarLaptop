from typing import List, Dict, Any

# ================= DATA =================

FAULTS = {
    "K1": {
        "name": "Kerusakan kabel fleksibel LCD",
        "solution": "Memeriksa dan membersihkan kabel fleksibel LCD yang terhubung ke panel LCD dan mainboard. Apabila kondisi tidak berubah, dilakukan penggantian kabel fleksibel LCD."
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
        "solution": "Melepas perangkat DVD RW/Combo dan membersihkan bagian konektor. Apabila perangkat tidak dapat membaca atau menulis data, dilakukan penggantian DVD RW/Combo."
    },
    "K5": {
        "name": "Kerusakan keyboard",
        "solution": "Membersihkan bagian keyboard yang bermasalah serta memeriksa kabel dan soket keyboard yang terhubung ke mainboard."
    },
    "K6": {
        "name": "Gangguan driver VGA",
        "solution": "Melakukan instalasi ulang atau pembaruan (update) driver VGA. Jika tampilan masih tidak normal, dilakukan pemeriksaan pada kabel LCD, komponen VGA, atau mainboard."
    },
    "K7": {
        "name": "Kerusakan power switch",
        "solution": "Memeriksa dan membersihkan komponen power switch. Jika laptop tetap tidak dapat menyala, kemungkinan terdapat gangguan pada rangkaian daya di mainboard."
    },
    "K8": {
        "name": "Kerusakan motherboard",
        "solution": "Apabila setelah dilakukan pemeriksaan komponen lain laptop tetap tidak berfungsi, maka disimpulkan terjadi kerusakan pada motherboard dan disarankan dilakukan pemeriksaan lanjutan oleh teknisi."
    }
}

SYMPTOMS = {
    "G1": "Layar putih",
    "G2": "Gambar bergetar",
    "G3": "Layar berkedip",
    "G4": "Lampu indikator mati kembali",
    "G5": "Lampu menyala tapi layar kosong",
    "G6": "LCD hidup mati",
    "G7": "DVD tidak terdeteksi",
    "G8": "DVD tidak membaca",
    "G9": "Keyboard tidak berfungsi",
    "G10": "Tampilan bergaris",
    "G11": "Laptop sulit menyala"
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
    facts = set(selected_symptoms)
    used_rules = set()
    log = []

    step = 1
    inference_finished_at = 0

    while True:
        new_fact = False

        for rule, conditions in RULES.items():
            if rule in used_rules:
                continue

            facts_before = sorted(facts)

            satisfied = (
                all(c in facts for c in conditions)
                if mode == "AND"
                else any(c in facts for c in conditions)
            )

            if satisfied:
                used_rules.add(rule)
                if rule not in facts:
                    facts.add(rule)
                    new_fact = True
                    inference_finished_at = step

            log.append({
                "step": step,
                "rule": rule,
                "status": satisfied,
                "if_condition": conditions,
                "then_code": rule,
                "then_name": FAULTS[rule]["name"],
                "facts_before": facts_before,
                "facts_after": sorted(facts)
            })

            step += 1

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
        "facts_initial": sorted(set(selected_symptoms)),
        "log": log,
        "final_faults": final_faults,
        "inference_finished_at": inference_finished_at,
        "mode": mode
    }
