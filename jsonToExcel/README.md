# Covvert the JSON to Excel via Python

This Python script generates JSON contained file in the following sample format to Excel file. The generated Excel file will be in having headers as keyName and Text Respectively. You can run the following two commands to generate the excel file.

1. Without filename parameter. This approach you just need to replace the sample.json file with your data\
```python3 jsonToExcel.py```

2. With filename parameter. This approach you can run the script with desire file without replacing the sample.json file\
```python3 jsonToExcel.py filename=content.json```

## sample.json file with Associative Array

{
    "hello": "Hello",
    "goodbye": "Goodbye",
    "thank_you": "Thank you",
    "yes": "Yes",
    "no": "No"
}

## Sample languagedata.xlsx excel sheet Preview generated after running the python script 

| keyName    | text         |
|------------|--------------|
| hello      | Hello        |
| goodbye    | Goodbye      |
| thank_you  | Thank you   |
| yes        | Yes           |
| no         | No            |

