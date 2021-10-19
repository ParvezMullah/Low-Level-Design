from caching.eviction_policies.eviction_policy_interface import EvictionPolicyInterface


class LRUPolicy(EvictionPolicyInterface):
    def __init__(self, eviction_store):
        self.eviction_store = eviction_store

    def key_accesed(self, key):
        self.eviction_store.key_accesed(key)

    def key_full(self):
        return self.eviction_store.key_full()
