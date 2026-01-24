from flask import Flask, render_template, request
from rules import SYMPTOMS, FAULTS, forward_chaining

app = Flask(__name__)

@app.route("/diagnose-start")
def diagnosa_page():
    return render_template("form.html", symptoms=SYMPTOMS)

@app.route("/hasil", methods=["POST"])
def hasil_diagnosa():
    selected_symptoms = request.form.getlist("symptoms")
    mode = request.form.get("mode", "AND")

    result = forward_chaining(selected_symptoms, mode)

    mode_label = {
        "AND": "AND (Semua gejala harus terpenuhi)",
        "OR": "OR (Salah satu gejala terpenuhi)"
    }[mode]

    return render_template(
        "result.html",
        selected_symptoms=result["facts_initial"],
        process_log=result["log"],
        final_fault_detail=result["final_faults"],
        inference_finished_at=result["inference_finished_at"],  # 🔴 INI KUNCI
        mode=mode,
        mode_label=mode_label,
        SYMPTOMS=SYMPTOMS
    )

app = app
