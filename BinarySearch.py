def binary_search(sorted_list, key):
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if key == sorted_list[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid+1))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1
