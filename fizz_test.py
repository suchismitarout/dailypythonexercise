def fizz_buzz(number):
    if ((number % 3 == 0) & (number % 5 == 0)):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)


fizz_buzz(12)
