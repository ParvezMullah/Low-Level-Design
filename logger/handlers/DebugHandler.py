from logger.handlers.BaseHandler import BaseHandler
from logger.enums.LogLevelEnum import LogLevelEnum
from logger.helper.LogSubject import LogSubject


class DebugHandler(BaseHandler):
    def __init__(self):
        self.log_level = LogLevelEnum.DEBUG

    def display(self, message, log_subject: LogSubject):
        log_subject.notify_all(self.log_level, message)
