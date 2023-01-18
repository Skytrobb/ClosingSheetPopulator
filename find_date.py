import re

def find_first_date_in_string(string):

  match = re.findall(r'\d{2}/\d{2}/\d{4}', string)
  
  return match[0]