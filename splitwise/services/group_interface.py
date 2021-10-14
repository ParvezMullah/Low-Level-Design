from abc import ABC, abstractmethod


class GroupInterface(ABC):
    @abstractmethod
    def create_group(self, id, users):
        pass
