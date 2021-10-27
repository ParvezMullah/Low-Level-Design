from parkinglot.services.display_board_service import DisplayBoardService
class ParkingFloorService:
    def __init__(self, parking_floor):
        self.parking_floor = parking_floor
        self.display_board = DisplayBoardService()

    def assigned_vehicle(self, gate):
        pass

    def free_spot(self, spot):
        pass
