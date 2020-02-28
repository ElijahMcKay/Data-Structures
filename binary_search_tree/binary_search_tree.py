from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    """
    Notes:
    Each node also has to be a binary search tree

    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        """ 
        compare root node
        if lesser go to left child
        if greater or = to to right child
        if no child on that side, insert
        else try again starting from the child on appropriate side (recursion)
        """
        # creating a variable for whatever new node will be so we can return it
        new_node_tree = None
        # if curr tree val less than or equal to inserted val
        if self.value <= value:
            # and the .right node already exists, we have to keep going
            if self.right:
                # so we recursively call self.right.insert with the given value
                return self.right.insert(value)
            # if right node doesn't exist, create it
            else:
                self.right = BinarySearchTree(value)
                # assigning this var so we can return what we just created
                new_node_tree = self.right

        # if curr tree val greater than or equal to inserted val
        elif self.value >= value:
            # and the .left node already exists, we have to keep going
            if self.left:
                # so we recursively call self.left.insert with the given value
                return self.left.insert(value)
            # if left node doesn't exist, create it
            else:
                self.left = BinarySearchTree(value)
                # assigning this var so we can return what we just created
                new_node_tree = self.left

        return new_node_tree


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        """
        look at root, if root is it, return
        if value is less than node, go left and repeat.  If no left child, return none
        if value is >= node, go right and repeat.  If no left child, return none
        """
        # once we have it, return
        if self.value == target:

            return True

        #otherwise, carry on
        else:
            # if target is larger
            if self.value < target:
                # and there is nowhere else to search
                if not self.right:
                    # return None
                    return None

                # recursively call the contains() function to continue searching
                return self.right.contains(target)

            # if target is smaller
            else:
                # and there is nowhere else to search
                if not self.left:
                    # return none
                    return None

                # recursively call the contains() function to continue searching
                return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        """
        keep going right until no more right
        """
        # if we can't go right anymore
        if not self.right:
            # return the current value, bc it's the largest
            return self.value

        # if we can keep going right, recursively call getmax to the right
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call function on current node
        if self.value:
            cb(self.value)

        # call recursively call for_each if right node exists
        if self.right:
            # not returning this, because we want to function to keep going
            self.right.for_each(cb)

        # call recursively call for_each if left node exists
        if self.left:
            # not returning this, because we want to function to keep going
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):

        if self.left:
            # don't need an input node bc we print everything in this tree from low to high regardless of the order
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal


    def bft_print(self, node):
        """
        Iterative approach notes from lecture
        Make a queue
        add root to queue
        while queue.length > 0
        immediately pop root and save to a temp var (temp = queue.dequeue()) - with a queue, popping doesn't have to happen immediately
        Do the thing
        if temp.left add to queue
        if temp.right add to queue
        """
        # instantiating queue and adding initial node
        level_queue = Queue()
        level_queue.enqueue(node)

        # while the queue has stuff in it
        while level_queue.size > 0:
            # removing current node and save it as current node
            current_node = level_queue.dequeue()

            # printing each current node
            print(current_node.value)

            # if there is a node to the right, also add that to queue
            if current_node.right:
                level_queue.enqueue(current_node.right)

            # if there is a node to the right, also add that to queue
            if current_node.left:
                level_queue.enqueue(current_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        """
        Iterative approach notes from lecture
        Make a stack
        add root to stack
        while stack.length > 0
        immediately pop root and save to a temp var (temp = stack.pop())
        Do the thing
        if temp.left add to stack
        if temp.right add to stack
        """
        # instantiating stack
        level_stack = Stack()
        # pushing initial node to stack
        level_stack.push(node)

        # while something is in the stack
        while level_stack.len() > 0:
            # doing this after when enter loop, otherwise it will be 0 and it won't start the loop
            current_node = level_stack.pop()
            print(current_node.value)

            # if there is a node to the right, push that onto the stack
            if current_node.right:
                level_stack.push(current_node.right)

            # if there is a node to the left, push that onto the stack
            if current_node.left:
                level_stack.push(current_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node=None):

        print(self.value)

        if self.left:
            # don't need an input node bc we print everything in this tree from low to high regardless of the order
            self.left.pre_order_dft()

        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):

        if self.left:
            # don't need an input node bc we print everything in this tree from low to high regardless of the order
            self.left.post_order_dft()

        if self.right:
            self.right.post_order_dft()

        print(self.value)


# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# print(bst.in_order_print(bst))