from collections import defaultdict


class Floor:
    def __init__(self):
        self.id = id
        self.available_spots = defaultdict(list)
        self.available_spots_count = defaultdict(int)

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_available_spot_type_counts(self, spot_type):
        return self.available_spots_count[spot_type.name]

    def get_available_spot_counts(self):
        return self.available_spots_count

    def add_spot(self, spot):
        self.available_spots[spot.get_spot_type()].append(spot)

    def increament_available_spot(self, spot):
        self.available_spots_count[spot.get_spot_type()] += 1

    def decreament_available_spot(self, spot):
        self.available_spots_count[spot.name] -= 1
