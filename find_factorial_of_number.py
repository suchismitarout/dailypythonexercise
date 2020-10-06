def find_factorial(input_number):
    fact = 1
    while input_number > 0:
        fact = fact * input_number
        input_number -= 1

    return fact


print(find_factorial(3))

fac = 1
n = 3
for i in range(1,n+1):
    fac = fac * i
print(fac)
