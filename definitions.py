import re

def region_code(url):
     pattern = r"/(\d+)$"

     match = re.search(pattern, url)

     if match:
      extracted_number = match.group(1)
      return extracted_number
     else:
        print("No Region found.")
         

def stateORregion(url):
      region_id = region_code(url)
      if re.search(r'#map/details/', url):
        return f"https://rivalregions.com/#map/details/{region_id}"
      elif re.search(r'#state/details/', url):
        return f"https://rivalregions.com/#state/details/{region_id}"
      else:
        return "No valid url", 
    

def gold_checker( arg: str) -> tuple:
   amount = int(re.sub(r'\D', '', arg))
   amount = amount * 10
   print(f" gold checker amount: {amount}")


   if amount >= 1000:
      print("Recharging gold, wait.")
      return True, amount
   else:
      print("No need for recharge")
      return False, amount
  
    
   
   
