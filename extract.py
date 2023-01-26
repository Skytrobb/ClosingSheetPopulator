import pdfplumber
import re
import sys
import argparse

from datetime import datetime
from write import update_value
from get_table import get_table_dict


parser = argparse.ArgumentParser(description='extract from pdf and put it in a spreadsheet')
parser.add_argument('--pdf', default="./purchaseAgreement.pd",
                    help='location of the purchaseAgreement')
parser.add_argument('--sheet', default="1dJVtKrP1GD15_ZQE-7FrtMFTAKUIosT80HhQqToPBE0", help="google sheet ID, found in url")


args = parser.parse_args()
pdf_location=args.pdf
sheet_id = args.sheet
print(pdf_location, sheet_id)

date_mapping = {
    "C9": [13, 0],
    "C10": [13, 1],
    "C11": [13, 2],
    "D9": [10, 0],
    "D10": [10, 1],
    "D11": [10, 2],
    "B5": [7, 0], # this would be the closing value but something is wrong with the cell
    "B13": [6, 1],
    "B14": [6, 0],
}


def get_date_from_page (page, datePosition):
    with pdfplumber.open(pdf_location) as pdf:
        first_date = pdf.pages[page]
        text = first_date.extract_text()
        remove_underscores = text.replace('_', '')

        match = re.findall(r'\d{2}/\d{2}/\d{4}', remove_underscores)
        # date = datetime.strptime(match.group(), '%m/%d/%Y').date()

        # result = re.findall(date_pattern, remove_underscores)
        
    try:
      date = match[datePosition]
    except IndexError:
      print("thats weeohd")
      return "date not found"

    return date

# my_value = get_date_from_page(6, 0)

# update_value("B13", "USER_ENTERED", my_value)

def create_update_value_map(mapping=date_mapping):
    # get table map values and combine it with the page map values
    update_map = {}
    for cell in mapping:
        page = mapping[cell][0]
        date_position = mapping[cell][1]
        update_map[cell] = get_date_from_page(page, date_position)
    
    full_dict = get_table_dict()
    print(update_map.update(full_dict))
    print(update_map)
    return update_map
        
def update_values_with_map():
    values = create_update_value_map()
    for cell in values:
        print(cell, values[cell])
        update_value(cell, "USER_ENTERED", values[cell], sheet_id)

update_values_with_map()


