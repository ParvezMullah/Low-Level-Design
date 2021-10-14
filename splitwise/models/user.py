class User:
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return f" {self.id} {self.first_name} {self.last_name}"
