from caching.cache.policies.policy import Policy
from caching.algorithms.doubly_linked_list import DoublyLinkedList
from caching.algorithms.exceptions.invalid_element_exception import InvalidElementException
from caching.algorithms.exceptions.no_such_element_exception import NoSuchElementException


class LruPolicy(Policy):
    def __init__(self):
        self.ddl = DoublyLinkedList()
        self.mapper = dict()

    def access_key(self, key):
        existing_element = self.mapper.get(key)
        if existing_element:
            self.ddl.dettach_node(existing_element)  
        self.mapper[key] = self.ddl.add_element_last(key)

    def evict_key(self):
        first_node = self.ddl.get_first_node()
        self.ddl.dettach_node(first_node)
        return first_node.key
