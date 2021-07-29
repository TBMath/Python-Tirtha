def power_squa(numbers):
    numbers = int(numbers)
    return  numbers ** 2


def power_cub(nums):
    nums = int(nums)
    return nums ** 3


num = input('>')
num = int(num)
print(F"Squared: {power_squa(num)}")
print(f"Cubed: {power_cub(num)}")
