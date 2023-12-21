import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestGetCharacterName(TestCase):

    @patch('builtins.input', side_effect=["john"])
    def test_add_character_name_that_is_letters_only(self, _mock_input):
        actual = game.get_character_name()
        expected = "John"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["tim8", "tim ", "timmy tim", 'tim'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_character_name_that_is_not_letters_only(self, mock_stdout, _mock_input):
        actual = game.get_character_name()
        expected = "Tim"
        error_message = "That won't work. Use uppercase or lowercase letters only."
        self.assertIn(error_message, mock_stdout.getvalue())
        self.assertEqual(expected, actual)
