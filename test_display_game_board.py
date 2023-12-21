from unittest import TestCase
import game


class TestDisplayGameBoard(TestCase):
    def test_display_game_board(self):
        rows = 3
        columns = 3
        character = {"Location": [1, 2]}
        boss = {"Location": [2, 1]}
        actual = game.display_game_board(rows, columns, character, boss)
        expected = "[ ][ ][ ]"
        "[ ][ ][B]"
        "[ ][@][ ]"
        self.assertEqual(print(expected), actual)
