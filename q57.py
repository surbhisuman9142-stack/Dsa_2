class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def reverse_linked_list(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
def print_list(head):
        current = head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print("Before reversing:")
print_list(head)

head = reverse_linked_list(head)

print("After reversing:")
print_list(head)