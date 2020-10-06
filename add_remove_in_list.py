def remove_and_add(input_list):
    for i in range(len(input_list)):
        if i == 4:
            global x
            x = input_list.pop(i)
    input_list.insert(2, x)
    input_list.insert(len(input_list), x)

    print(input_list)
    print(x)


remove_and_add([34, 54, 67, 89, 11, 43, 94])
