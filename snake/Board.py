from typing import List
from snake.Cell import Cell
from random import randint
from snake.enums.CellTypeEnum import CellTypeEnum


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells: List[List[Cell]] = [[Cell(row, col) for col in range(cols)] for row in range(rows)]

    def generate_food(self):
        while True:
            row, col = randint(0, self.rows - 1), randint(0, self.cols - 1)
            cell: Cell = self.cells[row][col]
            if cell.get_type() == CellTypeEnum.EMPTY:
                cell.set_type(CellTypeEnum.FOOD)
                return
