import InsertionSort as Is

lst = []
size = eval(input('Enter the size of the list: '))
for i in range(size):
    n = int(input('Enter the number: '))
    lst.append(n)
print('Before sorting list is: ', lst)
Is.Inssort(lst)
print('After sorting list is: ', lst)
