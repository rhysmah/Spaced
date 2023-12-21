from unittest import TestCase
import game


class GenerateCharacterRanks(TestCase):
    def test_generate_character_ranks(self):
        actual = game.CHARACTER_RANKS()
        expected = {"Engineer": {0: "Novice",
                                 10: "Intermediate",
                                 20: "Expert"},
                    "Medic": {0: "Intern",
                              10: "Resident",
                              20: "Attending"},
                    "Soldier": {0: "Private",
                                10: "Sergeant",
                                20: "Corporal"},
                    "Scavenger": {0: "Scrounger",
                                  10: "Explorer",
                                  20: "Master"}}
        self.assertEqual(expected, actual)
