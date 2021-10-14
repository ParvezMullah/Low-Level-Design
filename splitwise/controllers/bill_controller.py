class BillController:
    def __init__(self, bill_service):
        self.bill_service = bill_service

    def add_bill(self, id, group_id, amount, paid_by, contributions):
        bill = self.bill_service.add_bill(
            id, group_id, amount, paid_by, contributions)
        return bill
