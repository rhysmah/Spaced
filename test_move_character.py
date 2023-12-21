from unittest import TestCase
import game


class TestMoveCharacter(TestCase):

    def test_move_character_north(self):
        character = {'Location': [1, 1]}
        direction = "North"
        actual = game.move_character_location(character, direction)
        expected = None
        self.assertEqual(expected, actual)

    def test_move_character_south(self):
        character = {'Location': [1, 1]}
        direction = "South"
        actual = game.move_character_location(character, direction)
        expected = None
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character = {'Location': [1, 1]}
        direction = "East"
        actual = game.move_character_location(character, direction)
        expected = None
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        character = {'Location': [1, 1]}
        direction = "West"
        actual = game.move_character_location(character, direction)
        expected = None
        self.assertEqual(expected, actual)
