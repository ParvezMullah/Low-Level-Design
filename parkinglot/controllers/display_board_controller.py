from parkinglot.services.display_board_service import DisplayBoardService


class DisplayBoardController:
    def __init__(self, display_board=DisplayBoardService()):
        self.display_board = display_board

    def show_display_message(self, available_spots_count):
        return self.display_board.show_display_message(available_spots_count)
