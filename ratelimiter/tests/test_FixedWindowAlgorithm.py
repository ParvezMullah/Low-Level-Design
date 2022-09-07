from unittest import TestCase
from ratelimiter.algorithm.FixedWindowAlgorithm import FixedWindowAlgorithm
import time


class Test(TestCase):
    def check_valid_cases(self, fixed_window_algorithm: FixedWindowAlgorithm, user_id):
        for _ in range(6):
            self.assertEqual(True, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))

    def test_fixed_window_algorithm_within_window(self):
        user_id = "user_id1"
        fixed_window_algorithm: FixedWindowAlgorithm = FixedWindowAlgorithm(10)
        self.check_valid_cases(fixed_window_algorithm, user_id)
        self.assertEqual(False, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))
        self.assertEqual(False, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))

    def test_fixed_window_algorithm_outside_window(self):
        user_id = "user_id2"
        fixed_window_algorithm: FixedWindowAlgorithm = FixedWindowAlgorithm(10)
        self.check_valid_cases(fixed_window_algorithm, user_id)
        self.assertEqual(False, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))
        self.assertEqual(False, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))
        time.sleep(11)
        self.assertEqual(True, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))
        self.assertEqual(True, fixed_window_algorithm.is_request_allowed(user_id, int(time.time())))
