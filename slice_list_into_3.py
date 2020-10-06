def slice_rever_list(list1):
    length = len(list1)
    n = length//3
    list_one = []
    list_two = []
    list_three = []
    for i in range(n):
        list_one.append(list1[i])

    print(list_one)



slice_rever_list([11, 45, 8, 23, 14, 12, 78, 45, 89])