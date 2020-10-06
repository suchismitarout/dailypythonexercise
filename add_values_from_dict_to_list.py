def add_dict_values_into_a_list(dict1):
    set1 = set()
    for i in dict1.values():
        set1.add(i)
    print(list(set1))


add_dict_values_into_a_list(
    {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54})
