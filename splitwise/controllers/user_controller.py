class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def add_user(self, id, first_name, last_name):
        user = self.user_service.add_user(id, first_name, last_name)
        return user
