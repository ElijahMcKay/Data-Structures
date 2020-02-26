from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()


    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # checking to see if the LL is empty
        if not self.isEmpty():
            self.size -= 1
            # self.storage.length -= 1
            return self.storage.remove_from_head()
        # if it is empty, just return
        else:
            return

    def len(self):
        return self.size

    # read an article mentioning the common methods on a stack and isEmpty was mentioned
    def isEmpty(self):
        if self.size == 0:
            return 1
        else:
            return 0


