class ParkingSpot:
    def __init__(self, spot_type):
        self.spot_type = spot_type
        self.assigned_vehicle = None

    def assign_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle

    def deassign_vehicle(self):
        self.assigned_vehicle = None

    def is_free(self):
        return self.assigned_vehicle is None

    def get_spot_type(self):
        return self.spot_type.name
