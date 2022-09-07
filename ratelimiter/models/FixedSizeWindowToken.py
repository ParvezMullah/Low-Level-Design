class FixedSizeWindowModel:
    def __init__(self, start_time_stamp, requests_allowed, request_window_duration_in_seconds):
        self.__start_time_stamp = start_time_stamp
        self.__requests_allowed = requests_allowed
        self.__request_window_duration_in_seconds = request_window_duration_in_seconds

    def is_time_window_exceeded(self, request_time_stamp):
        return (request_time_stamp - self.get_start_time_stamp()) > self.get_request_window_duration_in_seconds()

    def is_request_valid(self, request_time_stamp):
        return self.__requests_allowed > 0

    def get_start_time_stamp(self):
        return self.__start_time_stamp

    def get_requests_allowed(self):
        return self.__requests_allowed

    def set_requests_allowed(self, requests_allowed):
        self.__requests_allowed = requests_allowed

    def get_request_window_duration_in_seconds(self):
        return self.__request_window_duration_in_seconds

    def decrement_requests_allowed(self):
        self.set_requests_allowed(self.get_requests_allowed() - 1)
