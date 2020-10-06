def odd_even_in_a_range(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            print(i, "EVEN")
        elif i % 2 != 0:
            print(i, "ODD")


odd_even_in_a_range(3)



