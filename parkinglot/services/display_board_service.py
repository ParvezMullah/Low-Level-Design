class DisplayBoardService:
    def show_display_message(self, available_spots_count):
        free_space_message_list = []
        for spot_type, free_spots in available_spots_count.items():
            free_space_message_list.append(f"{spot_type} : {free_spots}")
        return '\n'.join(free_space_message_list)
