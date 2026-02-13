<!-- ================= HEADER ================= -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&height=240&section=header&text=PakarLaptop&fontSize=54&fontColor=ffffff&animation=twinkling&fontAlignY=38" alt="PakarLaptop - Sistem Pakar Diagnosa Laptop" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=26&duration=4000&pause=800&color=1E90FF&center=true&vCenter=true&width=850&lines=Sistem+Pakar+Diagnosa+Kerusakan+Laptop;Menggunakan+Metode+Forward+Chaining;Berbasis+Flask+%2B+Python+%2B+Tailwind+CSS;Proyek+Kelompok+2+-+2024+%F0%9F%9A%80" alt="Typing animation" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Alfarobby27&repo=PakarLaptop&label=Visitors&color=1E90FF&style=flat-square" alt="Repo visitors" />
  <img src="https://img.shields.io/github/stars/Alfarobby27/PakarLaptop?style=flat-square&logo=github&color=yellow" alt="Stars" />
  <img src="https://img.shields.io/github/forks/Alfarobby27/PakarLaptop?style=flat-square&logo=github&color=blue" alt="Forks" />
  <img src="https://img.shields.io/github/license/Alfarobby27/PakarLaptop?style=flat-square&color=success" alt="License" />
</p>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

<br>

## 📖 Tentang Proyek

**PakarLaptop** adalah **aplikasi web sistem pakar** yang membantu mendiagnosa kerusakan laptop berdasarkan gejala yang dipilih pengguna.  
Menggunakan metode **Forward Chaining** (rule-based inference) untuk menyimpulkan kerusakan secara logis dan memberikan **solusi perbaikan** yang praktis.

### ✨ Fitur Utama
- Diagnosa otomatis berbasis gejala (multi-select)
- Mesin inferensi Forward Chaining sederhana tapi powerful
- UI responsif & modern (Tailwind CSS + Flask templates)
- Hasil diagnosa + saran langkah perbaikan jelas
- Mudah di-deploy ke Vercel (serverless-friendly)
- Kode bersih, mudah dimodifikasi / ditambah rule baru

<br>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

## 🚀 Cara Menjalankan Lokal (Step-by-Step)

```bash
# 1. Clone repo
git clone https://github.com/Alfarobby27/PakarLaptop.git

# 2. Masuk ke direktori
cd PakarLaptop

# 3. Buat & aktifkan virtual environment (sangat direkomendasikan)
python -m venv venv

# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate

# 4. Install dependensi
pip install --upgrade pip
pip install -r requirements.txt

# 5. Jalankan aplikasi
# Cara 1: simple
python app.py

# Cara 2: dengan debug mode (auto-reload saat edit kode)
flask --debug run
```

Buka browser:

```
http://localhost:5000
atau
http://127.0.0.1:5000
```

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

## 👥 Anggota Kelompok 2

| NPM          | Nama |
| ------------ | ----------------------------------------------------------- |
| 202243500496 | Muhamad Suhada |
| 202243500497 | [Alfarobby](https://github.com/Alfarobby27) |
| 202243500500 | [Ahmad Badawi](https://github.com/Ahmadbadawi123) |
| 202243500501 | [Abdur Rosyid Fachriansyah](https://github.com/dellwatch21) |
| 202243500502 | [Sangga Buana](https://github.com/sanggabuana453) |
| 202243500540 | Novia Citra Sholihah |
| 202243500503 | Rani Stevidayanti |
| 202243500538 | Raditha Andaliaripa |

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

## 🛠️ Teknologi yang Digunakan

<p align="center">
  <style>
    .tech-card {
      display: inline-block;
      margin: 10px;
      padding: 12px 16px;
      background: linear-gradient(135deg, #0f172a, #1e293b);
      border-radius: 16px;
      border: 1px solid #334155;
      transition: all 0.3s ease;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
      cursor: pointer;
    }
    .tech-card:hover {
      transform: scale(1.12);
      box-shadow: 0 0 20px rgba(30, 144, 255, 0.6);
      border-color: #1e90ff;
    }
    .tech-card img {
      display: block;
      margin: 0 auto 8px;
    }
    .tech-card span {
      font-size: 0.9rem;
      color: #94a3b8;
      font-weight: 500;
    }
  </style>

  <div class="tech-card">
    <a href="https://www.python.org/" target="_blank">
      <img src="https://skillicons.dev/icons?i=python" height="60" alt="Python" />
    </a>
    <span>Python 3.9+</span>
  </div>

  <div class="tech-card">
    <a href="https://flask.palletsprojects.com/" target="_blank">
      <img src="https://skillicons.dev/icons?i=flask" height="60" alt="Flask" />
    </a>
    <span>Flask</span>
  </div>

  <div class="tech-card">
    <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank">
      <img src="https://skillicons.dev/icons?i=html" height="60" alt="HTML5" />
    </a>
    <span>HTML5</span>
  </div>

  <div class="tech-card">
    <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank">
      <img src="https://skillicons.dev/icons?i=css" height="60" alt="CSS3" />
    </a>
    <span>CSS3</span>
  </div>

  <div class="tech-card">
    <a href="https://tailwindcss.com/" target="_blank">
      <img src="https://skillicons.dev/icons?i=tailwind" height="60" alt="Tailwind CSS" />
    </a>
    <span>Tailwind CSS</span>
  </div>

  <div class="tech-card">
    <a href="https://vercel.com/" target="_blank">
      <img src="https://skillicons.dev/icons?i=vercel" height="60" alt="Vercel" />
    </a>
    <span>Vercel</span>
  </div>
</p>

<p align="center">
  <sub><b>Python 3.9+ • Flask • HTML5 • CSS3 • Tailwind CSS • Vercel</b></sub>
</p>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

## 🧠 Sumber Pengetahuan (Pakar Digital)

Basis pengetahuan sistem disusun berdasarkan referensi teknisi laptop profesional berikut:

<p align="center">
  <a href="https://youtu.be/Wq_w8ZQ9PnQ" target="_blank">
    <img src="https://img.youtube.com/vi/Wq_w8ZQ9PnQ/maxresdefault.jpg" width="750">
  </a>
</p>

<p align="center">
  <a href="https://youtu.be/Wq_w8ZQ9PnQ" target="_blank">
    <img src="https://img.shields.io/badge/▶%20Watch%20Video-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
  </a>
</p>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

## 🚀 Demo Program

<p align="center">
  <a href="https://pakarlaptop.vercel.app" target="_blank">
    <img src="https://img.shields.io/badge/🚀%20Launch%20Live%20Demo-PakarLaptop-0A66C2?style=for-the-badge&logo=vercel&logoColor=white">
  </a>
</p>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=4&section=header" />
</div>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1E90FF,100:0A66C2&height=170&section=footer&animation=twinkling"/>
</p>
