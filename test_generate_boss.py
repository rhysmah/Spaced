from unittest import TestCase
from unittest.mock import patch
import game


class TestGenerateBoss(TestCase):

    @patch("random.randint", side_effect=[23, 6, 5, 6])
    def test_generate_boss(self, _mock_input):
        rows = 10
        columns = 10
        actual = game.generate_boss(rows, columns)
        expected = {"Name": "HAL 8500", "Current HP": 23,
                    "Attack": 6, "Hit Chance": 8, "Location": [5, 6]}
        self.assertEqual(expected, actual)
