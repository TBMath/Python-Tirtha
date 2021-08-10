products = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 12),
]
sorted_products = sorted(products, key=lambda item: item[1])
print(sorted_products)