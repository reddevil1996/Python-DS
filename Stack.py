class Stack:
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        if not self.list:
            return -1
        else:
            return self.list.pop()

    def top(self):
        if not self.list:
            return -1
        else:
            return self.list[-1]

    def display(self):
        return self.list


s = Stack()
print("******HEY YOU ARE USING STACK LETS DO SOME FUN******")
ch = 0
while 1:
    print('1. PUSh')
    print('2. POP')
    print('3. TOP ELEMENT')
    print('4. DISPLAY')
    print('5. EXIT')
    ch = int(input("Enter your choice: "))
    if ch == 1:
        n = eval(input("Enter the element, you want to push in stack: "))
        s.push(n)
    elif ch == 2:
        n = s.pop()
        if n == -1:
            print("Stack is empty!!")
        else:
            print("The popped element is: ", n)
    elif ch == 3:
        n = s.top()
        if n == -1:
            print("Stack is empty!!")
        else:
            print("The top element of stack is: ", n)
    elif ch == 4:
        print("Stack elements are: ")
        print(s.display())
    else:
        print("Thanks for using now BYE BYE!!")
        break

