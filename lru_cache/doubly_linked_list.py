"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value 
        self.prev = prev # having both pointers tells us doubly linked list
        self.next = next

    def __str__(self):
        return f"{self.value}"
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

        return self


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        # isn't usually required, just using this to play around and understand this better
        self.node = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    
    def __str__(self):
        return f"{self.node}"


    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if not self.head and not self.tail:  #i.e. this list is empty
            self.head = new_node
            self.tail = new_node # this new node is going to be both the head and tail
        else:
            # the new head's next node is equal to the current head
            new_node.next = self.head
            # the current head's previous node equals our new head
            self.head.prev = new_node
            # we define this last because if we don't, we lose our references and thus the values.  Similar to having to use a temp variable when doing swaps
            self.head = new_node

        return new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)

        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if not self.head and not self.tail:  #i.e. this list is empty
            self.head = new_node
            self.tail = new_node # this new node is going to be both the head and tail
        else:
            # the new tail's prev node is equal to the current tail
            new_node.prev = self.tail
            # the current tail's next node equals our new tail
            self.tail.next = new_node
            # we define this last because if we don't, we lose our references and thus the values.  Similar to having to use a temp variable when doing swaps
            self.tail = new_node

        return new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)

        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1

        # if LL is empty 
        if not self.head and not self.tail:
            # TODO error handling
            return

        # if head and tail
        if self.head == self.tail: # if there is only 1 node
            #just removing all pointers
            self.head = None
            self.tail = None

        # if head
        elif self.head == node:
            self.head = self.head.next
            node.delete()

        # if tail
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()

        # otherwise
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        
        max_value = self.head.value
        current = self.head

        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.next
        
        return max_value
