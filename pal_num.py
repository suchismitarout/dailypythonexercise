def check_pallindrom_num(number):
    temp = number
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10
    if rev == temp:
        print(temp, "is pallindrom")
    else:
        print(temp, "is not pallindrom")


check_pallindrom_num(121)


def check_length_of_number(num):
    temp = num
    count1 = 0
    while num > 0:
        d = num % 10
        num = num // 10
        count1 += 1
    print("length of", temp, "is", count1)


check_length_of_number(24653)
