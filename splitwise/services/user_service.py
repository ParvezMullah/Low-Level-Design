from splitwise.services.user_interface import UserInterface
from splitwise.models.user import User


class UserService(UserInterface):
    def __init__(self):
        self.users = dict()

    def add_user(self, id, first_name, last_name):
        user = User()
        user.set_id(id)
        user.set_first_name(first_name)
        user.set_last_name(last_name)
        self.users[id] = user
        return user
