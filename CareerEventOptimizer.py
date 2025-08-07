import json
import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def get_1se_json_path() -> str:
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    savegame_base = os.path.join(documents_path, "Assetto Corsa Competizione", "Savegames")

    # First: Check if 1SE.json exists directly inside Savegames
    direct_path = os.path.join(savegame_base, "1SE.json")
    if os.path.isfile(direct_path):
        return direct_path

    # If not, check inside any subfolders (like for other users with profile folders)
    possible_folders = glob.glob(os.path.join(savegame_base, "*"))
    for folder in possible_folders:
        target_file = os.path.join(folder, "1SE.json")
        if os.path.isfile(target_file):
            return target_file

    return None


def clean_json_bytes(input_json_path: str):
    try:
        with open(input_json_path, 'rb') as f:
            raw = f.read()
        clean_text = raw.replace(b'\x00', b'')
        try:
            decoded = clean_text.decode('utf-8')
        except UnicodeDecodeError:
            decoded = clean_text.decode('latin1')
        return json.loads(decoded)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read or decode JSON:\n{e}")
        return None

def remove_duplicate_events(data: dict) -> int:
    seen_keys = set()
    unique_events = []
    removed = 0

    for event in data.get("events", []):
        key = (event.get("track"), event.get("mode"))
        if key not in seen_keys:
            seen_keys.add(key)
            unique_events.append(event)
        else:
            removed += 1

    data["events"] = unique_events
    return removed

def remove_duplicate_teams(data: dict) -> int:
    removed = 0
    for event in data.get("events", []):
        if "carSet" in event and "cars" in event["carSet"]:
            seen_team_guids = set()
            unique_cars = []
            for car in event["carSet"]["cars"]:
                team_guid = car["info"].get("teamGuid")
                if team_guid not in seen_team_guids:
                    seen_team_guids.add(team_guid)
                    unique_cars.append(car)
                else:
                    removed += 1
            event["carSet"]["cars"] = unique_cars
    return removed

def optimize_file(input_path: str):
    data = clean_json_bytes(input_path)
    if not data:
        return

    # Backup original
    backup_path = input_path.replace("1SE.json", "1SE_backup.json")
    shutil.copy2(input_path, backup_path)

    # Output to Downloads folder
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(downloads, "1SE.json")

    if os.path.exists(output_path):
        confirm = messagebox.askyesno("Overwrite?", f"{output_path} already exists. Overwrite?")
        if not confirm:
            return

    removed_events = remove_duplicate_events(data)
    removed_teams = remove_duplicate_teams(data)
    total_removed = removed_events + removed_teams

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo(
        "Success!",
        f"Cleaned file saved to Downloads as '1SE.json'\n"
        f"Backup created as '1SE_backup.json'\n\n"
        f"Removed Duplicates:\n- Events: {removed_events}\n- Teams: {removed_teams}\n- Total: {total_removed}"
    )

def run_gui():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask if user wants to use the auto-detected file or select manually
    use_auto = messagebox.askyesno("Choose File", "Try to auto-detect your ACC save file?\nClick No to choose manually.")

    if use_auto:
        input_path = get_1se_json_path()
        if not input_path:
            messagebox.showerror("Not Found", "Could not find '1SE.json' in your ACC Savegame folder.")
            return
    else:
        input_path = filedialog.askopenfilename(title="Select 1SE.json", filetypes=[("JSON Files", "*.json")])
        if not input_path:
            return

    optimize_file(input_path)

if __name__ == "__main__":
    run_gui()
