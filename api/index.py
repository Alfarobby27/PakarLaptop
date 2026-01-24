from flask import Flask, render_template, request
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from rules import SYMPTOMS, FAULTS, forward_chaining

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# ================= HOME =================
@app.route("/")
def index():
    return render_template("index.html")

# ================= DATA =================
@app.route("/gejala")
def data_gejala():
    return render_template("gejala.html", symptoms=SYMPTOMS)

@app.route("/kerusakan")
def data_kerusakan():
    return render_template("kerusakan.html", faults=FAULTS)

@app.route("/tentang")
def data_tentang():
    return render_template("tentang.html")

# ================= DIAGNOSA =================
@app.route("/diagnose-start")
def diagnosa_page():
    return render_template("form.html", symptoms=SYMPTOMS)

@app.route("/hasil", methods=["POST"])
def hasil_diagnosa():
    raw_symptoms = request.form.getlist("symptoms")
    selected_symptoms = sorted(set(raw_symptoms))
    mode = request.form.get("mode", "AND")

    result = forward_chaining(selected_symptoms, mode)

    mode_label = {
        "AND": "AND (Semua gejala harus terpenuhi)",
        "OR": "OR (Salah satu gejala terpenuhi)"
    }[mode]

    return render_template(
        "result.html",
        selected_symptoms=selected_symptoms,
        process_log=result["log"],
        final_fault_detail=result["final_faults"],
        inference_finished_at=result["inference_finished_at"],
        mode=mode,
        mode_label=mode_label,
        SYMPTOMS=SYMPTOMS
    )


# 🔴 PENTING UNTUK VERCEL
app = app
