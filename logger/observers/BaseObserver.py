from abc import ABC, abstractmethod


class BaseObserver(ABC):

    @abstractmethod
    def log(self, string):
        pass
