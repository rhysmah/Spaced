from unittest import TestCase
from unittest import mock
import io
import game


class TestExecuteUserChoice(TestCase):

    @mock.patch('builtins.input', side_effect=['q'])
    def test_user_selects_q_to_quit(self, _mock_input):
        self.assertRaises(SystemExit)

    @mock.patch('builtins.input', side_effect=["m", "1"])
    @mock.patch.object(game, "display_game_board")
    def test_user_selects_m_for_map(self, _mock_input, mock_function):
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
        game.execute_user_choice(rows, columns, character, boss)
        mock_function.assert_called()

    @mock.patch('builtins.input', side_effect=["s", "1"])
    @mock.patch.object(game, "display_stats")
    def test_user_selects_s_for_stats(self, _mock_input, mock_function):
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
        game.execute_user_choice(rows, columns, character, boss)
        mock_function.assert_called()

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=["r", "3"])
    def test_user_selects_r_for_room(self, _mock_input, mock_stdout):
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
                     "Location": [2, 5]}
        boss = {"Name": "HAL 8500",
                "Current HP": 23,
                "Attack": 6,
                "Hit Chance": 8,
                "Location": [3, 6]}
        actual = game.execute_user_choice(rows, columns, character, boss)
        print_message = "You're currently in room [2, 5].\n"
        expected = "South"
        self.assertEqual(mock_stdout.getvalue(), print_message)
        self.assertEqual(expected, actual)

    @mock.patch('builtins.input', side_effect=["4"])
    def test_user_selects_valid_integer_to_move_south(self, _mock_input):
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
        actual = game.execute_user_choice(rows, columns, character, boss)
        expected = "West"
        self.assertEqual(expected, actual)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=["6", "3"])
    def test_user_selects_invalid_integer_to_move(self, _mock_input, mock_stdout):
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
        actual = game.execute_user_choice(rows, columns, character, boss)
        print_message = "That won't work. Choose one of the available options.\n"
        expected = "South"
        self.assertEqual(mock_stdout.getvalue(), print_message)
        self.assertEqual(expected, actual)
