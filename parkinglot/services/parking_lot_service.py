from parkinglot.models.parking_lot import ParkingLot


class ParkingLotService:
    def __init__(self):
        self.parking_lot = ParkingLot()

    def assigned_vehicle(self, parking_floor_controller_obj, gate, spot_type):
        parking_floor_controller_obj.assign_vehicle(gate, spot_type)

    def add_floor(self, floor):
        self.parking_lot.add_floor(floor)

    def get_floor(self, floor_id):
        return self.parking_lot.get_floor(floor_id)
