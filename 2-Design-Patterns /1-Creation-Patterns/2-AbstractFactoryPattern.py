"""
Definition:
    It provides an interface to create objects of related or dependent classes.

Note:  It is similar to Factory method but factory method only create one type of object.
        Abstract factory creates multiple type of objects.
https://refactoring.guru/images/patterns/diagrams/abstract-factory/example.png?id=5928a61d18bf00b04746
"""

from __future__ import annotations

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


class CheckBox(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_select(self):
        pass


class WebCheckBox(CheckBox):
    def render(self):
        print("rendering WebCheckBox")

    def on_select(self):
        print("on_select on WebCheckBox")


class WindowsCheckBox(CheckBox):
    def render(self):
        print("rendering WindowsCheckBox")

    def on_select(self):
        print("on_select on WindowsCheckBox")


class GUI(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class GUIWindow(GUI):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckBox()


class GUIWeb(GUI):
    def create_button(self):
        return WebButton()

    def create_checkbox(self):
        return WebCheckBox()


def read_configuration_file():
    from random import randint
    PLATFORMS = ["windows", "web"]
    return dict(platform=PLATFORMS[randint(0, len(PLATFORMS) - 1)])


if __name__ == "__main__":
    configs = read_configuration_file()
    gui_factory = None
    platform = configs.get('platform')
    if platform == "windows":
        gui_factory = GUIWindow()
    elif platform == "web":
        gui_factory = GUIWeb()
    else:
        raise Exception("Unknown Platform")

    button = gui_factory.create_button()
    button.render()
    checkbox = gui_factory.create_checkbox()
    checkbox.render()


"""
Application : Use the Abstract Fac­to­ry when your code needs to work with var­i­ous fam­i­lies of relat­ed prod­ucts, 
but you don’t want it to depend on the con­crete class­es of those prod­ucts—they might be unknown before­hand or you sim­ply want to allow for future exten­si­bil­i­ty. 
"""
