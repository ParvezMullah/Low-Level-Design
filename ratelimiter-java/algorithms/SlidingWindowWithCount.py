from RateLimitingAlgorithm import RateLimitingAlgorithm
from ratelimiter.ratelimitingrequests import RateLimitingRequest


class SlidingWindowWithCount(RateLimitingAlgorithm):
    def is_request_valid(self, request: RateLimitingRequest) -> bool:
        return False

    def add_request_to_bucket(self, request: RateLimitingRequest) -> None:
        pass
