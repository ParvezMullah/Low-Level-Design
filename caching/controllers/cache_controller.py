class CacheController:
    def __init__(self, cache_service, cache_eviction_policy, capacity):
        self.cache_service = cache_service
        self.cache_eviction_policy = cache_eviction_policy
        self.capacity = capacity
        self.current_capacity = 0

    def put(self, key, value):
        is_new_key = self.cache_service.put(key, value)
        if is_new_key:
            self.current_capacity += 1
            if self.current_capacity == self.capacity + 1:
                key_to_delete = self.cache_eviction_policy.key_full()
                self.cache_service.remove(key_to_delete)
                self.current_capacity -= 1
        self.cache_eviction_policy.key_accesed(key)

    def get(self, key):
        value = self.cache_service.get(key)
        self.cache_eviction_policy.key_accesed(key)
        return value
