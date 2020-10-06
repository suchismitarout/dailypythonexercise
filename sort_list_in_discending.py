def sort_in_descending(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] < input_list[j]:
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp
    print(input_list)


sort_in_descending([12, 3, 10, 1, 34, 56, 11])
