dictionary_1 = [("Tirtha", 10),("Mukta", 38), ("Srimaa",2),("Kumar",40)]
print("Oldest to Youngest")
sorted_products = sorted(dictionary_1, key=lambda item: item[1], reverse=True)
def pope(input):
    return sorted_products.pop(lambda nums: nums[1])
print(pope("hi"))
