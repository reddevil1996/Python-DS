def MrgSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        l = list[:mid]
        r = list[mid:]
        MrgSort(l)
        MrgSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                list[k] = l[i]
                i = i + 1
            else:
                list[k] = r[j]
                j = j + 1
            k = k + 1
        while i < len(l):
            list[k] = l[i]
            i = i + 1
            k = k + 1
        while j < len(r):
            list[k] = r[j]
            j = j + 1
            k = k + 1


def printlist(list):
    for i in range(len(list)):
        print(list[i], end="")
    print()
