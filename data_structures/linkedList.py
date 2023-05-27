class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        return None

    def insert(self, data):
        if self.head == None:
            head = Node(data)
