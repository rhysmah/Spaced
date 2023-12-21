from unittest import TestCase
import game


class TestGenerateCharacterStats(TestCase):
    def test_generate_character_stats(self):
        actual = game.CHARACTER_STATS()
        expected = {"Novice": (13, 3, 6),
                    "Intermediate": (17, 4, 7),
                    "Expert": (20, 5, 8),
                    "Intern": (15, 1, 6),
                    "Resident": (18, 2, 7),
                    "Attending": (23, 3, 8),
                    "Private": (20, 4, 7),
                    "Sergeant": (23, 5, 8),
                    "Corporal": (23, 6, 9),
                    "Scrounger": (13, 3, 6),
                    "Explorer": (17, 4, 7),
                    "Master": (19, 4, 8)}
        self.assertEqual(expected, actual)
