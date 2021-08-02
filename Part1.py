from pprint import pprint
products = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 12),
]
sorted_products = [products[1] for x in products[2]]
pprint(sorted_products)