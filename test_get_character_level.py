from unittest import TestCase
import game


class GetCharacterLevel(TestCase):

    def test_get_character_level_when_xp_level_below_10(self):
        character = {"XP": 8}
        actual = game.round_character_xp(character)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_character_level_when_xp_level_between_and_19(self):
        character = {"XP": 11}
        actual = game.round_character_xp(character)
        expected = 10
        self.assertEqual(expected, actual)

    def test_get_character_level_when_xp_level_20(self):
        character = {"XP": 20}
        actual = game.round_character_xp(character)
        expected = 20
        self.assertEqual(expected, actual)


