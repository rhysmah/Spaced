from unittest import TestCase
import game


class TestIsAlive(TestCase):

    def test_is_alive(self):
        character = {'Current HP': 1}
        actual = game.is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_not_alive(self):
        character = {'Current HP': 0}
        actual = game.is_alive(character)
        expected = False
        self.assertEqual(expected, actual)
