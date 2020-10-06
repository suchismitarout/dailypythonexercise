def merge_two_dict(dict1, dict2):
    dict1.update(dict2)
    print(dict1)
    dict3 = {**dict1, **dict2}
    print(dict3)


merge_two_dict({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
