from sys import path as path
path.append("/Users/parvezmullah/Documents/Low-Level-Design")


from parkinglot.constants import (parking_spot_enum)
from parkinglot.exceptions import (spot_full_exception)
from parkinglot.services import (
    display_board_service, parking_floor_service, parking_lot_service, parking_spot_service)
from parkinglot.controllers import (
    display_board_controller, parking_floor_controller, parking_lot_controller,
    parking_spot_controller
)

def print_seperator(text=""):
    print("#"*65, text, "#"*65)
    if not text:
        print("\n"*2)


def print_tickets():
    for slot_type in parking_spot_enum.ParkingSpotEnum:
        try:
            parking_lot_controller_obj.issue_ticket(
                parking_floor_controller_obj_1, gate_1, slot_type)
        except spot_full_exception.SpotFullException as e:
            print(e)


parking_floor_service_obj = parking_floor_service.ParkingFloorService(
    floor_id=1)
parking_floor_controller_obj_1 = parking_floor_controller.ParkingFloorController(
    parking_floor_service_obj)
floor_1 = parking_floor_controller_obj_1.get_floor()
parking_spot_controller_obj = parking_spot_controller.ParkingSpotController
compact_spot = parking_spot_service.ParkingSpotService(
    parking_spot_enum.ParkingSpotEnum.compact)
parking_floor_controller_obj_1.add_spot(compact_spot)
parking_floor_controller_obj_1.update_display_board()
gate_1 = None


parking_lot_service_obj = parking_lot_service.ParkingLotService()

parking_lot_controller_obj = parking_lot_controller.ParkingLotController(
    parking_lot_service_obj)

parking_lot_controller_obj.add_floor(floor_1)
print_seperator("All empty slots")
print_tickets()
print_seperator()



parking_lot_controller_obj.close_ticket(parking_floor_controller_obj_1, compact_spot)

print_seperator("Assigned only compact_spot")
print_tickets()
print_seperator()

print_seperator("all empty")
print_tickets()
print_seperator()