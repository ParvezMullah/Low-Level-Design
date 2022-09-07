from ratelimiter.algorithm.RateLimitAlgorithm import RateLimitingAlgorithm
from ratelimiter.models.FixedSizeWindowToken import FixedSizeWindowModel
from ratelimiter.exceptions.TimeWindowExceededException import TimeWindowExceededException
from threading import Lock


class FixedWindowAlgorithm(RateLimitingAlgorithm):
    def __init__(self, time_window_in_second):
        self.time_window_in_second = time_window_in_second
        self.usage = dict()
        self.__lock = Lock()

    def is_request_allowed(self, user_id, request_time_stamp):
        fixed_window_model: FixedSizeWindowModel = self.get_fixed_size_window_model(user_id, request_time_stamp)
        if fixed_window_model.is_request_valid(request_time_stamp):
            with self.__lock:
                fixed_window_model.decrement_requests_allowed()
            return True
        return False

    def set_and_get_usage(self, user_id, request_time_stamp):
        fixed_size_window_model = FixedSizeWindowModel(request_time_stamp, 6, self.get_time_window_in_second())
        self.usage[user_id] = fixed_size_window_model
        return fixed_size_window_model

    def get_fixed_size_window_model(self, user_id, request_time_stamp):
        try:
            fixed_size_window_model = self.usage[user_id]
            if fixed_size_window_model.is_time_window_exceeded(request_time_stamp):
                raise TimeWindowExceededException("Time Window Exceeded")
        except (KeyError, TimeWindowExceededException) as e:
            fixed_size_window_model = self.set_and_get_usage(user_id, request_time_stamp)
        return fixed_size_window_model

    def get_time_window_in_second(self):
        return self.time_window_in_second
