from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError

    def display_board(self):
        print(f"{self.get_description()} : {self.get_price()}")


class BasicPizza(Pizza):
    def get_description(self):
        return "Pizza"

    def get_price(self):
        return 100


class ExtraCheesePizza(Pizza):
    def __init__(self, pizze):
        self.pizza = pizze

    def get_description(self):
        return self.pizza.get_description() + " Extra Cheese"

    def get_price(self):
        return self.pizza.get_price() + 20


class ExtraChickenPizza(Pizza):
    def __init__(self, pizze):
        self.pizza = pizze

    def get_description(self):
        return self.pizza.get_description() + " Extra Chicken"

    def get_price(self):
        return self.pizza.get_price() + 40


if __name__ == "__main__":
    extra_chicken_cheese_pizza = ExtraChickenPizza(
        ExtraCheesePizza(BasicPizza()))
    extra_chicken_cheese_pizza.display_board()
    print("\n")
    extra_cheese_pizza = ExtraCheesePizza(BasicPizza())
    extra_cheese_pizza.display_board()