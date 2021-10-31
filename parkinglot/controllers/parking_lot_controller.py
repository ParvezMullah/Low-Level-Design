class ParkingLotController:
    def __init__(self, parking_lot_service):
        self.parking_lot_service = parking_lot_service

    def issue_ticket(self, parking_floor_controller_obj, gate, spot_type):
        ticket = self.parking_lot_service.assigned_vehicle(
            parking_floor_controller_obj, gate, spot_type)
        return ticket

    def close_ticket(self, parking_floor_controller_obj, spot):
        self.parking_lot_service.free_spot(
            parking_floor_controller_obj, spot)

    def add_floor(self, floor):
        self.parking_lot_service.add_floor(floor)
