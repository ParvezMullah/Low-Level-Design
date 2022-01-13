class Player:
    def __init__(self, name):
        self.name = name


class TicTacToe:
    def __init__(self, board_size, players):
        self.players = players
        self.board_size = board_size
        self.board = self.get_board()
        self.players_contributions = [1, -1]
        self.scores = self.get_scores()
        self.diagonal_scores = 0

    def get_board(self):
        return [[-1 for _ in range(self.board_size)]
                for _ in range(self.board_size)]

    def get_scores(self):
        return [[0 for _ in range(self.board_size)] for _ in range(2)]

    def play(self):
        move_count = 0

        while move_count < self.board_size * self.board_size:
            player_number = move_count % 2
            row, column = map(int, (input(f"{self.players[move_count%2].name} Enter row and column: ").split(' ')))
            if self.is_valid_move(row, column):
                if self.move(player_number, row, column):
                    return self.players[player_number]
                move_count += 1
            else:
                print("Invalid Move")
        return None

    def move(self, player_number, row, column):
        self.board[row][column] = player_number
        current_player_contribution = self.players_contributions[player_number]
        self.scores[0][row] += current_player_contribution
        self.scores[1][column] += current_player_contribution
        if row == column:
            self.diagonal_scores += current_player_contribution
        is_winner = self.board_size in (
            abs(self.scores[0][row]), abs(self.scores[1][column]), abs(self.diagonal_scores))
        return is_winner

    def is_valid_move(self, row, col):
        return 0 <= row < self.board_size and \
            0 <= col < self.board_size and \
            self.board[row][col] == -1


if __name__ == '__main__':
    board_size = int(input("Enter Board Size: "))
    first_player_name = input("Enter first player's name: ")
    first_player_obj = Player(first_player_name)
    second_player_name = input("Enter second player's name: ")
    second_player_obj = Player(second_player_name)
    tic_tac_toe_obj = TicTacToe(
        board_size, [first_player_obj, second_player_obj])
    winner = tic_tac_toe_obj.play()
    if winner:
        print(f"Winner : {winner.name}")
    else:
        print("Draw")
