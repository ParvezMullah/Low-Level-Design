class Group:
    def __init__(self):
        self.id = None
        self.users = []

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_users(self, users):
        self.users = users

    def get_users(self):
        return self.users

    def add_user(self, user):
        if user in self.users:
            raise Exception(f"{user} is an existing member.")
        self.users.append(user)

    def remove_user(self, user):
        if user not in self.users:
            raise Exception(f"{user} is not an existing member.")
        self.users.remove(user)

    def __str__(self):
        return self.id
