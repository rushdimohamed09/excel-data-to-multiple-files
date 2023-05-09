# MIT License

# Copyright (c) 2023 Rushdi Mohamed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pandas as pd
import json
import sys
import os

# Check if filename parameter was provided
isParameter = False
if len(sys.argv) > 1:
    isParameter = True
    filename = sys.argv[1].split('=')[1]
else:
    filename = 'languageData.xlsx'

# Read the Excel file into a Pandas dataframe
try:
    df = pd.read_excel(filename, header=1)
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
    if (isParameter):
        print(f"Provided parameter filename : '{filename}' is not found in the current directory, \nPlease add the file to the current directory and run the command back!")
    else:
        print(f"Seems like you have mistakenly deleted the '{filename}'")
    sys.exit(1)

# Get the language columns from the dataframe
language_columns = list(df.columns[2:])

# Create folders for each language
parent_folder = "lang"
os.makedirs(parent_folder, exist_ok=True)

# Loop through the dataframe and create a dictionary of dictionaries for each language
lang_dict = {}
for lang in language_columns:
    lang_dict[lang] = {}
    for index, row in df.iterrows():
        key_name = row[0]
        text = row[lang]
        if pd.notnull(text):
            keys = key_name.split(".")
            cur_dict = lang_dict[lang]
            for key in keys[:-1]:
                cur_dict = cur_dict.setdefault(key, {})
            cur_dict[keys[-1]] = text

# Loop through the language dictionary and write the custom_php files for each language
for lang, lang_dict in lang_dict.items():
    file_name = lang.lower()
    file_path = os.path.join("lang", file_name+'.json')
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(lang_dict, f, ensure_ascii=False, indent=4)
