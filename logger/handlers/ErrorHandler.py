from logger.handlers.BaseHandler import BaseHandler
from logger.enums.LogLevelEnum import LogLevelEnum
from logger.helper.LogSubject import LogSubject


class ErrorHandler(BaseHandler):
    def __init__(self):
        self.log_level = LogLevelEnum.ERROR

    def display(self, message, log_subject: LogSubject):
        log_subject.notify_all(self.log_level, message)
