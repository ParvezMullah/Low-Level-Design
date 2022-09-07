from snake.enums.CellTypeEnum import CellTypeEnum


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col
        self.cell_type: CellTypeEnum = CellTypeEnum.EMPTY

    def set_type(self, cell_type: CellTypeEnum):
        self.cell_type = cell_type

    def get_type(self) -> CellTypeEnum:
        return self.cell_type

    def __str__(self):
        return f"row: {self.row}, col: {self.col}"
