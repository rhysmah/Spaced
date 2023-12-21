from unittest import TestCase
import game


class TestGenerateCharacterClasses(TestCase):

    def test_generate_character_classes(self):
        actual = game.CHARACTER_CLASSES()
        expected = ('Engineer', 'Medic', 'Soldier', 'Scavenger')
        self.assertEqual(expected, actual)
