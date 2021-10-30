from parkinglot.services.display_board_service import DisplayBoardService
from parkinglot.models.floor import Floor
import threading
from parkinglot.exceptions import (spot_full_exception)


class ParkingFloorService:
    def __init__(self, floor_id):
        self.parking_floor = Floor()
        self.parking_floor.set_id(floor_id)
        self.display_board = DisplayBoardService()
        self.__lock = threading.Lock()

    def assign_vehicle(self, gate, spot_type):
        try:
            self.__lock.acquire()
            if self.is_free(spot_type):
                spot = self.parking_floor.available_spots[spot_type.name].pop()
                self.decreament_available_spot(spot_type)
            else:
                raise spot_full_exception.SpotFullException(f'{spot_type.name} Spot is Full.')
        finally:
            self.__lock.release()

    def is_free(self, spot_type):
        return self.parking_floor.get_available_spot_type_counts(spot_type) > 0

    def get_floor(self):
        return self.parking_floor

    def update_display_board(self):
        available_spot_display_message = self.display_board.show_display_message(
            self.get_floor().get_available_spot_counts())
        return available_spot_display_message

    def add_spot(self, spot):
        self.parking_floor.add_spot(spot)

    def increament_available_spot(self, spot):
        self.parking_floor.increament_available_spot(spot)

    def decreament_available_spot(self, spot):
        self.parking_floor.decreament_available_spot(spot)
