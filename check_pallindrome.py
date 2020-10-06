def check_pallindrome_string(input_string):
    new_string = ""
    for i in input_string:
        new_string = i + new_string
    if new_string == input_string:
        return True
    else:
        return False


print(check_pallindrome_string("REACT"))


def check_pallindrome_number(input_number):
    temp = input_number
    result = 0
    while input_number > 0:
        digit = input_number % 10
        result = result * 10 + digit
        input_number = input_number // 10

    if result == temp:
        return True
    else:
        return False

print(check_pallindrome_number(345))