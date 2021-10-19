from caching.cache_services.cache_interface import CacheInterface


class CacheService(CacheInterface):
    def __init__(self):
        self.dict = {}

    def put(self, key, value):
        is_new_key = key not in self.dict
        self.dict[key] = value
        return is_new_key

    def get(self, key):
        return self.dict[key]

    def remove(self, key):
        del self.dict[key]
