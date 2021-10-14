from abc import ABC, abstractmethod


class GroupInterface(ABC):
    @abstractmethod
    def add_group(self, id, users):
        pass
