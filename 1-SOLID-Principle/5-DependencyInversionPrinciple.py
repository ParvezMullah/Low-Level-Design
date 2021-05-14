"""
definition: 
    High Level classes should not depend upon low level classes.
    Both should depend upon abstraction.
    abstraction should not depend on details.

    Store -------> Payment Processor -------> (
                                            1. PayPal
                                            2. Stripe
                                        )
"""
from abc import ABC, abstractmethod

################################ Violation of DIP ################################


class PaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class Store:
    def __init__(self, user):
        self.user = user

    def purchase(self, quantity):
        stripe = Stripe(self.user)
        stripe.make_payment(quantity*100)


class Stripe(PaymentProcessor):
    def __init__(self, user):
        self.user = user

    def make_payment(self, amount):
        print(f"{self.user} has purchased product(s) of {amount} dollar(s).")


"""
If we want to add Paypal payment mode then we need to modify store class.
"""
# store = Store("Parry")
# store.purchase(1)


################################ Correct way by DIP ################################
class PaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class PayPalPaymentProcessor(PaymentProcessor):
    def make_payment(self, amount):
        print(f"PayPalPaymentProcessor : {amount}")


class StripePaymentProcessor(PaymentProcessor):
    def make_payment(self, amount):
        print(f"StripePaymentProcessor : {amount}")


class Store:
    def __init__(self, user, payment_processor):
        self.user = user
        self.payment_processor = payment_processor

    def purchase(self, quantity, price):
        self.payment_processor.make_payment(quantity*price)


store = Store("Parry", PayPalPaymentProcessor())
store.purchase(2, 20)


store = Store("Parry", StripePaymentProcessor())
store.purchase(3, 30)
