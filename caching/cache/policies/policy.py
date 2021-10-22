from abc import ABC, abstractmethod


class Policy(ABC):
    @abstractmethod
    def access_key(self, key):
        pass

    @abstractmethod
    def evict_key(self):
        pass
