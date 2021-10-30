import threading


def singelaton(cls):
    objects = dict()
    singelaton_lock = threading.Lock()

    def inner_func(*args, **kwargs):
        singelaton_lock.acquire()
        if cls not in objects:
            objects[cls] = cls(*args, **kwargs)
        singelaton_lock.release()
        return objects[cls]
    return inner_func


@singelaton
class ParkingLot:
    def __init__(self):
        self.floors = dict()

    def add_floor(self, floor):
        self.floors[floor.get_id()] = floor

    def get_floor(self, id):
        return self.floors[id]
