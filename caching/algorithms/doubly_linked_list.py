
from caching.algorithms.doubly_linked_list_node import DoublyLinkedListNode
from caching.algorithms.exceptions.invalid_element_exception import InvalidElementException
from caching.algorithms.exceptions.no_such_element_exception import NoSuchElementException


class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = DoublyLinkedListNode(None)
        self.dummy_tail = DoublyLinkedListNode(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def is_empty(self):
        return self.dummy_head.next == self.dummy_tail

    def add_node_at_last(self, node):
        tail_prev = self.dummy_tail.prev
        tail_prev.next = node
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
        node.prev = tail_prev

    def add_element_last(self, element):
        if not element:
            raise InvalidElementException()
        node = DoublyLinkedListNode(element)
        self.add_node_at_last(node)
        return node

    def get_first_node(self):
        first_node = self.dummy_head.next
        if first_node is self.dummy_tail:
            return None
        return first_node

    def dettach_node(self, node):
        if not node:
            raise NoSuchElementException()
        node.prev.next = node.next
        node.next.prev = node.prev

    def iterate(self):
        node = self.dummy_head
        while node:
            print(f"{node.key}", end=" ")
            node = node.next 
        print()
