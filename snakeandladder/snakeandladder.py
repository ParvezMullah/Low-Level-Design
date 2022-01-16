import enum
from collections import deque
from random import randint


class CharacterType(enum.Enum):
    ladder = 0
    snake = 1


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Character:
    def __init__(self, start, end, type):
        self.start = start
        self.end = end
        self.type = type

    def get_start_position(self):
        return self.start

    def get_end_position(self):
        return self.end

    def get_type_name(self):
        return self.type.name


class Dice:
    def __init__(self, faces):
        self.faces = faces

    def roll_dice(self):
        return randint(0, self.faces)


class SnakeAndLadder:
    def __init__(self, board_size, players, number_of_snakes, number_of_ladders, dice):
        self.board_size = board_size
        self.players = deque(players)
        self.number_of_snakes = number_of_snakes
        self.number_of_ladders = number_of_ladders
        self.dice = dice
        self.board = [None]*(board_size+1)
        self.winners = []
        self.set_snakes()
        self.set_ladders()
        self.players_positions = self.get_players_initial_position()

    def get_players_initial_position(self):
        players_position = []
        for _ in range(len(self.players)):
            players_position.append(0)
        return deque(players_position)

    def play(self):
        print("#"*20, "Playing", "#"*20)
        while len(self.players) > 1:
            print("*"*40)
            current_player = self.players.popleft()
            current_player_position = self.players_positions.popleft()
            current_face_value = self.dice.roll_dice()
            current_player_new_position = current_player_position + current_face_value
            print(f"Current Player : {current_player}, Current Position: {current_player_position}, Dice Value : {current_face_value},  New Position : {current_player_new_position}",)
            if current_player_new_position <= self.board_size:
                character_at_position = self.board[current_player_new_position]
                if character_at_position:
                    print(' '*20,character_at_position.get_type_name().upper())
                    current_player_new_position = character_at_position.get_end_position()
            if current_player_new_position == self.board_size:
                self.winners.append(current_player)
                print(f"{current_player} has won and come {len(self.winners)}")
                print("*"*40)
                continue
            elif current_player_new_position > self.board_size:
                self.players_positions.append(current_player_position)
            else:
                self.players_positions.append(current_player_new_position)
            self.players.append(current_player)
            print("*"*40)

    def get_winner(self):
        return self.winners

    def set_snakes(self):
        print("*"*20, "Setting Snakes", "*"*20)
        count = 0
        while count < self.number_of_snakes:
            start = randint(1, self.board_size-1)
            if self.board[start] != None:
                continue
            end = randint(1, start)
            if self.board[end] != None:
                continue
            snake = Character(start, end, CharacterType.snake)
            self.board[start] = snake
            count += 1
            print(start, end)
        print("*"*60)

    def set_ladders(self):
        print("*"*20, "Setting Ladders", "*"*20)
        count = 0
        while count < self.number_of_ladders:
            start = randint(1, self.board_size-1)
            if self.board[start] != None:
                continue
            end = randint(start, self.board_size)
            if self.board[end] != None:
                pass
            ladder = Character(start, end, CharacterType.ladder)
            self.board[start] = ladder
            count += 1
            print(start, end)
        print("*"*60)


if __name__ == '__main__':
    number_of_players = int(input('Please Enter a number of players. : '))
    players = []
    for _ in range(number_of_players):
        name = input('Enter the player name.: ')
        player = Player(name)
        players.append(player)
    board_size = int(input('Please enter the board size.: : '))
    number_of_snakes = int(input('Please Enter the number of snakes. : '))
    number_of_ladders = int(input('Please Enter the number of ladders. : '))
    number_of_dice_faces = int(
        input('Please Enter the number of dice faces. : '))
    dice_obj = Dice(number_of_dice_faces)
    snake_and_ladder_obj = SnakeAndLadder(
        board_size, players, number_of_snakes, number_of_ladders, dice_obj)
    snake_and_ladder_obj.play()
    # snake_and_ladder_obj = SnakeAndLadder(
    #     20, [Player("Parvez"), Player("Atif"), Player("Aairah")], 2, 2, Dice(6))
    # snake_and_ladder_obj.play()
