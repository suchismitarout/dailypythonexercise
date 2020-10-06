def delete_ele_from_list_present_in_dict(dict1, list1):
    for i in list1:
        if i not in dict1.values():
            list1.remove(i)
    print(list1)

delete_ele_from_list_present_in_dict({'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97},
                                     [47, 64, 69, 37, 76, 83, 95, 97])
