from sys import path as path
path.append("/Users/parvezmullah/Documents/Low-Level-Design")

from parkinglot.controllers import (
    display_board_controller, parking_floor_controller, parking_lot_controller,
    parking_spot_controller
)
from parkinglot.services import (
    display_board_service, parking_floor_service, parking_lot_service, parking_spot_service)
from parkinglot.exceptions import (spot_full_exception)
from parkinglot.constants import (parking_spot_enum)


def print_seperator(text=""):
    print("#"*15, text, "#"*15)


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
for slot_type in parking_spot_enum.ParkingSpotEnum:
    try:
        parking_lot_controller_obj.issue_ticket(
            parking_floor_controller_obj_1, gate_1, slot_type)
    except spot_full_exception.SpotFullException as e:
        print(e)
print_seperator()

print_seperator("Assigned only compact_spot")
try:
    parking_lot_controller_obj.issue_ticket(
        parking_floor_controller_obj_1, gate_1, parking_spot_enum.ParkingSpotEnum.compact)
except Exception as e:
    print(e)
