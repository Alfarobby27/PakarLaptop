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

# ================= RULE BASE =================

RULES = {
    "R1": {"if": ["G1", "G2", "G3", "G6"], "then": "K1"},
    "R2": {"if": ["G4"], "then": "K2"},
    "R3": {"if": ["G5"], "then": "K3"},
    "R4": {"if": ["G7", "G8"], "then": "K4"},
    "R5": {"if": ["G9"], "then": "K5"},
    "R6": {"if": ["G10"], "then": "K6"},
    "R7": {"if": ["G11"], "then": "K7"}
}

# ================= FORWARD CHAINING =================
def forward_chaining(selected_symptoms, mode="AND"):

    facts = set(selected_symptoms)
    initial_facts = set(facts)

    log = []
    step = 1
    last_conclusion = None

    mode = mode.upper()
    if mode not in ("AND", "OR"):
        raise ValueError("Mode harus 'AND' atau 'OR'")

    for rule_code, rule in RULES.items():
        premises = rule["if"]
        conclusion = rule["then"]
        facts_before = sorted(facts)

        # Cek minimal satu premis cocok untuk menjalankan rule
        if any(p in facts for p in premises):
            # Evaluasi status rule sesuai mode
            if mode == "AND":
                status = all(p in facts for p in premises)
            else:  # OR
                status = any(p in facts for p in premises)

            # Tambahkan kesimpulan jika status True
            if status and conclusion not in facts:
                facts.add(conclusion)
                last_conclusion = conclusion

            log.append({
                "step": step,
                "rule": rule_code,
                "if_condition": premises,
                "then_code": conclusion,
                "then_name": FAULTS.get(conclusion, {}).get("name", ""),
                "status": status,
                "facts_before": facts_before,
                "facts_after": sorted(facts)
            })

            step += 1

    final_fault = None
    if last_conclusion:
        final_fault = {
            "code": last_conclusion,
            "name": FAULTS[last_conclusion]["name"],
            "solution": FAULTS[last_conclusion]["solution"]
        }

    return {
        "mode": mode,
        "facts_initial": sorted(initial_facts),
        "facts_final": sorted(facts),
        "final_fault": final_fault,
        "log": log
    }

