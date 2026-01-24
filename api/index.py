import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from flask import Flask, render_template, request
from rules import SYMPTOMS, FAULTS, forward_chaining

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gejala")
def data_gejala():
    return render_template("gejala.html", symptoms=SYMPTOMS)

@app.route("/kerusakan")
def data_kerusakan():
    return render_template("kerusakan.html", faults=FAULTS)

@app.route("/tentang")
def data_tentang():
    return render_template("tentang.html")

@app.route("/diagnose-start")
def diagnosa_page():
    return render_template("form.html", symptoms=SYMPTOMS)

@app.route("/hasil", methods=["POST"])
def hasil_diagnosa():
    selected = request.form.getlist("symptoms")
    mode = request.form.get("mode", "AND")

    log_data = forward_chaining(selected, mode)

    mode_label = {
        "AND": "AND (Semua gejala harus terpenuhi)",
        "OR": "OR (Salah satu gejala terpenuhi)"
    }.get(mode, mode)

    return render_template(
        "result.html",
        selected_symptoms=selected,
        process_log=log_data["log"],
        final_fault_detail=log_data["final_faults"],
        mode=mode,
        mode_label=mode_label,
        SYMPTOMS=SYMPTOMS
    )

# WAJIB untuk Vercel
app = app
