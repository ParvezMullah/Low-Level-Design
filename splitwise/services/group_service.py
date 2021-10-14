from splitwise.services.group_interface import GroupInterface
from splitwise.models.group import Group


class GroupService(GroupInterface):
    def __init__(self):
        self.groups = dict()

    def add_group(self, id, users):
        group = Group()
        group.set_id(id)
        group.set_users(users)
        self.groups[id] = group
        return group
