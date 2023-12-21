from unittest import TestCase
import game


class TestAssignCharacterStats(TestCase):

    def test_assign_lowest_character_stats(self):
        character = {'Rank': 'Private', 'Max HP': '', 'Current HP': '', 'Attack': '', 'Hit Chance': ''}
        stats = {"Private": (20, 4, 7), "Sergeant": (23, 5, 8), "Corporal": (23, 6, 9)}
        actual = game.assign_character_stats(character, stats)
        expected = {'Rank': 'Sergeant', 'Max HP': 20, 'Current HP': 20, 'Attack': 4, 'Hit Chance': 7}
        self.assertEqual(print(expected), actual)

    def test_assign_highest_character_stats(self):
        character = {'Rank': 'Corporal', 'Max HP': '', 'Current HP': '', 'Attack': '', 'Hit Chance': ''}
        stats = {"Private": (20, 4, 7), "Sergeant": (23, 5, 8), "Corporal": (23, 6, 9)}
        actual = game.assign_character_stats(character, stats)
        expected = {'Rank': 'Sergeant', 'Max HP': 23, 'Current HP': 23, 'Attack': 6, 'Hit Chance': 9}
        self.assertEqual(print(expected), actual)
