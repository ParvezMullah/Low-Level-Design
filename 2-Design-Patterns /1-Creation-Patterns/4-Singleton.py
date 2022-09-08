"""
Definition :
    It ensures that a class has only one instance, 
    while proving a global access point to this instance.
"""


def singelaton(my_class):
    instances = {}

    def create_obj(*args, **kwargs):
        if my_class not in instances:
            instances[my_class] = my_class(*args, **kwargs)
        return instances[my_class]
    return create_obj


@singelaton
class DataBase:
    def __init__(self):
        print("I will be called only once.")


db = DataBase()
print(db)
db = DataBase()
print(db)
db = DataBase()
print(db)


"""
Applications
1. Database object shared in different part of the code.
2. when you need stricter control over global variables.
"""
