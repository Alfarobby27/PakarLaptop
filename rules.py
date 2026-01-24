from typing import List, Dict, Any

# ================= DATA =================

FAULTS = {
    "K1": {
        "name": "Kerusakan kabel fleksibel LCD",
        "solution": "Memeriksa dan membersihkan kabel fleksibel LCD."
    },
    "K2": {
        "name": "Kerusakan prosesor",
        "solution": "Membersihkan dan memasang ulang prosesor."
    },
    "K3": {
        "name": "Kerusakan modul RAM",
        "solution": "Membersihkan dan menguji ulang RAM."
    },
    "K4": {
        "name": "Kerusakan DVD RW/Combo",
        "solution": "Membersihkan atau mengganti DVD RW."
    },
    "K5": {
        "name": "Kerusakan keyboard",
        "solution": "Membersihkan atau mengganti keyboard."
    },
    "K6": {
        "name": "Gangguan driver VGA",
        "solution": "Instal ulang driver VGA."
    },
    "K7": {
        "name": "Kerusakan power switch",
        "solution": "Periksa dan bersihkan power switch."
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
