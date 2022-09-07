class SlidingWindowModel:
    def __init__(self, requests_allowed, requests_window_in_second):
        self.requests_allowed = requests_allowed
        self.requests_window_in_second = requests_window_in_second
        # self.requests = deque() #add request way
        self.requests = dict()

    def add_request(self, request_timestamp):
        request_consumer = self.requests.get(request_timestamp, 0)
        self.requests[request_timestamp] = request_consumer + 1

    def process_outside_window_requests(self, request_timestamp):
        self.requests = {key: value for key, value in self.requests.items() if
                         request_timestamp - key < self.requests_window_in_second}

    def is_request_valid(self, time_stamp):
        return sum(self.requests.values()) < self.requests_allowed


"""

    def add_request(self, request_timestamp):
        # add request way
        self.requests.append(request_timestamp)

    def process_outside_window_requests(self, request_timestamp):
        # add request way
        while len(self.requests) > 0 and request_timestamp - self.requests[0] > self.requests_window_in_second:
            self.requests.popleft()

    def is_request_valid(self, time_stamp):
        # add request way
        return len(self.requests) < self.requests_allowed
"""
