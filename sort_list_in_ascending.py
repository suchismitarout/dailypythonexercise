def sort_in_ascending(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp

    print(input_list)


sort_in_ascending([12, 34, 10, 3, 56, 1, 8])
