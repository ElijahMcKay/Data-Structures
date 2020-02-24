from doubly_linked_list import DoublyLinkedList
import unittest

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.cache = DoublyLinkedList()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            # if key is in cache, we need to move it to the front of the cache to show that it is most recently used
            self.cache.move_to_front(self.storage[key])
            # returns value associated with the key
            # print(self.cache[key].value[1])
            return self.storage[key].value[1]
        else:
            # if key doesn't exist in cache, returning None
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key in cache
        if key in self.storage.keys():
            print(self.storage)
            # since this already exists
            # assigning ListNode.value to the new key/val pair
            self.storage[key].value = [key, value]

            # self.storage[key] is going to equal the entire node
            self.cache.move_to_front(self.storage[key])

            # returning the entire node
            return self.storage[key]
        
        else:
            # since this DOESN'T exist
            #   key is going to equal this entire node (which is returned from adding it to the head, 2 birds 1 stone)
            self.storage[key] = self.cache.add_to_head([key, value])

            # if we're at the max size, do all the same things above except
            if self.cache.length > self.limit:
                # capture           returns the value attr of the Node that we removed
                oldest_node = self.cache.remove_from_tail()
                #                   since we saved the ListNode.value as array, index[0] = the key
                #  So we remove the node from the cache by the key that we gave it
                del self.storage[oldest_node[0]] # oldest_node[0] == removed_node.value[0] (i.e the key)
                # this will return the key, deleting node from storage by key

            # returning the entire node that we added
            return self.storage[key]



lru = LRUCache(3)

lru.set('item1', 'a')
lru.set('item2', 'b')
lru.set('item3', 'c')

# lru.set('item2', 'z')
# print(lru.storage['item1'])
# print(lru.storage['item1'])

# print(lru.cache.get('item1'))
# print(lru.cache.get('item2'))

# playing around with tests to try and get a better understanding
# class CacheTests(unittest.TestCase):
#     def setUp(self):
#         self.cache = LRUCache(3)

#     def test_cache_overwrite_appropriately(self):
#         self.cache.set('item1', 'a')
#         self.cache.set('item2', 'b')
#         self.cache.set('item3', 'c')

#         self.cache.set('item2', 'z')

#         self.assertEqual(self.cache.get('item1'), 'a')
#         self.assertEqual(self.cache.get('item2'), 'z')

#     def test_cache_insertion_and_retrieval(self):
#         self.cache.set('item1', 'a')
#         self.cache.set('item2', 'b')
#         self.cache.set('item3', 'c')

#         self.assertEqual(self.cache.get('item1'), 'a')
#         self.cache.set('item4', 'd')

#         self.assertEqual(self.cache.get('item1'), 'a')
#         self.assertEqual(self.cache.get('item3'), 'c')
#         self.assertEqual(self.cache.get('item4'), 'd')
#         self.assertIsNone(self.cache.get('item2'))

#     def test_cache_nonexistent_retrieval(self):
#         self.assertIsNone(self.cache.get('nonexistent'))



# if __name__ == '__main__':
#     unittest.main()
