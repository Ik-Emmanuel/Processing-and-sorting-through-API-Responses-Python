"""
import requests

url = 'www.retailprices.com/v1/updates'

r = requests.get(url)

sample_resp = r.json()
"""

#Sample response of items with different suppliers and different prices
sample_resp = [
      {'gtin': '123', 'price': 3.12, 'supplier': 'AH'},
      {'gtin': '123', 'price': 3.13, 'supplier': 'Jumbo'},
      {'gtin': '124', 'price': 2.40, 'supplier': 'AH'},
      {'gtin': '124', 'price': 1.50, 'supplier': 'AH'},
      {'gtin': '124', 'price': 1.40, 'supplier': 'AH'},
      {'gtin': '125', 'price': 3.00, 'supplier': 'AH'},
      {'gtin': '125', 'price': 2.40, 'supplier': 'AH'},
      {'gtin': '126', 'price': 3.09, 'supplier': 'jumbo'},
      {'gtin': '127', 'price': 3.07, 'supplier': 'AH'},
      {'gtin': '124', 'price': 2.49, 'supplier': 'AH'},
      {'gtin': '123', 'price': 1.90, 'supplier': 'AH'},
      {'gtin': '124', 'price': 2.67, 'supplier': 'AH'},
      {'gtin': '126', 'price': 4.90, 'supplier': 'AH'},
      {'gtin': '124', 'price': 8.49, 'supplier': 'AH'},
      {'gtin': '123', 'price': 3.90, 'supplier': 'AH'},
      {'gtin': '124', 'price': 6.67, 'supplier': 'AH'},
      {'gtin': '126', 'price': 0.90, 'supplier': 'MX'},
      {'gtin': '120', 'price': 0.90, 'supplier': 'MX'},
      
    ]

#This will contain the final list of items filtered for lowest prices
final_lowest_prices = []

#get item identification number of unique items from response list
items_identification_number = [i['gtin'] for i in sample_resp]

#get unique items from response list 
unique_items = list(set(items_identification_number))


def get_same_items(id:str)-> list:
    ''' 
    This function takes an identification number 
    and returns all items with same identification number within a list 
    '''
    same_items = []
    for item in sample_resp:
        if item['gtin'] == id:
            same_items.append(item)
    return same_items


def get_lowest_price_item(itemlist:list)->dict:
    '''
    This function takes a list of similar items, identifies and retruns 
    an item with the least price 
    '''
    price_list = [i['price'] for i in itemlist]
    min_price = min(price_list)
    for item in itemlist:
        if item['price'] == min_price:
            return item

for item in unique_items:
    same_items = get_same_items(item)
    lowest_price = get_lowest_price_item(same_items)
    final_lowest_prices.append(lowest_price)

print(final_lowest_prices)


"""
'final_lowest_price' which is a list of dict items,  will contain a list of items from the sample_response with the lowest prices ready to be written to a database and shared with the client
"""
    
