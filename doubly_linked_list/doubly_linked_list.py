"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # creating new node to insert
        new_node = ListNode(value, None, None)

        # increasing length of LL
        self.length += 1

        # checking if there is 0 nodes in the LL
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # assigning old heads previous node to new_node
            self.head.prev = new_node
            # assigning the new_node.next to the old head, before we redefign the new head
            new_node.next = self.head
            # assigning new head to new_node
            self.head = new_node

        return new_node




    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):

        old_head = self.head
        self.head = old_head.next

        self.delete(old_head)

        self.length -= 1
        
        return old_head.value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)

        # adding to length
        self.length += 1

        # checking if the LL is empty, making new_node head and tail if true
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            # assigning old tail's next to new_node
            self.tail.next = new_node
            # assigning new tail's prev to old tail
            new_node.prev = self.tail
            # reassigning self.tail to new_node
            self.tail = new_node

        # returning what we added
        return new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):

        value = self.tail.value
        self.delete(self.tail)

        self.length -= 1

        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # capture the node.value to pass to self.addtohead
        value = node.value
        # deleting node in old location, new references happen automatically with self.delete()
        self.delete(node)
        # re-adding this value to head
        self.add_to_head(value)

        # returning new head
        return self.head


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # capture the node.value to pass to self.addtohead
        value = node.value
        # deleting node in old location, new references happen automatically with self.delete()
        self.delete(node)
        # re-adding this value to head
        self.add_to_tail(value)

        # returning new head
        return self.tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # decrement
        self.length -= 1

        # if the LL is empty
        if not self.head and not self.tail:
            return

        # if the LL has 1 item
        elif self.head == self.tail:
            # not sure if I have to specify this or not
            self.head = None
            self.tail = None

        # if the target node is head 
        elif node == self.head:
            self.head = self.head.next
            node.delete()

        # if the target node is the tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()

        # all other cases
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if LL is empty, can't return anything
        if self.head is None:
            return None
        
        # immediately set the max value to the first positions value (the head)
        max_value = self.head.value
        # another value we use to iterate, again starting at the first position
        current = self.head
        
        # looping until we hit the end of the LL, i.e. current no longer has a .next
        while current:
            if current.value > max_value:
                max_value = current.value

            # iterating after loop logic done, equivalent of something like i++
            current = current.next
        
        return max_value
