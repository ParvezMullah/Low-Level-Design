from collections import defaultdict
from logger.enums.LogLevelEnum import LogLevelEnum


class LogSubject:
    def __init__(self):
        self.observers = defaultdict(list)

    def add_observer(self, log_level, observer):
        self.observers[log_level].append(observer)

    def remove_observer(self, log_level, observer):
        try:
            self.observers[log_level].remove(observer)
        except ValueError:
            print(f"log level: {log_level} does not have observer : {observer}")

    def notify_all(self, log_level: LogLevelEnum, message):
        for observer in self.observers[log_level]:
            observer.log(F"{log_level.name} : {message}")
