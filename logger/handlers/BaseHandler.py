from abc import ABC, abstractmethod


class BaseHandler(ABC):
    def __init__(self):
        self.next_handler: BaseHandler = None
        self.log_level = None

    def handle_log(self, log_level, message, log_subject):
        if self.log_level == log_level:
            self.display(message, log_subject)
        elif self.next_handler:
            self.next_handler.handle_log(log_level, message, log_subject)

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def get_next_handler(self):
        return self.next_handler

    @abstractmethod
    def display(self, message, log_subject):
        pass
