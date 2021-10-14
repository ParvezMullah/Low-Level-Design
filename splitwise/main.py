from sys import path
path.append("/Users/parvezmullah/Documents/Low-Level-Design")

from splitwise.controllers.bill_controller import BillController
from splitwise.controllers.group_controller import GroupController
from splitwise.controllers.user_controller import UserController
from splitwise.services.bill_service import BillService
from splitwise.services.group_service import GroupService
from splitwise.services.user_service import UserService

if __name__ == '__main__':
    user_service = UserService()
    group_service = GroupService()
    bill_service = BillService()
    user_controller = UserController(user_service)
    group_controller = GroupController(group_service)
    bill_controller = BillController(bill_service)

    user1 = user_controller.add_user(1, "user1_first", "user1_last")
    user2 = user_controller.add_user(2, "user2_first", "user2_last")
    user3 = user_controller.add_user(3, "user3_first", "user3_last")
    user4 = user_controller.add_user(4, "user4_first", "user4_last")

    group1 = user_controller.add_group(1, [user1, user2, user3, user4])
