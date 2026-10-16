class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
current = head
while current is not None:
    print(current.data)
    current = current.next