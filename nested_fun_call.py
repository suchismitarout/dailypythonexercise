def addition(a, b):
    print("addition:", a + b)
    subtraction(a, b)


def subtraction(a, b):
    print("subtraction: ", a - b)
    division(a, b)


def division(a, b):
    print("division: ", a // b)
    return multiplication(a, b)


def multiplication(a, b):
    print("multiplication: ", a * b)


# addition(12, 2)


# def hello_world():
#     return addition(10, 2)
#
#
# hello_world()


def greetings():
    res = addition(15, 5)
    print(res)


greetings()
