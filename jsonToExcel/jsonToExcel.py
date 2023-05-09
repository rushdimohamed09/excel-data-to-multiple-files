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

import openpyxl
import json
import sys

# Check if filename parameter was provided
isParameter = False
if len(sys.argv) > 1:
    isParameter = True
    filename = sys.argv[1].split('=')[1]
else:
    filename = 'sample.json'

# Load the JSON file
try:
    with open(filename, 'r') as f:
        data = json.load(f)
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

# Create a new workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Add the header
sheet["A1"] = "keyName"
sheet["B1"] = "text"

# Add the data
for i, key in enumerate(data.keys()):
    sheet[f"A{i+2}"] = key
    sheet[f"B{i+2}"] = data[key]

# Save the workbook
wb.save('languagedata.xlsx')
print(f"Excel file generated successfully based on {filename}!")
