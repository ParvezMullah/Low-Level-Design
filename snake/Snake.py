from snake.Cell import Cell
from snake.enums.CellTypeEnum import CellTypeEnum
from collections import deque


class Snake:
    def __init__(self, initial_pos: Cell):
        self.head = initial_pos
        self.head.set_type(CellTypeEnum.SNAKE_NODE)
        self.snake_cells = deque([initial_pos])
        self.tail_node = None

    def move(self, next_cell: Cell):
        self.head = next_cell
        self.head.set_type(CellTypeEnum.SNAKE_NODE)
        self.snake_cells.append(self.head)
        self.tail_node: Cell = self.snake_cells.popleft()
        self.tail_node.set_type(CellTypeEnum.EMPTY)

    def grow(self):
        self.snake_cells.append(self.tail_node)
        self.tail_node.set_type(CellTypeEnum.SNAKE_NODE)

    def is_crashing(self, next_cell: Cell):
        return next_cell in self.snake_cells


"""
    >
"""
