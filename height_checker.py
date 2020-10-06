def height_checker(arr):
    count = 0
    arr1 = arr.copy()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:

                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


    print(arr)
    for i in range(len(arr1)):
        if arr1[i] != arr[i]:
            count += 1
    print(count)








height_checker([1,1,4,2,1,3])
