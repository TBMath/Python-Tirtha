from pprint import pprint
products = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 12),
]
sorted_products = products.sort(key= lambda sort_by: sort_by[1])
pprint(sorted)