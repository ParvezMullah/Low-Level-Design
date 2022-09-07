from RateLimitingAlgorithm import RateLimitingAlgorithm
from ratelimiter.ratelimitingrequests import RateLimitingRequest
from ratelimiter.services import FixedWindowService
from time import time
from ratelimiter.constants.TimeDifferenceInSecond import TimeDifferenceInSecond
class FixedSizeWindow(RateLimitingAlgorithm):
    def __int__(self):
        self.fixed_size_window_service = FixedWindowService()

    def is_request_valid(self, request: RateLimitingRequest) -> bool:
        user_id = request.user_id
        fixed_request_count = self.fixed_size_window_service.get_fixed_window_request_count(user_id)
        time_gap = int(time()) - fixed_request_count.initial_time
        if time_gap > TimeDifferenceInSecond.minute:
            self.fixed_size_window_service.set_fixed_window_request_count(user_id)
            fixed_request_count = self.fixed_size_window_service.get_fixed_window_request_count(user_id)
        if fixed_request_count.request_left <= 0:
            return False
        self.fixed_size_window_service.
        return True



    def add_request_to_bucket(self, request: RateLimitingRequest) -> None:
        pass
