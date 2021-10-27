class ParkingFloorController:
    def __init__(self, parking_floor_service):
        self.parking_floor_service = parking_floor_service

    def assigned_vehicle(self, gate):
        ticket = self.parking_floor_service.assign_vehicle(gate)
        return ticket

    def free_spot(self, spot):
        self.parking_floor_service.free_spot(spot)

    def add_floor(self, floor):
        pass
