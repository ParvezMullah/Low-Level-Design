"""
Definition:
    All the classes should be open for extension and closed for modification.
    We can achieve it by making interface and feature will be in the form of class.
    make object of the new classes. No if else or switch.
"""
from abc import ABC, abstractmethod


class SendLog(ABC):
    @abstractmethod
    def process_log(self):
        pass


class EmailLog(SendLog):
    def process_log(self, log):
        print(f"Email ", log)


class NotifyLog(SendLog):
    def process_log(self, log):
        print(f"Notification ", log)


class PrintLog(SendLog):
    def process_log(self, log):
        print(f"Print ", log)


class LogCalories:
    def __init__(self, calory_tracker):
        self.calory_tracker = calory_tracker

    def log_calory_surplus(self):
        log = f"Max calories Exceeded. Max Calories Set : {self.calory_tracker.max_calories}, Current Calories : {self.calory_tracker.current_calories}, Surplused by : {self.calory_tracker.current_calories - self.calory_tracker.max_calories}"
        self.send_log(log)

    def log_catory_deficit(self):
        log = f"Now you are in calories deficit. Max Calories Set : {self.calory_tracker.current_calories}, Current Calories : {self.calory_tracker.current_calories}, Deficited By : {self.calory_tracker.max_calories - self.calory_tracker.current_calories}"
        self.send_log(log)

    def send_log(self, log):
        for logger in self.calory_tracker.loggers:
            logger.process_log(log)


class CaloryTracker:
    def __init__(self, max_calories, loggers=tuple()):
        self.current_calories = 0
        self.max_calories = max_calories
        self.loggers = loggers

    def is_calories_surplus(self):
        return self.current_calories > self.max_calories

    def add_calories(self, calories):
        self.current_calories += calories
        if self.is_calories_surplus():
            log_calories_obj = LogCalories(self)
            log_calories_obj.log_calory_surplus()

    def subtract_calories(self, calories):
        is_calories_surplus_before = self.is_calories_surplus()
        self.current_calories -= calories
        is_calories_surplus_now = self.is_calories_surplus()
        if is_calories_surplus_before and not is_calories_surplus_now:
            log_calories_obj = LogCalories(self)
            log_calories_obj.log_catory_deficit()

    def reset_calories(self):
        self.current_calories = 0


calory_tracker = CaloryTracker(
    2500, (EmailLog(), NotifyLog(), PrintLog()))
calory_tracker.add_calories(1500)
calory_tracker.add_calories(1500)
calory_tracker.subtract_calories(600)


"""
1. Now if we want to add any logger then we need to make 
that logger class and add object while creating CaloryTracker object.
2. Hence No need to modify any other classes
"""
