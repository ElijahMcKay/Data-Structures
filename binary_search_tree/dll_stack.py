# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

    # read an article mentioning the common methods on a stack and isEmpty was mentioned
    def isEmpty(self):
        if self.size == 0:
            return 1
        else:
            return 0
