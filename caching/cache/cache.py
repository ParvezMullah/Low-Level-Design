from caching.cache.storage.hashmap_based_storage import HashMapStorage
from caching.cache.exceptions.capacity_full_exception import CapacityFullException
from caching.cache.exceptions.key_not_present_exception import KeyNotPresentException
from caching.cache.policies.lru_policy import LruPolicy


class Cache:
    def __init__(self, capacity):
        self.storage = HashMapStorage(capacity)
        self.eviction_policy = LruPolicy()

    def put(self, key, value):
        try:
            self.storage.put(key, value)
            self.eviction_policy.access_key(key)
        except CapacityFullException:
            key_to_evict = self.eviction_policy.evict_key()
            self.storage.remove(key_to_evict)
            self.storage.put(key, value)
        self.eviction_policy.access_key(key)

    def get(self, key):
        value = None
        try:
            value = self.storage.get(key)
            self.eviction_policy.access_key(key)
        except KeyNotPresentException:
            pass
        return value
