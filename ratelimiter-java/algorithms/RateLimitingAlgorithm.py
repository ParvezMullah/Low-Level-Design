from ratelimiter.ratelimitingrequests import RateLimitingRequest
from abc import ABC, abstractmethod


class RateLimitingAlgorithm(ABC):

    @abstractmethod
    def is_request_valid(self, request: RateLimitingRequest) -> bool:
        pass

    @abstractmethod
    def add_request_to_bucket(self, request: str) -> None:
        pass
