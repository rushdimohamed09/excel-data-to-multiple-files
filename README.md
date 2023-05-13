# Generate Language Files

This Python script generates language files in and JSON/PHP associative array formats from an Excel file. The Excel file should have a header row with column names in English and subsequent rows with translated text for each language. This script can help you to include languages to your website efficiently. 

## Installation

1. Install Python 3 from the official website: https://www.python.org/downloads/
2. Install required Python packages by running the following command in the terminal or command prompt:\
```pip install pandas openpyxl```

## Usage

1. Clone or download this repository to your computer.
2. Copy your Excel file to the same directory as the Python scripts.
3. There are two python scripts in the root folder as `languagesInJson.py` and `languagesInPhp.py` respectively generates languages in JSON format and PHP associative array format:

## Run the command in one of the following approaches 

NOTE: Please run all the commands from the root folder terminal\

(Both `languagesInJson.py` and `languagesInPhp.py` uses the same convention and following example will demonstrates in JSON)\

1. Without filename parameter. This approach you just need to replace the sample.php file with your data\
```python3 languagesInJson.py```

2. With filename parameter. This approach you can run the script with desire file without replacing the sample.php file\
```python3 languagesInJson.py filename=sample.xlsx```

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

## Generate Excel file from JSON/PHP associateive format

Read the following README.md files
1. [Generate from JSON file](./jsonToExcel/README.md)
2. [Generate from PHP file](./phpToExcel/README.md)