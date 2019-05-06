import BubbleSort as bs

lst = []
size = eval(input('Enter the size of the list: '))
for i in range(size):
    n = int(input('Enter the number: '))
    lst.append(n)
print('Before sorting list is: ', lst)
bs.Bubsort(lst)
print('After sorting list is: ', lst)
