from unittest import TestCase
from snake.Game import Game
from snake.enums.DirectionEnum import DirectionEnum
from snake.enums.CellTypeEnum import CellTypeEnum


class TestGame(TestCase):
    def setUp(self) -> None:
        self.rows = 5
        self.cols = 5
        self.game: Game = Game(self.rows, self.cols)
        self.game.board.generate_food()

    def test_game(self):
        for _ in range(self.rows - 1):
            self.game.update()
            self.assertFalse(self.game.is_game_over)
        self.game.update()
        self.assertTrue(self.game.is_game_over)

    def test_game_direction_change(self):
        for _ in range(self.rows - 1):
            self.game.update()
            self.assertFalse(self.game.is_game_over)
        self.game.direction = DirectionEnum.DOWN
        self.game.update()
        self.assertFalse(self.game.is_game_over)

    def reset_food(self):
        for cell_rows in self.game.board.cells:
            for cell in cell_rows:
                if cell.cell_type == CellTypeEnum.FOOD:
                    cell.set_type(CellTypeEnum.EMPTY)

    def test_food_eaten(self):
        self.assertEqual(1, len(self.game.snake.snake_cells))  # initial size of snake
        for col in range(self.cols - 1):
            self.reset_food()
            self.game.board.cells[0][col + 1].set_type(CellTypeEnum.FOOD)
            self.game.update()
            self.assertEqual(col + 2, len(self.game.snake.snake_cells))
