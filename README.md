# Assetto Corsa Competizione Career Event Optimizer

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization?sort=semver)](https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/releases)
[![Downloads](https://img.shields.io/github/downloads/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/total?label=Downloads&color=blue)](https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/releases)

---

##  What This Tool Does

This utility helps clean up your 1SE.json career save file by removing:

- Duplicate events (based on track and mode)
- Duplicate team/car entries (based on teamGuid)
- Null byte corruption for safer loading


**Cleans up your ACC career save file by removing:**
-  Duplicate events (same track + mode)
-  Duplicate team entries in car lists

It automatically:
- Detects your `1SE.json` save file (or lets you pick it manually)
- Backs up your original file
- Saves the cleaned version to your **Downloads** folder

---

##  How to Use

### - Option 1: Download the `.exe` (No Python Needed)

1. Go to the [Releases Page](https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/releases)
2. Download the `CareerEventOptimizer.exe`
3. Run it — a GUI will pop up
4. It auto-finds your `1SE.json` or lets you choose manually

---

### - Option 2: Run the Python Script

1. Clone the repo:
   ```bash
   git clone https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization.git
   cd Assetto-Corsa-Competizione-Event-Save-Optimization
Create a virtual environment and install requirements:

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt  # (if needed)
Run the script:

bash
Copy
Edit
python CareerEventOptimizer.py


---

##  Disclaimer

This is the **first script I've ever written**, so I'm still learning.

If you spot bugs, have suggestions, or want to improve the code, feel free to open an issue or pull request.

**All constructive feedback is welcome and appreciated.**

---

