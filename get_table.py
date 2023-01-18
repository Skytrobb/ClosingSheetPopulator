import pdfplumber
from find_date import find_first_date_in_string

def get_table_dict():

      with pdfplumber.open("./purchaseAgreement.pdf") as pdf:
        page = pdf.pages[11]
        table = page.extract_table()
        hoa = table[9]
        nmar = table[10]
        ccr = table[11]

        mapping = {
          "B9": table[3][1].replace(' ', ''),
          "B10": table[3][4].replace(' ', ''),
          "B11": table[3][5].replace(' ', ''),
          "E9": hoa[1].replace(' ', ''),
          "F9": hoa[4].replace(' ', ''),
          "G9": hoa[5].replace(' ', ''),
          "E10": nmar[1],
          "F10": find_first_date_in_string(nmar[4].replace('_', '')),
          "G10": nmar[5],
          "E11": ccr[1],
          "F11": ccr[4],
          "G11": ccr[5],
        }

        return mapping

print(get_table_dict())