from sys import path
path.append("/Users/parvezmullah/Documents/Low-Level-Design")

from caching.cache.cache import Cache

capacity = 3
cache = Cache(capacity)
cache.put(1, "parvez")
cache.put(2, "parry")
cache.put(3, "lol")
cache.put(4, "parry")
print(cache.get(1))
