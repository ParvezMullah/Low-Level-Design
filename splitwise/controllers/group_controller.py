class GroupController:
    def __init__(self, group_service):
        self.group_service = group_service

    def add_group(self, id, users):
        group = self.group_service.add_group(id, users)
        return group

