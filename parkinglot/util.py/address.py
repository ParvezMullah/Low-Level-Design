class Address:
    def __init__(self):
        self.line1 = None
        self.line2 = None
        self.pincode = None
        self.city = None
        self.state = None
        self.country = None

    def set_line1(self, line1):
        self.line1 = line1

    def get_line1(self):
        return self.line1

    def set_line2(self, line2):
        self.line2 = line2

    def get_line2(self):
        return self.line2

    def set_pincode(self, pincode):
        self.pincode = pincode

    def get_pincode(self):
        return self.pincode

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country
