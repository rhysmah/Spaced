from unittest import TestCase
from unittest.mock import patch
import game


class TestGenerateCharacter(TestCase):

    @patch('builtins.input', side_effect=['emily', '1'])
    def test_generate_character_engineer_novice_named_emily(self, _mock_input):
        classes = "Engineer", "Medic", "Soldier", "Scavenger"
        ranks = {"Engineer": {0: "Novice", 10: "Intermediate", 20: "Expert"}}
        stats = {"Novice": (15, 2, 6), "Intermediate": (17, 3, 7), "Expert": (20, 4, 8)}
        actual = game.generate_character(classes, ranks, stats)
        expected = {"Name": "Emily",
                    "Class": "Engineer",
                    "Rank": "Novice",
                    "Max HP": 15,
                    "Current HP": 15,
                    "Attack": 2,
                    "Hit Chance": 6,
                    "XP": 0,
                    "Location": [0, 0]}
        self.assertEqual(expected, actual)
