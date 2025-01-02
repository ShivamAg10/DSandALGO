class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

n5 = Node(int(input("Enter a number: ")))
n1.next = n5
n5.next = n2

curr = n1
while curr is not None:
    print(curr.data, end="->")
    curr = curr.next
print("None")