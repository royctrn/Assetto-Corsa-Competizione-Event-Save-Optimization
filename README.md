# Assetto-Corsa-Competizione-Event-Save-Optimization
Assetto Corsa Competizione’s career mode save file (1SE.json) can become bloated with duplicate events and team entries over time, causing performance issues and long load times.  This tool automatically locates your save file, backs it up, removes duplicates, and exports a clean version to your Downloads folder — all in one click.

# 🏁 Assetto Corsa Competizione Career Event Optimizer

A simple, one-click tool that finds and cleans your **1SE.json career save file** for Assetto Corsa Competizione.

This tool removes duplicate events and team entries from your career progression file, creates a backup of the original, and exports a cleaned version to your **Downloads** folder.

---

## 💡 What It Does

✅ Automatically finds your `1SE.json` save file  
✅ Removes duplicate events (based on track + mode)  
✅ Removes duplicate team/car entries (based on `teamGuid`)  
✅ Backs up your original file  
✅ Saves the cleaned version to your **Downloads** folder

---

## 🛠 How to Use

1. Download and run `CareerEventOptimizer.exe`
2. A popup will ask:
   - Click **Yes** to let the tool auto-detect your save file
   - Click **No** to manually select the `1SE.json` file
3. The tool will:
   - Create a backup as `1SE_backup.json`
   - Clean the save file
   - Save a new version to your **Downloads** folder as `1SE.json`
4. You can copy the cleaned file back into your game save folder

---

## 📁 Default File Location

The script looks for your save file in one of these locations:

```plaintext
C:\Users\<YourName>\Documents\Assetto Corsa Competizione\Savegames\1SE.json
C:\Users\<YourName>\Documents\Assetto Corsa Competizione\Savegames\<profile_folder>\1SE.json
