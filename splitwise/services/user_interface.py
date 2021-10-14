from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def add_user(self, id, first_name, last_name):
        pass
