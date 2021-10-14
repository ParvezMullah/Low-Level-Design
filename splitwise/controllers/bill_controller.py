class BillController:
    def __init__(self, bill_service):
        self.bill_service = bill_service

    def add_bill(self, id, group_id, amount, paid_by, contributions):
        bill = self.bill_service.add_bill(
            id, group_id, amount, paid_by, contributions)
        return bill

    def get_user_balance(self, user_id):
        balance = 0
        for bill in self.bill_service.bills.values():
            if bill.get_paid_by() == user_id:
                balance += bill.get_amount()
            balance -= bill.get_contributions().get(user_id, 0)
        return balance
