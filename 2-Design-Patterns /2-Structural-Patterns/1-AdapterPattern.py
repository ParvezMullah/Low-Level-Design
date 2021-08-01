"""
Definition:
    It allows incompetible interfaces to collaborate. 

Note: We have achieve it by multiple inheritance or composition.
"""


class Target:
    def request(self):
        print("Target: The default target's behavior.")


class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adaper(Target, Adaptee):
    def request(self):
        return self.specific_request()[::-1]


def client_code(target):
    print(target.request())


if __name__ == "__main__":
    # direct call in unusual
    target = Adaptee()
    print(target.specific_request())
    print("#"*20)

    # via adapter is making meaningful
    target = Adaper()
    client_code(target)

