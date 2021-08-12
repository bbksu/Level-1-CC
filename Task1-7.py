def combine(list1=None, list2=None):
    if list2 is None:
        list2 = [1, 2, 3]
    if list1 is None:
        list1 = [11, 22, 33, 44]
    l1 = len(list1)
    l2 = len(list2)

    list3 = ["#"] * (l1 + l2)

    list3[::2] = list1
    list3[1::2] = list2
    return list3
