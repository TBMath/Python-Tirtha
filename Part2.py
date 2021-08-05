def fizz_buzz(input):
    if input % 5 or 3 == 0:
        fb = "FizzBuzz"
    if input % 3 == 0:
        fb = "Fizz"
    elif input % 5 == 0:
        fb = "Buzz"
    else:
        fb = f"{input}"
    return fb
    print(fizz_buzz(5))
