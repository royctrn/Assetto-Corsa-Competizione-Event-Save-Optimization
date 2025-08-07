# Assetto Corsa Competizione Career Event Optimizer

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization?sort=semver)](https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/releases)
[![Downloads](https://img.shields.io/github/downloads/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/total?label=Downloads&color=blue)](https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/releases)

---

## Overview

This tool cleans up your `1SE.json` save file from Assetto Corsa Competizione’s Career Mode. It removes:

- Duplicate events (same track and mode)
- Duplicate team/car entries (based on `teamGuid`)
- Null byte corruption

Cleaning the file can help reduce load times and improve save stability.

## Features

- Automatically detects your `1SE.json` file or allows manual selection
- Backs up the original file before making any changes
- Saves a cleaned version to your Downloads folder
- Available as both a standalone `.exe` and a Python script

## How to Use

### Option 1: Download the `.exe` (No Python Required)

1. Go to the [Releases](https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization/releases) page.
2. Download `CareerEventOptimizer.exe`.
3. Run the program. A simple GUI will appear.
4. It will either auto-detect your save or let you choose it manually.
5. A cleaned version will be saved to your Downloads folder, and a backup of the original will be created.

### Option 2: Run the Python Script

1. Clone the repository:

    ```bash
    git clone https://github.com/royctrn/Assetto-Corsa-Competizione-Event-Save-Optimization.git
    cd Assetto-Corsa-Competizione-Event-Save-Optimization
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python CareerEventOptimizer.py
    ```

## Disclaimer

This is the first Python script I've written. I'm still learning, so if you have suggestions, spot bugs, or want to contribute improvements, feel free to open an issue or pull request. Feedback is always welcome.

## License

This project is licensed under the [MIT License](LICENSE).
