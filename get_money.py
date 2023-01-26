import pdfplumber
import re
import sys

print(sys.argv)
pdf_arg = "./purchaseAgreement.pdf" if len(sys.argv) < 2 else sys.argv[1]
spreadsheet_arg = None if len(sys.argv) < 3 else sys.argv[2]

def get_money(pdf_arg):

  with pdfplumber.open(pdf_arg) as pdf:
    first_date = pdf.pages[3]
    text = first_date.extract_text()
    #remove_underscores = text.replace('_', '')
    
    # print(remove_underscores)
    # print(text)
    # match = re.findall(r'\d{2}/\d{2}/\d{4}', remove_underscores)

get_money(pdf_arg)