chicken_nugget = input('What is the price of an item? $')
chicken_nugget = float(chicken_nugget)
number = input('How many of the item do you do you want? ')
put = float(chicken_nugget) * int(number)
if put <= 1.00:
    tax = 0
else:
    tax = put * 0.10
    tax = float(tax)
pull = put + tax
print('That will be  $' + str(pull) + ' including tax')