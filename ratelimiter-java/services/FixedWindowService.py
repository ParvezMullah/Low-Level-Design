from ratelimiter.requestcounts import FixedSizeCount
from ratelimiter.repositories.FixedSizeRepo import FixedSizeRepo
from threading import Thread

class FixedWindowService:
    def __int__(self):
        self.__repo = FixedSizeRepo()
        self.__lock = Thread()

    def get_fixed_window_request_count(self, user_id):
        fixed_size_count = self.__repo.get_usage(user_id)
        if not fixed_size_count:
            self.set_fixed_window_request_count(user_id)
        return self.__repo.get_usage(user_id)

    def set_fixed_window_request_count(self, user_id):
        self.__repo.set_usage(user_id, FixedSizeCount())

    def add_usage(self, user_id, fixed_request_count):
        with self.__lock:
            try:
                fixed_size_count = self.api_usages[user_id]
                fixed_size_count.request_count -= 1
            except KeyError:
                pass
