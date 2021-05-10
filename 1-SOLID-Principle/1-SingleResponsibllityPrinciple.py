"""
Definition:
    A class should have just one reason to change.
    ie. A class should have only one job.
"""
import enum


class Communication(enum.Enum):
    email = 1
    notication = 2
    show = 3


class SendLog:
    def __init__(self, log):
        self.log = log

    def email_log(self):
        print(f"Email ", self.log)

    def notication_log(self):
        print("Notification ", self.log)

    def print_log(self):
        print("Print ", self.log)


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
        send_log = SendLog(log)
        for mode in self.calory_tracker.communication_modes:
            if mode == Communication.show:
                send_log.print_log()
            elif mode == Communication.email:
                send_log.email_log()
            elif mode == Communication.notication:
                send_log.notication_log()


class CaloryTracker:
    def __init__(self, max_calories, communication_modes=(Communication.show, )):
        self.current_calories = 0
        self.max_calories = max_calories
        self.communication_modes = communication_modes

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
    2500, (Communication.show, Communication.email, Communication.show))
calory_tracker.add_calories(1500)
calory_tracker.add_calories(1500)
calory_tracker.subtract_calories(600)


"""
Violation:
    Current program is violeting the Open/Closed Principle. 
    For e.g if we want to add new log(log in our system) then we would need to
    change send_log method because we need to add one more if/elif to encorporate 
    new log.
    .
"""
