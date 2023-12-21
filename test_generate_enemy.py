from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestGenerateEnemy(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.randint", side_effect=[3, 3, 8, 4, 4, 8, 6, 5, 8])
    @patch("random.choice", side_effect=["Drone"])
    def test_generate_enemy(self, _mock_input, _mock_enemy_name, _mock_output):
        character = {"XP": 0}
        actual = game.generate_enemy(character)
        expected = {"Name": "Drone",
                    "Current HP": 3,
                    "Attack": 3,
                    "XP": 2,
                    "Hit Chance": 8}
        printed_message = "A Drone appears..."
        self.assertEqual(expected, actual, printed_message)
