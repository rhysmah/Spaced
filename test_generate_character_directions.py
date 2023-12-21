from unittest import TestCase
import game


class TestGenerateCharacterDirections(TestCase):

    def test_generate_character_directions(self):
        actual = game.CHARACTER_DIRECTIONS()
        expected = {'North': -1, 'East': 1, 'South': 1, 'West': -1}
        self.assertEqual(expected, actual)
