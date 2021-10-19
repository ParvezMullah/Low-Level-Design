from sys import path
path.append("/Users/parvezmullah/Documents/Low-Level-Design")

from caching.eviction_storage.eviction_storage_doubly_linked_list import EvictionStorageDoublyLinkedList
from caching.eviction_policies.lru_policy import LRUPolicy
from caching.cache_services.cache_service import CacheService
from caching.controllers.cache_controller import CacheController

eviction_storage_doubly_linked_list_obj = EvictionStorageDoublyLinkedList()
lru_policy_obj = LRUPolicy(eviction_storage_doubly_linked_list_obj)
cache_serice_obj = CacheService()
capacity = 5

lru_cache = CacheController(cache_serice_obj, lru_policy_obj, capacity)

lru_cache.put("user1", 1)
lru_cache.put("user2", 2)
lru_cache.put("user3", 3)
lru_cache.put("user4", 4)
lru_cache.put("user5", 5)
lru_cache.get("user1")
lru_cache.put("user6", 6)
print(lru_cache.current_capacity, lru_cache.cache_service.dict)
