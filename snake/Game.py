from snake.Board import Board
from snake.Snake import Snake
from snake.enums.DirectionEnum import DirectionEnum
from snake.exceptions.InValidDirectionException import InValidDirectionException
from snake.enums.CellTypeEnum import CellTypeEnum
from snake.Cell import Cell


class Game:
    def __init__(self, rows, cols):
        self.board: Board = Board(rows, cols)
        self.snake: Snake = Snake(self.board.cells[0][0])
        self.direction = DirectionEnum.RIGHT
        self.is_game_over = False

    def update(self):
        if not self.is_game_over:
            try:
                next_cell: Cell = self.get_next_cell()
            except IndexError:
                self.is_game_over = True
                return
            if self.snake.is_crashing(next_cell):
                self.is_game_over = True
            else:
                is_food_cell = next_cell.cell_type == CellTypeEnum.FOOD
                self.snake.move(next_cell)
                if is_food_cell:
                    self.snake.grow()
                    self.board.generate_food()

    def get_next_cell(self):
        row, col = self.snake.head.row, self.snake.head.col
        if self.direction == DirectionEnum.RIGHT:
            col += 1
        elif self.direction == DirectionEnum.TOP:
            row -= 1
        elif self.direction == DirectionEnum.DOWN:
            row += 1
        elif self.direction == DirectionEnum.LEFT:
            col -= 1
        else:
            raise InValidDirectionException("Direction is Invalid.")
        return self.board.cells[row][col]
