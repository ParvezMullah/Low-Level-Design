from logger.enums.LogLevelEnum import LogLevelEnum
from logger.helper.LogSubject import LogSubject
from logger.handlers.BaseHandler import BaseHandler

class Logger:
    def __init__(self, log_subject: LogSubject, log_handler: BaseHandler):
        self.log_subject = log_subject
        self.log_handler = log_handler

    def debug(self, message):
        self.handle_log(LogLevelEnum.DEBUG, message)

    def info(self, message):
        self.handle_log(LogLevelEnum.INFO, message)

    def warning(self, message):
        self.handle_log(LogLevelEnum.WARNING, message)

    def error(self, message):
        self.handle_log(LogLevelEnum.ERROR, message)

    def fatal(self, message):
        self.handle_log(LogLevelEnum.FATAL, message)

    def handle_log(self, log_level, message):
        self.log_handler.handle_log(log_level, message, self.log_subject)
