import pickle
import pprint
import json
import yaml
from decimal import Decimal

# products = [
#      {'name' : 'Soap', 'quantity': 3, 'price': Decimal('23.50'), 'is_expired': False},
#      {'name': 'Tissue', 'quantity': 6, 'price': Decimal('20.00'), 'is_expired': False},
#      {'name': 'Durex', 'quantity': 2, 'price': Decimal('123.99'), 'is_expired': False},
#      {'name': 'Neck choke', 'quantity': 1, 'price': Decimal('239.99'), 'is_expired': True},
#
# ]
products = [
     {"name" : "Soap", "quantity": 3, "price": 23, "is_expired": False},
     {"name": "Tissue", "quantity": 6, "price": 20, "is_expired": False},
     {"name": "Durex", "quantity": 2, "price":123, "is_expired": False},
     {"name": "Neck choke", "quantity": 1, "price": 239, "is_expired": True},

]
##print(products)
# with open('pickled_object.txt', mode='wb') as file:
#      pickle.dump(products, file)
#
# with open('json_object.txt', mode='w') as file:
#          json.dump(products, file, indent=4)
#
# with open('json_object.txt', mode='r') as file:
#      x = json.load(file)
#      pprint.pprint(x, indent=4)

with open('yaml_object.txt', mode='w') as file:
     yaml.dump(products, file, indent=4)

with open('yaml_object.txt', mode='r') as file:
     x = yaml.load(file, Loader=yaml.Loader)
     print(x)

# with open('pickled_object.txt', mode='rb') as file:
#     x = pickle.load(file)
#     pprint.pprint(x, indent=4)

#print(0.1 + 0.2)
#print(Decimal('0.1') + ('0.2'))


