from flask import Flask, render_template, request
import os
import sys

# ================= PATH SETUP =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from rules import SYMPTOMS, FAULTS, RULES, forward_chaining

# ================= APP INIT =================
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# =========================================================
# ROUTE: HOME
# =========================================================
@app.route("/")
def index():
    return render_template("index.html")


# =========================================================
# ROUTE: DATA MASTER
# =========================================================
@app.route("/gejala")
def data_gejala():
    return render_template("gejala.html", symptoms=SYMPTOMS)


@app.route("/kerusakan")
def data_kerusakan():
    return render_template("kerusakan.html", faults=FAULTS)


@app.route("/tentang")
def data_tentang():
    return render_template("tentang.html")


# =========================================================
# ROUTE: FORM DIAGNOSA
# =========================================================
@app.route("/diagnose-start")
def diagnosa_page():
    return render_template(
        "form.html",
        symptoms=SYMPTOMS,
        rules=RULES
    )


# =========================================================
# ROUTE: HASIL DIAGNOSA (FORWARD CHAINING EXECUTION)
# =========================================================
@app.route("/hasil", methods=["POST"])
def hasil_diagnosa():

    # ================= 1. AMBIL INPUT USER =================
    raw_symptoms = request.form.getlist("symptoms")
    selected_symptoms = sorted(set(raw_symptoms))

    mode = request.form.get("mode", "AND").upper()
    if mode not in ["AND", "OR"]:
        mode = "AND"

    mode_label = {
        "AND": "AND (Semua gejala harus terpenuhi)",
        "OR": "OR (Minimal satu gejala terpenuhi)"
    }[mode]

    # ================= 2. VALIDASI INPUT =================
    if not selected_symptoms:
        return render_template(
            "result.html",
            error="Silakan pilih minimal satu gejala.",
            selected_symptoms=[],
            mode=mode,
            mode_label=mode_label,
            SYMPTOMS=SYMPTOMS,
            process_log=[],
            final_fault=None,
            diagnosis_message=None,
            facts_initial=[],
            facts_final=[]
        )

    try:
        # ================= 3. EKSEKUSI FORWARD CHAINING =================
        result = forward_chaining(selected_symptoms, mode)

    except Exception as e:
        # Error handling agar sistem tetap stabil
        return render_template(
            "result.html",
            error=f"Terjadi kesalahan pada proses inferensi: {str(e)}",
            selected_symptoms=selected_symptoms,
            mode=mode,
            mode_label=mode_label,
            SYMPTOMS=SYMPTOMS,
            process_log=[],
            final_fault=None,
            diagnosis_message=None,
            facts_initial=[],
            facts_final=[]
        )

    # ================= 4. AMBIL HASIL INFERENSI =================
    final_fault = result.get("final_fault", None)
    facts_initial = result.get("facts_initial", [])
    facts_final = result.get("facts_final", [])
    process_log = result.get("log", [])

    # ================= 5. PESAN DIAGNOSA =================
    if final_fault:
        diagnosis_message = None
    else:
        diagnosis_message = "Tidak ditemukan kerusakan berdasarkan gejala yang dipilih."


    # ================= 6. RENDER VIEW =================
    return render_template(
        "result.html",
        selected_symptoms=selected_symptoms,
        mode=mode,
        mode_label=mode_label,
        SYMPTOMS=SYMPTOMS,
        process_log=process_log,
        final_fault=final_fault,
        diagnosis_message=diagnosis_message,
        facts_initial=facts_initial,
        facts_final=facts_final
    )


# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)
