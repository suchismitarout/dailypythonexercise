def check_balanced_symbols(input_string):
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    new_list = []
    for i in input_string:
        if i in open_list:
            new_list.append(i)
        elif i in close_list:
            position = close_list.index(i)
            if open_list[position] == new_list[len(new_list)-1]:
                new_list.pop()
            else:
                return "Unbalanced"
    if len(new_list) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

print(check_balanced_symbols("{[]{()}}{{{{"))
