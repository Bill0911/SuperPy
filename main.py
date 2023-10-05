import argparse
import csv
from datetime import date
current_date = date.now().strftime("%Y-%m-%d")

with open("current.txt", 'w') as date_file:
 
 date_file.write(current_date) 

 


# Do not change these lines.
 __winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def load_data(file_path):
    data = []
    with open (file_path, mode='r', delimiter='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data 



def save_data(file_path, data):
    with open(file_path, mode='w', newline='' ) as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def product_lists(products):
    for product in products:
        print(f'Product name: {product["product_name"]}')


def calculate_inventory(bought_data, sold_data):
    inventory = {}
    for bought_item in bought_data:
        product_id = bought_item["id"]
        product_name = bought_item["product_name"]
        buy_price = float(bought_item["buy_price"])
        expiration_date = date.strptime(bought_item[expiration_date], "%Y-%m-%d")
        sold_item = next((sold for sold in sold_data if sold["bought_id"] == product_id), None)

        if sold_item:
            sell_price = float(sold_item["sell_price"])
            sell_date = date.strptime(sold_item["sell_date"], "%Y-%m-%d")
            if sell_date < expiration_date:
                profit = sell_price - buy_price
            else:
                profit = 0
        else:
            profit = 0 


        if product_name in inventory:
           inventory[product_name]['quantity'] += 1
           inventory[product_name]['total_profit'] += profit

        else:
            inventory[product_name] = {'quantity': 1, 'total_profit': profit}

    return inventory     

def advanced_day(days):
  try:
    with open('current_date.txt', 'r') as date_file:
     current_date = date_file.read()
     current_date = date.now().strptime(current_date, '%Y-%m-%d')
  except FileNotFoundError:
     current_date = date.now()

  
  current_date += timedelta(days=days)

  with open('current_date.txt', 'w') as date_file:
     date_file.write(current_date.strftime('%Y-%m-%d'))
  
  print(f"Time advance: {days}, The current_date is: {current_date.strftime('%Y-%m-%d')}")




     


  

    










    




     


def main():
    pass


if __name__ == "__main__":
    main()
