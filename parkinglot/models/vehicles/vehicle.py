class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.color = None
        self.number = None

    def get_vehicle_type(self):
        return self.vehicle_type

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number
