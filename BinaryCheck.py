import BinarySearch as bs

lst = []
size = eval(input("Enter the size of the list: "))
for n in range(size):
    num = eval(input("Enter the number: "))
    lst.append(num)
lst.sort()
print("After sorting list is: ", lst)
x = eval(input("Enter number to search: "))
bs.binary_search(lst, x)
