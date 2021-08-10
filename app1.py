dictionary_1 = [("Tirtha", 10),("Mukta", 38), ("Srimaa",2),("Kumar",40)]
print("Oldest to Youngest")
sorted_products = sorted(dictionary_1, key=lambda item: item[1], reverse=True)
print(sorted_products)
