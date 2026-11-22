class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)  # Dummy node
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head.next

        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0

        if index > self.size:
            return
        new_node = Node(val)
        current = self.head
        for i in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        current = self.head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1