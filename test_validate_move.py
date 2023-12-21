from unittest import TestCase
import game


class TestValidateMove(TestCase):

    def test_validate_moving_north_and_it_is_possible(self):
        character = {"Location": [1, 1]}
        direction = "North"
        rows = 4
        columns = 4
        expected = True
        actual = game.validate_character_move(character, direction, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_moving_north_and_it_is_not_possible(self):
        character = {"Location": [1, 0]}
        direction = "North"
        rows = 4
        columns = 4
        expected = False
        actual = game.validate_character_move(character, direction, rows, columns)
        self.assertEqual(expected, actual)
