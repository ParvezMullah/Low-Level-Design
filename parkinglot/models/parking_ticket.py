class ParkingTicket:
    def __init__(self):
        self.id = None
        self.spot_id = None
        self.issued_at = None
        self.paid_at = None
        self.payment_status = None
        self.payment_mode = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_spot_id(self, spot_id):
        self.spot_id = spot_id

    def get_spot_id(self):
        return self.spot_id

    def set_issued_at(self, issued_at):
        self.issued_at = issued_at

    def get_issued_at(self):
        return self.issued_at

    def set_paid_at(self, paid_at):
        self.paid_at = paid_at

    def get_paid_at(self):
        return self.paid_at

    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    def get_payment_status(self):
        return self.payment_status

    def set_payment_mode(self, payment_mode):
        self.payment_mode = payment_mode

    def get_payment_mode(self, payment_mode):
        self.payment_mode = payment_mode
