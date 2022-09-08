from logger.observers.BaseObserver import BaseObserver


class ConsoleObserver(BaseObserver):
    def log(self, message):
        print(self.__class__, message)
