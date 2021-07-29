try:
    range_num = int(input('How many number do you want to add? '))
    total = 0
    for add in range(range_num):
        nums = int(input('Number: '))
        check_1 = nums/nums
        total += nums
    check = range_num/range_num
    stop = (print(total))


except (ZeroDivisionError):
    print("You can't add zero numbers")
except ValueError:
     print("Enter a number.")