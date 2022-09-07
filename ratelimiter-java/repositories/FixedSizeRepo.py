from collections import defaultdict
from ratelimiter.requestcounts import FixedSizeCount


class FixedSizeRepo:

    def __int__(self):
        self.api_usages = dict()

    def get_usage(self, user_id):
        return self.api_usages.get(user_id)

    def set_usage(self, user_id, fixed_size_count):
        self.api_usages[user_id] = fixed_size_count
