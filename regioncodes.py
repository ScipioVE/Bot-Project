import re

def region_code(url):
    pattern = r"/(\d+)$"

    match = re.search(pattern, url)

    if match:
     extracted_number = match.group(1)
     print("Extracted Number:", extracted_number)
     return extracted_number
    else:
        print("No Region found.")
         

