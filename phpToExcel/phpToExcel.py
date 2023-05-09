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
import ast
import sys

# Check if filename parameter was provided
isParameter = False
if len(sys.argv) > 1:
    isParameter = True
    filename = sys.argv[1].split('=')[1]
else:
    filename = 'sample.php'

# Read the PHP file as text
try:
    with open(filename, 'r') as f:
        php_text = f.read()
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
    if (isParameter):
        print(f"Provided parameter filename : '{filename}' is not found in the current directory, \nPlease add the file to the current directory and run the command back!")
    else:
        print(f"Seems like you have mistakenly deleted the '{filename}'")
    sys.exit(1)

# Extract the array from the PHP code
try:
    data = ast.literal_eval(
        php_text.split("return ")[1]
            .split(';')[0]
            .replace('[', '{')
            .replace(']', '}')
            .replace('=>', ':')
        )
except (ValueError, IndexError, SyntaxError):
    print(f"Error: {filename} does not contain a valid PHP associative array.")
    sys.exit(1)

# Create a new workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Set the header row
ws.append(['keyName', 'text'])

# Add data to the worksheet
for key, value in data.items():
    ws.append([key, value])

# Save the workbook
wb.save('languagedata.xlsx')
print(f"Excel file generated successfully based on {filename}!")
