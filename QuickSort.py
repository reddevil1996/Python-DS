def QuiSort(list):
    QuikSort(list, 0, len(list)-1)


def QuikSort(list, start, end):
    if start < end:
        p = partition(list, start, end)
        QuikSort(list, start, p-1)
        QuikSort(list, p+1, end)


def partition(list, start, end):
    pivot = list[start]
    i = start + 1
    j = end
    while i < j:
        while i <= j and list[i] <= pivot:
            i = i+1

        while i <= j and list[j] >= pivot:
            j = j-1

        if i < j:
            list[i], list[j] = list[j], list[i]

    list[start], list[j] = list[j], list[start]
    return j


