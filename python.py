class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


singleLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singleLinkedList.head = node1
singleLinkedList.head.next = node2
singleLinkedList.tail = node2

print(singleLinkedList.head.next)
print(node1 )