import os
import regex
import re
import sys
import subprocess
# Check if tqdm is installed, and if not, install it
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing tqdm...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm

# Python version 3.11.5
# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66

# โปรแกรมนี้ใช้เพื่อหาตัวอักษรภาษาไทยใดที่มีวรรณยุกต์มากกว่า2ตัวขึ้นไป
# This program is used to find any Thai characters that have more than 2 diacritics.

# How to use on PC
# Just input Folder paths, the keyword you want to search, and the file extension

# วิธีใช้บนคอม
# เพียงป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

# How to use in moblie version
# Please run in Pydroid 3 - IDE for Python 3
# Then Just input Folder paths and the file extension
# If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]

# วิธีใช้บนมือถือ
# ให้รันบนPydroid 3 - IDE for Python 3
# ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
# เพียงป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

def to_raw_string(s):
    return s.encode('unicode_escape').decode()

def natural_keys(text):
    return [int(c) if c.isdigit() else c for c in re.split('(\d+)', text)]

def check_diacritics(line, base_characters):
    diacritics = ['่', '้', '๊', '๋', 'ิ', 'ี', 'ึ', 'ื', 'ั', '็', '์']
    for char in set(line):
        if char in base_characters:
            count = sum(1 for match in regex.finditer(f"{char}[{''.join(diacritics)}]+", line, overlapped=True) if len(match.group(0)) > 3)
            if count:
                return char
    return None

def process_file(file_path, base_characters):
    results = []

    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()

        for line_number, line in enumerate(lines, start=1):
            problematic_char = check_diacritics(line, base_characters)
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

โปรแกรมนี้ใช้เพื่อหาตัวอักษรภาษาไทยใดที่มีวรรณยุกต์มากกว่า2ตัวขึ้นไป
This program is used to find any Thai characters that have more than 2 diacritics.
 
How to use on PC
Just input Folder paths, the keyword you want to search, and the file extension

วิธีใช้บนคอม
เพียงป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 

How to use in moblie version
Please run in Pydroid 3 - IDE for Python 3
Then Just input Folder paths and the file extension
If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]

วิธีใช้บนมือถือ
ให้รันบนPydroid 3 - IDE for Python 3
ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
เพียงป้อนตำแหน่งของโฟลเดอร์ และนามสกุลของไฟล์นั้น ๆ 
""")
    while True:
        folder_paths = []

        while True:
            folder_path = input("Enter folder path (or 'done' to finish): ")

            if folder_path.lower() == 'done' and not folder_paths:
                print("You haven't added any folder paths yet. Please add at least one folder path.")
                continue
            elif folder_path.lower() == 'done':
                break

            raw_folder_path = to_raw_string(folder_path)

            if not os.path.exists(raw_folder_path):
                print("The provided path does not exist. Please enter a valid folder path.")
                continue

            if raw_folder_path in folder_paths:
                print("You have already added this folder path. Please add a different one.")
                continue
            
            folder_paths.append(raw_folder_path)

        for folder in folder_paths:
            file_extension = input(f"Enter the file extension you want to search for folder {folder} (e.g., txt or .txt): ").strip()
            if file_extension.startswith('.'):
                file_extension = file_extension[1:]

            files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.' + file_extension)]

            matching_files = sorted(files, key=natural_keys)

            all_results = []
            for file in tqdm(matching_files, desc="Processing files", unit="file"):
                all_results.extend(process_file(file, base_characters))
            
            if all_results:
                for file, line_number, char in all_results:
                    print(f"In file {os.path.basename(file)}, line {line_number}, char '{char}' has more than 2 diacritics.")
            else:
                print(f"No characters with more than 2 diacritics found in folder : {folder}.")

        # Asking to run the program again
        again = input("Do you want to run the program again? (yes/no): ").strip().lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()