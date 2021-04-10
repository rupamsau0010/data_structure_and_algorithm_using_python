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

    # only this traversal func in added
    # rest of all as previous
    def traversal(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # only this search func is added
    # rest of all are same
    def searchElement(self, element):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            count = 0
            while node is not None:
                if node.value == element:
                    print(count)
                count += 1
                node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


node1 = Node(1)
SLinkedList = SLinkedList()
SLinkedList.head = node1
SLinkedList.tail = node1
SLinkedList.insertOne(10, -1)
SLinkedList.searchElement(10)
