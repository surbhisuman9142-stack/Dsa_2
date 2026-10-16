class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def remove_value(head,target):
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            break
        current = current.next
    return dummy.next
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head = remove_value(head,10)
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")