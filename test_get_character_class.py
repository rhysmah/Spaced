import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestGetCharacterClass(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_valid_integer_input(self, _mock_input):
        classes = "Engineer", "Medic", "Soldier", "Scavenger"
        actual = game.get_character_class(classes)
        expected = "Engineer"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "2"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_integer_input(self, mock_stdout, _mock_input):
        classes = "Engineer", "Medic", "Soldier", "Scavenger"
        actual = game.get_character_class(classes)
        expected = "Medic"
        error_message = "That won't work. Select a class number."
        self.assertIn(error_message, mock_stdout.getvalue())
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["two", " ", "three!", "4"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_other_invalid_inputs(self, mock_stdout, _mock_input):
        classes = "Engineer", "Medic", "Soldier", "Scavenger"
        actual = game.get_character_class(classes)
        expected = "Scavenger"
        error_message = "That won't work. Select a class number."
        self.assertIn(error_message, mock_stdout.getvalue())
        self.assertEqual(expected, actual)
