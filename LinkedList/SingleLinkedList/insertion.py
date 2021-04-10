class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertOne(self, value, location):
        node = Node(value)

        # create the first node if list is empty
        if self.head is None:
            self.head = node
            self.tail = node
        # else if node is not empty
        else:
            if location == 0:
                node.next = self.head
                self.head = node
            elif location == -1:
                node.next = None
                self.tail.next = node
                self.tail = node
            else:
                temp = self.head
                index = 0
                while index < location-1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                # self.tail = nextNode
                node.next = nextNode
                temp.next = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


node1 = Node(1)
SLinkedList = SLinkedList()
SLinkedList.head = node1
SLinkedList.tail = node1
print([node.value for node in SLinkedList])
print(SLinkedList.head.value)
print(SLinkedList.tail.value)

SLinkedList.insertOne(2, -1)
print([node.value for node in SLinkedList])
print(SLinkedList.head.value)
print(SLinkedList.tail.value)

SLinkedList.insertOne(20, -1)
print(SLinkedList.head.value)
print(SLinkedList.tail.value)
print([node.value for node in SLinkedList])

SLinkedList.insertOne(30, -1)
print([node.value for node in SLinkedList])

SLinkedList.insertOne(21, 1)
print([node.value for node in SLinkedList])

SLinkedList.insertOne(50, -1)
print([node.value for node in SLinkedList])
print(SLinkedList.head.value)
print(SLinkedList.tail.value)

SLinkedList.insertOne(60, 3)
print([node.value for node in SLinkedList])

