from logger.observers.BaseObserver import BaseObserver


class FileObserver(BaseObserver):
    def log(self, message):
        print(self.__class__, message)
