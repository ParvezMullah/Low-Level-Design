from caching.eviction_storage.eviction_storage_interface import EvictionStorageInteface
from caching.eviction_storage.doubly_linked_list_node import Node


class EvictionStorageDoublyLinkedList(EvictionStorageInteface):
    def __init__(self):
        self.first = None
        self.last = None
        self.keys = dict()

    def add_node(self, key):
        node = Node(key, self.last, self.first)
        self.keys[key] = node
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def key_accesed(self, key):
        existing_node = self.keys.get(key)
        if existing_node:
            self.keys.pop(key)
            if existing_node.previous:
                existing_node.previous.next = existing_node.next
            else:
                self.first = self.first.next
                self.first.previous = None
        self.add_node(key)

    def key_full(self):
        key_to_delete = self.first.key
        self.keys.pop(self.first.key)
        self.first = self.first.next
        self.first.previous = None
        return key_to_delete
