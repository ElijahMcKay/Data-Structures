Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

2. What is the runtime complexity of `dequeue`?

3. What is the runtime complexity of `len`?

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(1)

2. What is the runtime complexity of `ListNode.insert_before`? O(1)

3. What is the runtime complexity of `ListNode.delete`? O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(n)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(n)

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(n) - we have to iterate through LL to find the node to delete

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?  While both being O(n) runtime, delete will still perform better in most cases.  Array.splice() reassigns all subsequent indices after the value you want to splice, so it will have to iterate through a large part of the array almost regardless how quickly you can access that random index (which arrays can do in constant time). Delete just has to iterate until it finds the node to delete, and then change the references to and from that node, functionally deleting it.