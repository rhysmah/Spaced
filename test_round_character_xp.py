from unittest import TestCase
import game


class TestRoundCharacterXP(TestCase):
    def test_round_low_character_xp(self):
        character = {"XP": 3}
        actual = game. round_character_xp(character)
        expected = 0
        self.assertEqual(expected, actual)

    def test_round_high_character_xp(self):
        character = {"XP": 44}
        actual = game. round_character_xp(character)
        expected = 20
        self.assertEqual(expected, actual)

    def test_exact_character_xp(self):
        character = {"XP": 10}
        actual = game.round_character_xp(character)
        expected = 10
        self.assertEqual(expected, actual)
