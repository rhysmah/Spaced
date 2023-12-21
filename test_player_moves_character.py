from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestPlayerMovesCharacter(TestCase):

    @patch("game.execute_user_choice", return_value="North")
    @patch("game.validate_character_move", return_value=False)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_player_unsuccessfully_moves_character(self, mock_stdout, _mock_execute_user_choice, _mock_validate_move):
        rows = 10
        columns = 10
        character = {"Name": "Emily",
                     "Class": "Engineer",
                     "Rank": "Novice",
                     "Max HP": 15,
                     "Current HP": 15,
                     "Attack": 2,
                     "Hit Chance": 6,
                     "XP": 0,
                     "Location": [0, 0]}
        boss = {"Name": "HAL 8500",
                "Current HP": 23,
                "Attack": 6,
                "Hit Chance": 8,
                "Location": [3, 6]}
        game.player_moves_character(rows, columns, character, boss)
        print_statement = "You're as far North as you can go!\n"
        self.assertEqual(mock_stdout.getvalue(), print_statement)

    @patch("game.execute_user_choice", return_value="South")
    @patch("game.validate_character_move", return_value=True)
    @patch("game.move_character_location", return_value="[0, 1]")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_player_successfully_moves_character(self, mock_stdout, _mock_execute_user_choice,
                                                 _mock_validate_move, _mock_move_character):
        rows = 10
        columns = 10
        character = {"Name": "Emily",
                     "Class": "Engineer",
                     "Rank": "Novice",
                     "Max HP": 15,
                     "Current HP": 15,
                     "Attack": 2,
                     "Hit Chance": 6,
                     "XP": 0,
                     "Location": [0, 1]}
        boss = {"Name": "HAL 8500",
                "Current HP": 23,
                "Attack": 6,
                "Hit Chance": 8,
                "Location": [3, 6]}
        game.player_moves_character(rows, columns, character, boss)
        print_statement = "You're now in [0, 1].\n"
        self.assertEqual(mock_stdout.getvalue(), print_statement)

