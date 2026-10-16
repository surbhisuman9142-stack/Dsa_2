class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head.next.next
if has_cycle(head):
    print("cycle detected")
else:
    print("no cycle detected")