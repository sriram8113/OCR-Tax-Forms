# -*- coding: utf-8 -*-
"""1065.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cuMj1DTT-pWTgu_6BCURhf13odLlPilr
"""

pip install fitz

pip install pytesseract

!pip install PyMuPDF

!pip install Pillow

!sudo apt-get install tesseract-ocr

!pip install pytesseract

!pip install PyPDF2

!apt-get install ocrmypdf -q

!pip install pdfplumber -q

import os

import requests
import pdfplumber

!pip install pdf2image pytesseract

"""::;;;  hghjj    hhihjhjhbjbihihihiuhvkufvgilugkuhgldiuqwgdiuw"""

!apt-get install poppler-utils

from pdf2image import convert_from_path
import pytesseract


def extract_text_from_pdf(pdf_path):
    # Convert PDF to list of PIL Image objects
    pages = convert_from_path(pdf_path)

    # Initialize empty string to store extracted text
    extracted_text = ""

    # Iterate through each page and perform OCR
    for page in pages:
        # Perform OCR on the page image
        text = pytesseract.image_to_string(page)

        # Append extracted text to the resu
        extracted_text += text

    return extracted_text

# Example usage:
pdf_path = "/content/1065-1.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)

extracted_text

new_text = extracted_text[:]

new_text

import re

parameters = {
    "2 Cost of goods sold (attach Form 1125-A) 2 ": "Cost of goods sold",
    "o | 3 Gross profit. Subtract line 2 from line 1c . . . 3 ": "Gross profit",
    "| 8 Total income (loss). Combine lines 3 through 7 toe ee ee 8": "Total income (loss)",
    "2 | 41 Repairs and maintenance . rr": "Repairs and maintenance",
    "| 9 Salaries and wages (other than to partners) (less employment credits) . 9 ": "Salaries and wages",
    "g 15 Interest (see instructions). . . Loe soe. | 15": "Interest",
    '£ 16a Depreciation (if required, attach Form 4562). : 16a ': "Depreciation",
    "| 22 Total deductions. Add the amounts shown in the far ‘right column for lines 9 through 21. 22": "Total deductions",
    "_____ 23 _ Ordinary business income (loss). Subtract line 22 from line 8 23": "Ordinary business income (loss)",
    " 1\nNet rental real estate income (loss) (attach Form 8825) . . . . . ..... 2... 2 ": "Net rental real estate income",
    "1 Cash... .... 22. ": "Cash",
    "14 Totalassets. ........, ": "Total assets",
    "15 Accounts payable . ": "Accounts_payable",
    "16 Mortgages, notes, bonds payable nies than 1 year ": "Mortgages, notes, bonds payable in less than 1 year",
    "b Mortgages, notes, bonds payable in 1 year or more .": "Mortgages, notes, bonds payable in 1 year or more",
}

def extract_info(parameters, text):
    details = {}  # Initialize an empty dictionary to store extracted details

    # Define regex patterns for extracting information
    patterns = {
        "Name of partnership": r"Principal business activity\s*\n(.+)",
        "Number, street, and room or suite no.": r"Type Number, street, and room or suite no\..*\n(?:or\s*\|)?(.+)",
        "City or town, state or province, country, and ZIP": r"City or town, state or province, country, and ZIP or foreign postal code\s*\n(.+)",
        "Employer identification number": r"Employer identification number\s*\n(\d+)",
        "Gross receipts or sales": r"1a Gross receipts or sales\s*([0-9,]+)"
    }
    for feature, pattern in patterns.items():
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            # Ensures that a match was found before attempting to access group(1)
            details[feature] = match.group(1).strip() if match.group(1) else "Match found, but group is empty"
        else:
            details[feature] = "No match found"  # Placeholder for no match

    for pattern, key in parameters.items():
        start_index = text.find(pattern)
        newline_index = text.find("\n", start_index)
        value = text[start_index + len(pattern): newline_index].strip()
        details[key] = value

    keys_to_split = ['Cash', 'Accounts_payable', 'Mortgages, notes, bonds payable in less than 1 year',
                     'Mortgages, notes, bonds payable in 1 year or more']

    for key in keys_to_split:
        # Split the value into two parts
        values = details[key].split()

        # Assign the split values to the appropriate keys
        details[key + '_begin_tax_year'] = values[0]
        details[key + '_end_tax_year'] = values[1]

        # Remove the original key from the dictionary
        del details[key]

    return details

# Assuming 'text' contains the entire block of text
extracted_info = extract_info(parameters, new_text)

# Convert to a list of tuples if needed
extracted_info_list = list(extracted_info.items())

extracted_info_list

"""# Extracting Information with Regular Expressions for different years"""

pdf_path1 = "/content/1065-1.pdf"
extracted_text3 = extract_text_from_pdf(pdf_path1)

new_text3 = extracted_text3[:]
new_text3

import re

def extract_details(text):
    details = {}

    # Define patterns to extract and store values
    patterns = {
        "Employer identification number": "Employer_identification_number",
        "Gross receipts or sales": "Gross_receipts_or_sales",
        "Cost of goods sold (attach Form 1125-A)": "Cost_of_goods_sold",
        "Gross profit": "Gross_profit",
        "Total income (loss)": "Total_income_(loss)" ,
        'Repairs and maintenance': "Repairs_and_maintenance",
        "Salaries and wages" : "Salaries_and_wages",
        "Total balance due":"Total_balance_due",
        "Other taxes ":"Other taxes ",
        "Repairs and maintenance": "Repairs_and_maintenance",
        "Depreciation":"Depreciation",
        "Rents" : "Rents",
        "Interest" :"Interest",
        "Total deductions" :"Total_Deductions",
        "Ordinary business income (loss)" : "Ordinary_business_income_loss)",
        "Net rental real estate income" : "Net_rental_real_estate_income",
        "Dividends and dividend equivalents": "Dividends_and_dividend_equivalents",
        "Cash": "Cash",
        "Total assets": "Total",
        "Accountspayable": "Accounts_payable",
        "Loans from partners":"Loans from partners",
        "Mortgages, notes, bonds payable in less than 1 year": "Mortgages_less_than_1_year",
        "Mortgages, notes, bonds payable in 1 year or more": "Mortgages_more_than_1_year",
        "Total liabilities and capital": "Total_liabilities_and_capital",
        "Net income (loss)":"Net_income_(loss)"
    }

    for pattern, key in patterns.items():
      start_index = text.find(pattern)
      if start_index != -1:  # Check if pattern exists
        newline_index = text.find("\n", start_index)
        line = text[start_index:newline_index]
        # Search for numbers with more than 2 digits
        match = re.search(r'\b(\d{3,}(\.\d*)?)\b', line)
        if match:
          value = match.group(1)
        else:
          value = None
        details[key] = value


    return details

details_2023 = extract_details(extracted_text3)

extracted_info_list_2023 = list(details_2023.items())

extracted_info_list_2023

pdf_path2 = "/content/1065-1_2022.pdf"
extracted_text2 = extract_text_from_pdf(pdf_path2)

details_2022 = extract_details(extracted_text2)

extracted_info_list_2022 = list(details_2022.items())

extracted_info_list_2022

pdf_path3 = "/content/1065-1_2021.pdf"
extracted_text4 = extract_text_from_pdf(pdf_path3)

details_2021 = extract_details(extracted_text4)

extracted_info_list_2021 = list(details_2021.items())

extracted_info_list_2021