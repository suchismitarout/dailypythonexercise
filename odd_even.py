def odd_even(list1, list2):
    list3 = []
    for i in range(len(list1)):
        if i % 2 != 0:
            list3.append(list1[i])

    for j in range(len(list2)):
        if j % 2 == 0:
            list3.append(list2[j])

    print(list3)


odd_even([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28])
