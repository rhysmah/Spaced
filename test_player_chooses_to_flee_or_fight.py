from unittest import TestCase
from unittest.mock import patch
import io
import game


class Test(TestCase):

    @patch('builtins.input', side_effect=["f"])
    def test_player_inputs_f_to_fight(self, _mock_input):
        enemy = {}
        actual = game.player_chooses_to_flee_or_fight(enemy)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["r"])
    def test_player_inputs_r_to_run(self, _mock_input):
        enemy = {}
        actual = game.player_chooses_to_flee_or_fight(enemy)
        expected = False
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=['e', 'r'])
    @patch.object(game, "display_stats")
    def test_player_inputs_e_to_display_enemy_stats(self, _mock_input, mock_function):
        enemy = {"Name": "Drone", "Attack": 5, "Current HP": 5}
        game.player_chooses_to_flee_or_fight(enemy)
        mock_function.assert_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["g", "f"])
    def test_player_inputs__invalid_input(self, _mock_input, mock_stdout):
        enemy = {}
        game.player_chooses_to_flee_or_fight(enemy)
        print_message = "Invalid command. Enter 'f' to fight or 'r' to run.\n"
        self.assertEqual(mock_stdout.getvalue(), print_message)
