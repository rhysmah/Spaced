from unittest import TestCase
import game


class TestAssignCharacterRank(TestCase):
    def test_assign_exact_middle_rank(self):
        character = {"Class": "Engineer", "XP": 10, "Rank": ""}
        ranks = {"Engineer": {0: "Novice", 10: "Intermediate", 20: "Expert"}}
        actual = game.assign_character_rank(character, ranks)
        expected = "Intermediate"
        self.assertEqual(expected, actual)

    def test_assign_inexact_highest_rank(self):
        character = {"Class": "Engineer", "XP": 26, "Rank": ""}
        ranks = {"Engineer": {0: "Novice", 10: "Intermediate", 20: "Expert"}}
        actual = game.assign_character_rank(character, ranks)
        expected = "Expert"
        self.assertEqual(expected, actual)

    def test_assign_inexact_lowest_rank(self):
        character = {"Class": "Engineer", "XP": 4, "Rank": ""}
        ranks = {"Engineer": {0: "Novice", 10: "Intermediate", 20: "Expert"}}
        actual = game.assign_character_rank(character, ranks)
        expected = "Novice"
        self.assertEqual(expected, actual)
