from unittest import TestCase
import io
from unittest.mock import patch
import game


class TestCharacterFightsEnemy(TestCase):

    @patch("game.player_chooses_to_flee_or_fight", return_value=False)
    @patch("game.enemy_attacks_fleeing_player")
    def test_character_runs_from_enemy(self, _mock_stdout, _mock_player_flees):
        character = {}
        enemy = {}
        actual = game.character_fights_enemy(character, enemy)
        expected = False
        self.assertEqual(expected, actual)

    @patch("game.player_chooses_to_flee_or_fight", return_value=True)
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[1])
    def test_character_attacks_enemy_and_enemy_runs_away(self, _mock_randint, _mock_stdout,
                                                         _mock_player_fights):
        character = {}
        enemy = {}
        game.character_fights_enemy(character, enemy)
        print_message = "The enemy runs away...\n"
        self.assertEqual(_mock_stdout.getvalue(), print_message)

    @patch("game.player_chooses_to_flee_or_fight", return_value=True)
    @patch('random.randint', side_effect=[2])
    @patch("game.attack_hits_or_misses")
    @patch("game.is_alive", return_value=False)
    @patch("game.level_up_character")
    def test_character_attacks_and_defeats_enemy(self, _mock_player_flees, _mock_randint,
                                                 _mock_attack_hits_or_misses, _mock_is_alive,
                                                 _mock_level_up):
        character = {}
        enemy = {}
        game.character_fights_enemy(character, enemy)

    @patch("game.player_chooses_to_flee_or_fight", return_value=True)
    @patch('random.randint', side_effect=[2])
    @patch("game.attack_hits_or_misses")
    @patch("game.is_alive", return_value=True)
    @patch("game.attack_hits_or_misses")
    def test_character_attacks_then_enemy_attacks_and_both_live(self, _mock_player_fights, _mock_randint,
                                                                _mock_player_attacks, _mock_is_alive,
                                                                _mock_enemy_attacks):
        character = {}
        enemy = {}
        game.character_fights_enemy(character, enemy)

    @patch("game.player_chooses_to_flee_or_fight", return_value=True)
    @patch('random.randint', side_effect=[2])
    @patch("game.attack_hits_or_misses")
    @patch("game.is_alive", return_value=True)
    @patch("game.attack_hits_or_misses")
    @patch("game.is_alive", return_value=False)
    def test_character_attacks_then_enemy_attacks_and_defeats_player(self, _mock_player_fights, _mock_randint,
                                                                     _mock_attack_hits_or_misses, _mock_is_alive,
                                                                     _mock_enemy_attacks, _mock_player_dies):
        character = {}
        enemy = {}
        game.character_fights_enemy(character, enemy)
