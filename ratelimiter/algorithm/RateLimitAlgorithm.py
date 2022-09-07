from abc import ABC, abstractmethod


class RateLimitingAlgorithm(ABC):
    @abstractmethod
    def is_request_allowed(self, user_id, request_timestamp):
        pass
