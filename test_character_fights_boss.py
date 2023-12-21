from unittest import TestCase
from unittest.mock import patch
import game


class TestCharacterFightsBoss(TestCase):

    @patch("game.is_alive", return_value=[True, True, False])
    @patch("game.player_chooses_to_flee_or_fight", return_value=True)
    @patch("game.attack_hits_or_misses")
    def test_character_attempts_attack_and_defeats_boss(self, _is_alive, _mock_fight_or_flee,
                                                        _mock_boss_attacks_player):
        character = {}
        boss = {}
        game.character_fights_boss(character, boss)

    @patch("game.player_chooses_to_flee_or_fight", return_value=True)
    @patch("game.attack_hits_or_misses")
    @patch("game.is_alive", return_value=True)
    @patch("game.attack_hits_or_misses")
    @patch("game.is_alive", return_value=False)
    def test_character_attacks_boss_then_is_defeated_by_boss(self, _mock_fight, _mock_player_attacks_boss,
                                                             _mock_boss_is_alive, _mock_boss_attacks_player,
                                                             _mock_player_is_dead):
        character = {}
        boss = {}
        actual = game.character_fights_boss(character, boss)
        expected = None
        self.assertEqual(expected, actual)
