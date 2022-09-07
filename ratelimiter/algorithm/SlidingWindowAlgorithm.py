from ratelimiter.algorithm.RateLimitAlgorithm import RateLimitingAlgorithm
from ratelimiter.models.SlidingWindowToken import SlidingWindowModel
from threading import Lock


class SlidingWindowAlgorithm(RateLimitingAlgorithm):

    def __init__(self, request_window_in_seconds, request_allowed):
        self.request_window_in_seconds = request_window_in_seconds
        self.request_allowed = request_allowed
        self.usage = dict()
        self.__lock = Lock()

    def is_request_allowed(self, user_id, request_timestamp):
        with self.__lock:
            sliding_window_model: SlidingWindowModel = self.get_and_set_usage(user_id)
            sliding_window_model.process_outside_window_requests(request_timestamp)
            if sliding_window_model.is_request_valid(request_timestamp):
                sliding_window_model.add_request(request_timestamp)
                return True
        return False

    def get_and_set_usage(self, user_id):
        try:
            sliding_window_model = self.usage[user_id]
        except KeyError:
            sliding_window_model = SlidingWindowModel(self.request_allowed, self.request_window_in_seconds)
            self.usage[user_id] = sliding_window_model
        return sliding_window_model
