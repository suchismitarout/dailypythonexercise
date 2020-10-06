def odd_in_odd_even_in_even(input_list):
    odd_index = 1
    even_index = 0
    length = len(input_list)
    new_list = input_list[:]
    for num in input_list:
        if even_index < length and num % 2 == 0:
            new_list[even_index] = num
            even_index += 2
        elif odd_index < length and num % 2 != 0:
            new_list[odd_index] = num
            odd_index += 2
    print(new_list)


odd_in_odd_even_in_even([12, 24, 24, 28, 10, 9])
