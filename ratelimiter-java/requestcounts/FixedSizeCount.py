import time
from ratelimiter.constants.ThrottleTimeEnum import ThrottleTimeEnum


class FixedSizeCount:
    def __int__(self, throttle_type=ThrottleTimeEnum.MINUTE, initial_time=int(time.time()), request_left=3):
        self.throttle_type = throttle_type
        self.initial_time = initial_time
        self.request_left = request_left
