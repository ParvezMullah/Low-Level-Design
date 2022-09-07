from unittest import TestCase
from ratelimiter.algorithm.SlidingWindowAlgorithm import SlidingWindowAlgorithm
import time
from threading import Thread


class SlidingWindowTest(TestCase):
    def setUp(self):
        self.requests_allowed = 5
        self.request_window_in_second = 10
        self.sliding_window_algorithm: SlidingWindowAlgorithm = SlidingWindowAlgorithm(self.request_window_in_second,
                                                                                       self.requests_allowed)

    @staticmethod
    def time():
        return int(time.time())

    def _test_initial_valid_requests(self, user_id):
        for _ in range(self.requests_allowed):
            self.assertEqual(True, self.sliding_window_algorithm.is_request_allowed(user_id, SlidingWindowTest.time()))

    def test_is_request_allowed_with_all_positive(self):
        user_id = "user1"
        self._test_initial_valid_requests(user_id)
        self.assertEqual(False, self.sliding_window_algorithm.is_request_allowed(user_id, SlidingWindowTest.time()))

    def test_is_request_allowed_with_outside_window(self):
        user_id = "user2"
        self._test_initial_valid_requests(user_id)
        self.assertEqual(False, self.sliding_window_algorithm.is_request_allowed(user_id, SlidingWindowTest.time()))
        time.sleep(self.request_window_in_second + 1)
        self._test_initial_valid_requests(user_id)
        self.assertEqual(False, self.sliding_window_algorithm.is_request_allowed(user_id, SlidingWindowTest.time()))

