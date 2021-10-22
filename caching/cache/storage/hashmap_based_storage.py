from caching.cache.storage.storage import Storage
from caching.cache.exceptions.capacity_full_exception import CapacityFullException
from caching.cache.exceptions.key_not_present_exception import KeyNotPresentException


class HashMapStorage(Storage):
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity

    def is_full(self):
        return self.capacity == len(self.cache)

    def put(self, key, value):
        if self.is_full() and key not in self.cache:
            raise CapacityFullException("Cache is full.")
        self.cache[key] = value

    def get(self, key):
        value = self.cache.get(key)
        if value is None:
            raise KeyNotPresentException(f"{key} is not present in the cache.")
        return value

    def remove(self, key):
        if key not in self.cache:
            raise KeyNotPresentException(f"{key} is not present in the cache. Hence connot remove")
        del self.cache[key]
