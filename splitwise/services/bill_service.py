from splitwise.services.bill_interface import BillInterface
from splitwise.models.bill import Bill


class BillService(BillInterface):
    def __init__(self):
        self.bills = dict()

    def add_bill(self, id, group_id, amount, paid_by, contributions):
        bill = Bill()
        bill.set_id(id)
        bill.set_group_id(group_id)
        bill.set_amount(amount)
        bill.set_paid_by(paid_by)
        bill.set_contributions(contributions)
        self.bills[id] = bill
        return bill
