def Selsort(list):
    for i in range(len(list)):
        small = i
        for j in range(i + 1, len(list)):
            if list[j] < list[small]:
                small = j
        list[i], list[small] = list[small], list[i]

