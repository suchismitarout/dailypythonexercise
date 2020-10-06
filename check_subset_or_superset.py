def check_subset_or_superset(set1,set2):

    print("First Set is subset of Second Set -", set1.issubset(set2))
    print("Second Set is subset of First Set -", set2.issubset(set1))
    print("First Set is superset of Second Set -", set1.issuperset(set2))
    print("Second Set is a superset of First Set -", set2.issuperset(set1))
    if set1.issubset(set2):
        set1.clear()
    if set2.issubset(set1):
        set2.clear()

    print(set1)
    print(set2)


print(check_subset_or_superset({57, 83, 29}, {67, 73, 43, 48, 83, 57, 29}))