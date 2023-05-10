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
import os

# Check if filename parameter was provided
# Read the Excel file into a Pandas dataframe
defaultFileName = 'languageData.xlsx'
df, filename = read_excel_file(defaultFileName)

# Get the language columns from the dataframe
languageColumns = list(df.columns[2:])

# Create folders for each language
for lang in languageColumns:
    folderName = lang.lower()
    parentFolder = "lang"
    fullFolderPath = os.path.join(parentFolder, folderName)
    if not os.path.exists(fullFolderPath):
        os.makedirs(fullFolderPath)

# Loop through the dataframe and create a dictionary of dictionaries for each language
langDict = create_lang_dictionary(languageColumns, df)

# Loop through the language dictionary and write the custom.php file for each language
for lang, langDict in langDict.items():
    folderName = lang.lower()
    filePath = os.path.join("lang", folderName, "custom.php")

    with open(filePath, "w", encoding='utf-8') as f:
        f.write("<?php\n\nreturn [\n")

        for keyName, text in langDict.items():
            f.write(f'    "{keyName}" => "{text}",\n')

        f.write("];")
        print(f"Successfully completed generating {folderName}/custom.php")