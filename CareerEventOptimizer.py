# Asseto Corsa Competizione Event Save Optimizer


# CareerEventOptimizer.py
# This script optimizes the 1SE.json file by removing duplicate events and teams. 
# It provides a GUI for user interaction and saves the cleaned file to the Downloads folder.

# SPDX-License-Identifier: GPL-3.0-or-later
 
# Created by: Roy Tran (royctrn)
# Date: 2025-08-06

import json     #Read and write JSON files
import os       #File and directory operations
import glob     #Glob patterns for file searching
import shutil   #File operations like copy
import tkinter as tk #GUI toolkit for Python to show pop ups and dialogs
from tkinter import filedialog, messagebox #GUI dialogs for file selection and messages

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
# May just exit the program if no file is found

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

# This function removes duplicate teams from the car sets in each event.
# It checks for unique team GUIDs and keeps only the first occurrence of each team.
# Returns the number of removed teams.

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

    # This function optimizes the 1SE.json file by removing duplicate events and teams.
    # It reads the JSON file, processes it to remove duplicates, and saves the cleaned data.
    
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
    
    # This function optimizes the 1SE.json file by removing duplicate events and teams.
    # It reads the JSON file, processes it to remove duplicates, and saves the cleaned data.
    # It also creates a backup of the original file and saves the cleaned file to the Downloads folder.


    # Note:
    # The script currently does not handle file locking issues.
    # If the file is open in another program, it may raise an error when trying to overwrite it.
    # This can be improved by checking if the file is in use and prompting the user accordingly.



# Potential improvements:
# - Implement a logging system to keep track of how many events and teams were removed, and how many times the script was run.
# - Allow the user to choose where to save the cleaned file instead of defaulting to Downloads.
# - Add error handling for cases where the JSON structure is not as expected or if the file is corrupted.
# - Consider adding a progress bar or status updates for larger files.
# - Add a check to see if the file is in use, and if so, ask the user to close it
# - Automate the backup creation and file overwriting process 
# - Create a new folder the save folder to contain the backup file and log.txt file


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

# This will run the GUI to allow the user to select the file and perform the optimization.


if __name__ == "__main__":
    run_gui()

# Main entry point for the script
# This will run the GUI to allow the user to select the file and perform the optimization.




# This script is designed to be run as a standalone application.