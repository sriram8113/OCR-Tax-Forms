# -*- coding: utf-8 -*-
"""1120.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L3PEiV2vWQhne3fQW5O9x_SdyVen2D4G
"""

!pip install fitz

!pip install pytesseract

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

        # Append extracted text to the result
        extracted_text += text

    return extracted_text

# Example usage:
pdf_path = "/content/drive/MyDrive/form_1120_highlighted.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)

extracted_text

new_text = extracted_text[:]

new_text

import re

def extract_details(text):
    details = {}

    # Extract name and employee ID
    start_index = text.find("eerie")
    end_index = start_index
    for i in range(start_index, len(text)):
        if text[i].isdigit():
            end_index = i
            break
    newline_index = text.find("\n", end_index)
    details["name"] = text[start_index+5:end_index].strip()
    details["employee_id"] = text[end_index:newline_index].strip()

    # Extract city
    city_start_index = text.find("(ee instructions).")
    city_end_index = text.find("$", city_start_index)
    details["city"] = text[city_start_index+len("(ee instructions)."):city_end_index].strip()

    # Extract additional detail after the dollar sign until '4 Schedule M-3 attached' or end of text
    dollar_index = text.find("$")
    schedule_index = text.find("4 Schedule M-3 attached", dollar_index)
    if schedule_index != -1:  # If '4 Schedule M-3 attached' is found
        details["Total Assests"] = text[dollar_index+1:schedule_index].strip()
    else:  # If '4 Schedule M-3 attached' is not found, extract until the end of the text
        details["Total Assests"] = text[dollar_index+1:].strip()

    # Define patterns to extract and store values
    patterns = {
        "2 Personal holding co.":"Street_no",
        "Grossreceiptsorsales . . . 2... ee ee la": "Gross_receipts_or_sales",
        "Returns andallowances. . . Be 1b": "Returns_and_allowances",
        "c  1b from line 1a . 1c": "Balance",
        "2 Cost of goods sold (attach ForBalance. Subtract linem 1125-A) . 2": "Cost_of_goods_sold",
        "3 Gross profit. Subtract line 2 from line 1c . 3": "Gross_profit",
        "Total income. Add lines 3 through 10. : 11": "Total_Income" ,
        'G| 12. Compensation of officers (see instructions — attach Form 1125-" -E) 12': "Compensation_of_officers",
        "§ | 13 Salaries and wages (less employment credits) 13" : "Salaries_and_wages",
        "8 | 14 Repairs and maintenance 14": "Repairs_and_maintenance",
        "5 16 Rents 16" : "Rents",
        "2} 18 Interest (see instructions) 18" :"Interest",
        "> | 27 Total deductions. Add lines 12 through 26 27" :"Total_Deductions",
        "8 28 Tarablincome befor net operating ose deduction and pei detections Subtract line 27 fromline 11... | 28" : "Taxable_Income_before_net",
        "| 29a Net operating loss deduction (see instructions) . . . 29a" : "Net_operating_loss_deduction",
        "3 b Special deductions (Schedule C, line24). 2. 2. 2. 2. 2 ek eee 29b": "Special_deductions",
        "z | 30 Taxable income. Subtract line 29c from line 28. See instructions . . 2. . . . . ee ee 30" : "Taxable income",
        "9 Subtotal. Add lines 1 through 8. See instructions for limitations . . . . . . . 4454| instructions":"Subtotal",
        "24 Total special deductions. Add column (c), lines 9 through 22. Enter here andonpagel,line29 . ." : "Total_special_deductions",
        "a Business activity code no. _" : "Business_activity_code_no",
        "1 Cash woe ee": "Cash",
        "15 Total assets": "Total",
        "16 Accountspayable. . . . 2... .": "Accounts_payable",
        "17 Mortgages, notes, bonds payable in less than 1 year": "Mortgages_less_than_1_year",
        "20 Mortgages, notes, bonds payable in 1 year or more": "Mortgages_more_than_1_year",
        "28 Total liabilities and shareholders’ equity 4": "Total_liabilities_shareholders_equity"
    }

    for pattern, key in patterns.items():
        start_index = text.find(pattern)
        newline_index = text.find("\n", start_index)
        value = text[start_index + len(pattern): newline_index].strip()
        details[key] = value

    keys_to_split = ['Cash', 'Accounts_payable', 'Mortgages_less_than_1_year','Mortgages_more_than_1_year', 'Total_liabilities_shareholders_equity']

    for key in keys_to_split:
        # Split the value into two parts
        values = details[key].split()

        # Assign the split values to the appropriate keys
        details[key + '_begin_tax_year'] = values[0]
        details[key + '_end_tax_year'] = values[1]

        # Remove the original key from the dictionary
        del details[key]

    return details

details = extract_details(new_text)
print(details)













pdf_path3 = "/content/drive/MyDrive/form_1120_highlighted.pdf"
extracted_text3 = extract_text_from_pdf(pdf_path3)

new_text3 = extracted_text3[:]
new_text3

import re

def extract_details(text):
    details = {}

    # Define patterns to extract and store values
    patterns = {
        "Grossreceiptsorsales": "Gross_receipts_or_sales",
        "Returns and allowances": "Returns_and_allowances",
        "Cost of goods sold": "Cost_of_goods_sold",
        "Gross profit": "Gross_profit",
        "Total income": "Total_Income" ,
        'Compensation of officers': "Compensation_of_officers",
        "Salaries and wages" : "Salaries_and_wages",
        "Repairs and maintenance": "Repairs_and_maintenance",
        "Rents" : "Rents",
        "Interest" :"Interest",
        "Total deductions" :"Total_Deductions",
        "Tarablincome befor net operating ose deduction and pei detections" : "Taxable_Income_before_net",
        "Net operating loss deduction" : "Net_operating_loss_deduction",
        "Special deductions": "Special_deductions",
        "Taxable income" : "Taxable income",
        "Subtotal":"Subtotal",
        "Total special deductions" : "Total_special_deductions",
        "Business activity code no. _" : "Business_activity_code_no",
        "Cash": "Cash",
        "Total assets": "Total",
        "Accountspayable": "Accounts_payable",
        "Mortgages, notes, bonds payable in less than 1 year": "Mortgages_less_than_1_year",
        "Mortgages, notes, bonds payable in 1 year or more": "Mortgages_more_than_1_year",
        "Total liabilities and shareholders’ equity": "Total_liabilities_shareholders_equity"
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

details_2023 = extract_details(new_text3)
print(details_2023)



pdf_path_2021 = "/content/drive/MyDrive/2.Dummy_1121.pdf"
extracted_text_2021 = extract_text_from_pdf(pdf_path_2021)

new_text_2021 = extracted_text_2021[:]
new_text_2021

details_2021 = extract_details(new_text_2021)
print(details_2021)



pdf_path_2022 = "/content/drive/MyDrive/3.Dummy_1122.pdf"
extracted_text_2022 = extract_text_from_pdf(pdf_path_2022)

new_text_2022 = extracted_text_2022[:]
new_text_2022

details_2022 = extract_details(new_text_2022)
print(details_2022)

