"""
Definition:
    It provides an interface for base class to create an object.
    It also gives flexiblity for child classes to modify the
    type of objects that will be created.
    Diagram : https://refactoring.guru/images/patterns/diagrams/factory-method/example.png?id=67db9a5cb817913444ef
"""
from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


class WebButton(Button):
    def render(self):
        print("rendering WebButton")

    def on_click(self):
        print("on_click on WebButton")


class WindowsButton(Button):
    def render(self):
        print("rendering WindowsButton")

    def on_click(self):
        print("on_click on WindowsButton")


class Dialog(ABC):

    def render(self):
        button = self.create_button()
        button.on_click()
        button.render()

    @abstractmethod
    def create_button(self):
        pass


class WebDialog(Dialog):
    def create_button(self):
        return WebButton()


class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()


def read_configuration_file():
    from random import randint
    PLATFORMS = ["windows", "web"]
    return dict(platform=PLATFORMS[randint(0, len(PLATFORMS) - 1)])


if __name__ == "__main__":
    configs = read_configuration_file()
    dialog = None
    platform = configs.get('platform')
    if platform == "windows":
        dialog = WindowsDialog()
    elif platform == "web":
        dialog = WebDialog()
    else:
        raise Exception("Unknown Platform")
    dialog.render()
