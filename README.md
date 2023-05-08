# Generate Language Files

This Python script generates language files in and JSON formats from an Excel file. The Excel file should have a header row with column names in English and subsequent rows with translated text for each language. This script can help you to include languages to your website efficiently. 

## Installation

1. Install Python 3 from the official website: https://www.python.org/downloads/
2. Install required Python packages by running the following command in the terminal or command prompt:\
```pip install pandas openpyxl```

## Usage

1. Clone or download this repository to your computer.
2. Copy your Excel file to the same directory as the Python scripts.
3. Open the `generatelanguages.py` script and modify the following line to match your Excel file name:

## Excel sheet Preview 

To use this script, you will need to provide an Excel file as shawn below. The Excel sheet should have a header row with the language codes (e.g. "English", "French", "German", "Spanish", etc.) and a second row with the corresponding two-letter language codes (e.g. "en", "fr", "de", "es", etc.). The first column of the sheet should contain a keyName for each translation, and the second column should contain the actual text to be translated. The remaining columns should contain the translations for each language, with each translation corresponding to the key name in the first column.


| keyName    | Text        | English | French | German | Spanish |
|------------|-------------|---------|-----------|------------|-----------|
|            |             | en      | fr        | de         | es        |
| hello      | Hello       | Hello   | Bonjour   | Hallo      | Hola      |
| goodbye    | Goodbye     | Goodbye | Au revoir | Auf Wiedersehen | Adiós |
| thank_you  | Thank you   | Thank you | Merci    | Danke      | Gracias   |
| yes        | Yes         | Yes     | Oui       | Ja         | Sí        |
| no         | No          | No      | Non       | Nein       | No        |


## Resulted JSON file Output

{
  "hello": "Hello",
  "thank_you": "Thank you",
  "yes": "Yes",
  "no": "No"
}

