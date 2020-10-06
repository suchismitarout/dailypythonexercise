import string


def unique_morse(words_list):
    list1 = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    list2 = list(string.ascii_lowercase)
    dict1 = dict(zip(list2, list1))
    print(dict1)
    list3 = []
    for i in words_list:
        for j in i:
            if j in dict1.keys():
                k = ""
                k += j
            list3.append(k)
    print(list3)


unique_morse(["gin", "zen", "gig", "msg"])
