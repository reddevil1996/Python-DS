class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insertion(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def printlist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="")
            current_node = current_node.next

    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                print("Item found")
                return True
            n = n.next
        print("item not found")
        return False

    def bub_sort_link_change(self):
        end = None
        while end != self.head:
            r = p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.next = q.next
                    q.next = p
                    if p != self.head:
                        r.next = q
                    else:
                        self.head = q
                    p, q = q, p
                r = p
                p = p.next
            end = p


l = LinkedList()

num = int(input("How many elements would you like to add:  "))
for i in range(num):
    data = int(input("Enter data items: "))
    l.insertion(data)

print("Linked list is: ", end="")
l.printlist()

element = int(input("\nEnter the element you have to search: "))
l.search_item(element)
print("After sorting linked list is: ")
l.bub_sort_link_change()
l.printlist()
