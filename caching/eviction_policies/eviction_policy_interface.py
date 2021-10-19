from abc import ABC, abstractmethod


class EvictionPolicyInterface(ABC):
    @abstractmethod
    def key_accesed(self, key):
        pass

    @abstractmethod
    def key_full(self):
        pass
