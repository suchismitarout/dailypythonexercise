def remove_intersection_from_sets(input_set1,input_set2):
    intersect_ele = input_set1.intersection(input_set2)
    print(intersect_ele)
    for i in intersect_ele:
        input_set1.remove(i)
    print(input_set1)



remove_intersection_from_sets({65, 42, 78, 83, 23, 57, 29}, {67, 73, 43, 48, 83, 57, 29})

