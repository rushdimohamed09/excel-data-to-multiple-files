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

from utils.file_utils import read_excel_file, create_lang_dictionary
import pandas as pd
import json
import os

# Check if filename parameter was provided
# Read the Excel file into a Pandas dataframe
defaultFileName = 'languageData.xlsx'
df, filename = read_excel_file(defaultFileName)

# Get the language columns from the dataframe
languageColumns = list(df.columns[2:])

# Create folders for each language
parentFolder = "lang"
os.makedirs(parentFolder, exist_ok=True)

# Loop through the dataframe and create a dictionary of dictionaries for each language
langDict = create_lang_dictionary(languageColumns, df)

# Loop through the language dictionary and write the language_code.json file for each language
for lang, langDict in langDict.items():
    fileName = lang.lower() + '.json'
    filePath = os.path.join("lang", fileName)
    
    # Replace double quotes with single quotes in langDict values
    langDict_modified = {key: value.replace('"',"'") for key, value in langDict.items()}
    
    with open(filePath, "w", encoding='utf-8') as f:
        json.dump(langDict_modified, f, ensure_ascii=False, indent=4)
print(f"Language JSON files are successfully completed generating based on {defaultFileName}")
