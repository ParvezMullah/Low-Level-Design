from parkinglot.models.parking_spots import (
    compact_parking_spot, handicap_parking_spot, large_parking_spot)
from parkinglot.constants.parking_spot_enum import ParkingSpotEnum
from parkinglot.models.parking_spots import (
    handicap_parking_spot, compact_parking_spot, large_parking_spot)


class ParkingSpotService:
    def __init__(self, spot_type):
        self.spot = self.get_parking_spot_obj(spot_type)
        print(f"created: {self.spot.spot_type}")

    def get_parking_spot_obj(self, spot_type):
        switcher = {
            ParkingSpotEnum.handicap: handicap_parking_spot.HandicapParkingSpot,
            ParkingSpotEnum.compact: compact_parking_spot.CompactParkingSpot,
            ParkingSpotEnum.large: large_parking_spot.LargeParkingSpot,
        }
        return switcher[spot_type](spot_type)

    def assign_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle

    def deassign_vehicle(self):
        self.assigned_vehicle = None

    def is_free(self):
        return self.assigned_vehicle is None

    def get_spot_type(self):
        return self.spot.spot_type.name

    def get_spot_obj(self):
        return self.spot
