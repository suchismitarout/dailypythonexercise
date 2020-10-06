def check_duplicates(input_list):
    dict1 = {}
    for i in input_list:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    print(dict1)

    for key,value in dict1.items():
        if dict1[key] > 1:
            for i in range(dict1[key]-1):
                input_list.remove(key)

    print(input_list)

check_duplicates([23,14,35,12,14,56])