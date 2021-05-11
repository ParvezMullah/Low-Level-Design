"""
Definition:
    When extending a class, Remember that you should able to pass object of the subclass
    in place of object of superclass without breaking the client code.

    1. Parameter of the subclass method should match or more abstract than 
    the parameters of the superclass method.
    2. Return type of subclass method should match or subtype of the superclass method.
    3. A method in a subclass should not throw any exception which method of superclass
    is not expected to throw.

We can achieve LSP by redesigning the hierarchy. 
"""

######################## Violation of LSP ########################


class Bird:
    def fly(self):
        print("I can fly!")


class Duck(Bird):
    def quack(self):
        print("I can quack!")


class Penguin(Bird):
    def swim(self):
        print("I can swim!")

    def fly(self):
        raise Exception("I can ot fly!")


def make_bird_fly(bird):
    bird.fly()


# duck = Duck()
# make_bird_fly(duck)
# penguin = Penguin()
# # below line with raise exception. As we cannot make penguin fly.
# make_bird_fly(penguin)


######################## Correct way by following LSP ########################


class FlyingBird:
    def fly(self):
        print("I can fly!")


class Duck(FlyingBird):
    pass


class SwimingBird:
    def swim(self):
        print("I can swim!")


class Penguin(SwimingBird):
    pass


def make_bird_fly(bird):
    bird.fly()


def make_bird_swin(bird):
    bird.swim()


duck = Duck()
make_bird_fly(duck)
penguin = Penguin()
make_bird_swin(penguin)
