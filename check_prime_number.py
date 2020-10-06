def check_prime_number(input_number):
    for num in range(2, input_number):
        if input_number % num == 0:
            print("its not a prime number")
            break
    else:
        print("its a prime number")


check_prime_number(31)
