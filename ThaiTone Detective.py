import os
import re
import sys
import subprocess
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing tqdm...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm
try:
    import regex
except ImportError:
    print("regex not found! Installing regex...")
    subprocess.run([sys.executable, "-m", "pip", "install", "regex"])
    import regex

# Python version 3.11.5
# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66

# โหมด1ใช้เพื่อหาตัวอักษรภาษาไทยใดที่มีวรรณยุกต์มากกว่า2ตัวขึ้นไป
# Mode 1 is used to find any Thai characters that have more than 2 diacritics.

# โหมด2ไว้ใช้หาตัวอักษรภาษาไทยใดที่มีวรรณยุกต์ผิดแปลกไป
# Mode 2 is used to find any Thai characters that have unusual tones.

# How to use on PC
# Just input Folder paths, and the file extension

# วิธีใช้บนคอม
# เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

# How to use in moblie version
# Please run in Pydroid 3 - IDE for Python 3
# Then Just input Folder paths and the file extension
# If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]

# วิธีใช้บนมือถือ
# ให้รันบนPydroid 3 - IDE for Python 3
# ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
# เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

def to_raw_string(s):
    return s.encode('unicode_escape').decode()

def natural_keys(text):
    return [int(c) if c.isdigit() else c for c in re.split('(\d+)', text)]

def check_diacritics_original(line, base_characters):
    diacritics = ['่', '้', '๊', '๋', 'ิ', 'ี', 'ึ', 'ื', 'ั', '็', '์']
    for char in set(line):
        if char in base_characters:
            count = sum(1 for match in regex.finditer(f"{char}[{''.join(diacritics)}]+", line, overlapped=True) if len(match.group(0)) > 3)
            if count:
                return char
    return None

def check_diacritics_advanced(line, base_characters):
    main_diacritics = ['่', '้', '๊', '์']
    secondary_diacritics = ['ิ', 'ี', 'ึ', 'ื', 'ั']

    for char in base_characters:
        # ทำการตรวจสอบเฉพาะเมื่อตัวอักษรภาษาไทยที่ต้องการตรวจสอบพบในบรรทัด
        if char in line:
            # ตรวจสอบ main_diacritics ซ้ำกับ main_diacritics
            for diacritic in main_diacritics:
                count = sum(1 for match in regex.finditer(f"{char}{diacritic}{{2,}}", line))
                if count:
                    return char
                    
            # ตรวจสอบ secondary_diacritics ซ้ำกับ secondary_diacritics
            for diacritic in secondary_diacritics:
                count = sum(1 for match in regex.finditer(f"{char}{diacritic}{{2,}}", line))
                if count:
                    return char

            # ตรวจสอบ main_diacritics ตามด้วย secondary_diacritics โดยการหาทีละตัวอักษรด้วย regex
            for main_diacritic in main_diacritics:
                for secondary_diacritic in secondary_diacritics:
                    if regex.search(f"{char}{main_diacritic}{secondary_diacritic}", line):
                        return char

    return None


def process_file(file_path, base_characters, check_func):
    results = []

    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()

        for line_number, line in enumerate(lines, start=1):
            problematic_char = check_func(line, base_characters)
            if problematic_char:
                results.append((file_path, line_number, problematic_char))

    return results

def main():
    base_characters = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
    
    print("""
Python version 3.11.5
Code from ChatGPT
Made By Bank's : Thai translator H Game
Link Discord : https://discord.gg/q6FkGCHv66

โหมด1ใช้เพื่อหาตัวอักษรภาษาไทยใดที่มีวรรณยุกต์มากกว่า2ตัวขึ้นไป
Mode 1 is used to find any Thai characters that have more than 2 diacritics.

โหมด2ไว้ใช้หาตัวอักษรภาษาไทยใดที่มีวรรณยุกต์ผิดแปลกไป
Mode 2 is used to find any Thai characters that have unusual tones.
 
How to use on PC
Just input Folder paths, and the file extension

วิธีใช้บนคอม
เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

How to use in moblie version
Please run in Pydroid 3 - IDE for Python 3
Then Just input Folder paths and the file extension
If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]

วิธีใช้บนมือถือ
ให้รันบนPydroid 3 - IDE for Python 3
ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ
""")
    print("Select a mode:")
    print("1. Original mode (Find any Thai characters that have more than 2 diacritics)")
    print("2. Advanced mode (Find characters with repeated diacritics of '่', '้', '๊', '์' and special conditions)")
    while True:
        mode = input("Enter the mode number (1/2): ").strip()
        
        if mode in ["1", "2"]:
            break
        else:
            print("Invalid selection. Please choose either 1 or 2.")

    while True:
        folder_paths = []

        while True:
            folder_path = input("Enter folder path (or 'done' to finish): ")

            if folder_path.lower() == 'done' and not folder_paths:
                print("You haven't added any folder paths yet. Please add at least one folder path.")
                continue
            elif folder_path.lower() == 'done':
                break

            if not os.path.exists(folder_path):
                print("The provided path does not exist. Please enter a valid folder path.")
                continue

            if folder_path in folder_paths:
                print("You have already added this folder path. Please add a different one.")
                continue
            
            folder_paths.append(folder_path)

        for folder in folder_paths:
            file_extension = input(f"Enter the file extension you want to search for folder {folder} (e.g., txt or .txt): ").strip()
            if file_extension.startswith('.'):
                file_extension = file_extension[1:]

            files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.' + file_extension)]
            matching_files = sorted(files, key=natural_keys)

            all_results = []
            check_func = check_diacritics_original if mode == "1" else check_diacritics_advanced
            for file in tqdm(matching_files, desc="Processing files", unit="file"):
                all_results.extend(process_file(file, base_characters, check_func))
            
            if all_results:
                for file, line_number, char in all_results:
                    print(f"In file {os.path.basename(file)}, line {line_number}, char '{char}' has more than 2 diacritics.")
            else:
                print(f"No problematic characters found in folder : {folder}.")

        # Asking what the user wants to do next
        while True:
            action = input("What do you want to do next? (yes/no/change mode): ").strip().lower()

            if action == "yes":
                break  # Break out of this loop to restart the main loop
            elif action == "change mode":
                print("Select a new mode:")
                print("1. Original mode (Find any Thai characters that have more than 2 diacritics)")
                print("2. Advanced mode (Find characters with repeated diacritics of '่', '้', '๊', '์' and special conditions)")
                while True:
                    mode = input("Enter the mode number (1/2): ").strip()
                    if mode in ["1", "2"]:
                        break  # Break out of this mode selection loop to restart the main loop with a new mode
                    else:
                        print("Invalid selection. Please choose either 1 or 2.")
                break  # Break out of the main action loop to restart the main loop
            elif action == "no":
                sys.exit()  # Exit the entire program
            else:
                print("Invalid option. Please choose 'yes', 'no', 'change mode'")


if __name__ == "__main__":
    main()
