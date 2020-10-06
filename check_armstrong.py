def check_armstrong_number(input_num):
    temp = input_num
    rev = 0
    while input_num > 0:
        digit = input_num % 10
        rev = rev + digit**3
        input_num = input_num // 10
    if rev == temp:
        return True
    else:
        return False

print(check_armstrong_number(234))
