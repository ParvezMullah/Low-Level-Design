class ParkingFloorController:
    def __init__(self, parking_floor_service):
        self.parking_floor_service = parking_floor_service

    def assign_vehicle(self, gate, spot_type):
        ticket = self.parking_floor_service.assign_vehicle(gate, spot_type)
        return ticket

    def free_spot(self, spot):
        self.parking_floor_service.free_spot(spot)

    def add_spot(self, spot):
        self.parking_floor_service.add_spot(spot)
        self.parking_floor_service.increament_available_spot(spot)

    def get_floor(self):
        return self.parking_floor_service.get_floor()

    def update_display_board(self):
        available_spot_display_message = self.parking_floor_service.update_display_board()
        print("*"*15, "available spot", "*"*15)
        print(available_spot_display_message)
        print("*"*40)
