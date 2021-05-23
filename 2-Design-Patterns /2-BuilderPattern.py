"""
Definition :
    Builder pattern lets you construct objects step by step. 
    The builder does not allow other objects to access the product while its being build.

Note: First we build object of builder class then we build main object from builder object.
"""
from __future__ import annotations


class Engine:
    pass


class Seat:
    pass


class Steering:
    pass


class Fuel:
    pass


class AirBag:
    pass


class SunRoof:
    pass


class MusicSystem:
    pass


class CentralLock:
    pass


class CarBuilder:
    engine = None
    seat = None
    steering = None
    fuel = None
    air_bag = None
    sun_roof = None
    music_system = None
    central_lock = None

    def with_engine(self, engine) -> CarBuilder:
        self.engine = engine
        return self

    def with_seat(self, seat) -> CarBuilder:
        self.seat = seat
        return self

    def with_steering(self, steering) -> CarBuilder:
        self.steering = steering
        return self

    def with_fuel(self, fuel) -> CarBuilder:
        self.fuel = fuel
        return self

    def with_air_bag(self, air_bag) -> CarBuilder:
        self.air_bag = air_bag
        return self

    def with_sun_roof(self, sun_roof) -> CarBuilder:
        self.sun_roof = sun_roof
        return self

    def with_music_system(self, music_system) -> CarBuilder:
        self.music_system = music_system
        return self

    def with_central_lock(self, lock) -> CarBuilder:
        self.central_lock = lock
        return self

    def build(self):
        car = Car()
        if not (self.engine and self.seat and self.steering and self.fuel):
            raise Exception("Not all required properties are set.")
        car.engine = self.engine
        car.seat = self.seat
        car.steering = self.steering
        car.fuel = self.fuel
        car.air_bag = self.air_bag
        car.sun_roof = self.sun_roof
        car.music_system = self.music_system
        car.central_lock = self.central_lock
        return car


class Car:
    engine = None
    seat = None
    steering = None
    fuel = None
    air_bag = None
    sun_roof = None
    music_system = None
    central_lock = None

    def builder(self) -> CarBuilder:
        return CarBuilder()


basic_car = Car().builder().with_engine(Engine()).with_seat(
    Seat()).with_steering(Steering()).with_fuel(Fuel()).build()

ha_ha_car = Car().builder().with_engine(Engine()).with_seat(
    Seat()).with_steering(Steering()).with_fuel(Fuel()).with_air_bag(AirBag()).with_sun_roof(SunRoof()).with_music_system(MusicSystem()).with_central_lock(CentralLock()).build()


"""
Applications: 
1. Use the Builder pat­tern to get rid of a “tele­scop­ic constructor.
2. When you want your code to able to create different representations of some product.
"""
