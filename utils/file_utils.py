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
import ast
import sys

def check_filename(defaultFilename):
    isParameter = False
    filename = defaultFilename

    if len(sys.argv) > 1:
        isParameter = True
        # Check if the filename parameter is provided
        if not sys.argv[1].startswith("filename="):
            raise ValueError("Invalid command-line argument. Please provide as 'filename=excel_filename.xlsx' parameter.")
        filename = sys.argv[1].split('=')[1]
    return isParameter, filename

def read_excel_file(defaultFilename):
    isParameter, filename = check_filename(defaultFilename)

    try:
        return pd.read_excel(filename, header=1), filename
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        if (isParameter):
            print(f"Provided parameter filename : '{filename}' is not found in the current directory,")
            print("Please add the file to the current directory and run the command back!")
        else:
            print(f"Seems like you have mistakenly deleted the '{filename}'")
        sys.exit(1)

def read_json_file(defaultFilename):
    isParameter, filename = check_filename(defaultFilename)

    try:
        with open('jsonToExcel/'+filename, 'r') as f:
            return json.load(f), filename
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        if isParameter:
            print(f"Provided parameter filename : '{filename}' is not found in the current directory, \nPlease add the file to the current directory and run the command back!")
        else:
            print(f"Seems like you have mistakenly deleted the '{filename}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not in a valid JSON format.")
        sys.exit(1)

def read_php_file(defaultFilename):
    isParameter, filename = check_filename(defaultFilename)

    try:
        with open('phpToExcel/'+filename, 'r') as f:
            phpText = f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        if isParameter:
            print(f"Provided parameter filename : '{filename}' is not found in the current directory, \nPlease add the file to the current directory and run the command back!")
        else:
            print(f"Seems like you have mistakenly deleted the '{filename}'")
        sys.exit(1)
    
    # Extract the array from the PHP code
    try:
        data = ast.literal_eval(
            phpText.split("return ")[1]
                .split(';')[0]
                .replace('[', '{')
                .replace(']', '}')
                .replace('=>', ':')
            )
        return data, filename
    except (ValueError, IndexError, SyntaxError):
        print(f"Error: {filename} does not contain a valid PHP associative array.")
        sys.exit(1)

def create_lang_dictionary(languageColumns, df):
    langDict = {}

    for lang in languageColumns:
        langDict[lang] = {}
        for index, row in df.iterrows():
            keyName = row[0]
            text = row[lang]
            if pd.notnull(text):
                langDict[lang][keyName] = text
    return langDict
