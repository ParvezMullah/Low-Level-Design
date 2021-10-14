from abc import ABC, abstractmethod


class BillInterface(ABC):
    @abstractmethod
    def add_bill(self, id, group_id, amount, paid_by, contributions):
        pass
