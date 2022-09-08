import unittest
from logger.Logger import Logger
from logger.handlers.DebugHandler import DebugHandler
from logger.handlers.ErrorHandler import ErrorHandler
from logger.helper.LogSubject import LogSubject
from logger.observers.ConsoleObserver import ConsoleObserver
from logger.observers.FileObserver import FileObserver
from logger.enums.LogLevelEnum import LogLevelEnum


class LoggerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.debug_handler = DebugHandler()
        self.error_handler = ErrorHandler()
        self.debug_handler.set_next_handler(self.error_handler)
        self.file_observer = FileObserver()
        self.console_observer = ConsoleObserver()
        self.log_subject = LogSubject()
        self.log_subject.add_observer(LogLevelEnum.ERROR, self.file_observer)
        self.log_subject.add_observer(LogLevelEnum.ERROR, self.console_observer)
        self.log_subject.add_observer(LogLevelEnum.DEBUG, self.console_observer)
        self.logger = Logger(self.log_subject, self.debug_handler)

    def test_error(self):
        # console and file
        self.logger.error("some error")

    def test_debug(self):
        # only console
        self.logger.debug("some debug")


if __name__ == '__main__':
    unittest.main()
