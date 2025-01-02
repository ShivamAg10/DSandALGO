class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

# Creating Nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# Creating Nodes to form a linked list
n1.next = n2
n2.next = n3
n3.next = n4

# Printing the linked list
curr = n1
while curr is not None:
    print(curr.data, end="->")
    curr = curr.next
    # print(curr)
print("None")