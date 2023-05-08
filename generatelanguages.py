import pandas as pd
import json
import os

# Read the Excel file into a Pandas dataframe
df = pd.read_excel('languagedata.xlsx', header=1)

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
