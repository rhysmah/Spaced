from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestEnemyAttacksFleeingPlayer(TestCase):

    @patch("random.randint", side_effect=[1])
    def test_enemy_unsuccessfully_attacks_fleeing_player(self, _mock_randint):
        character = {"Current HP": 5}
        enemy = {"Name": "Drone", "Attack": 3}
        actual = game.enemy_attacks_fleeing_player(enemy, character)
        expected = {"Current HP": 2}
        self.assertEqual(print(expected), actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.randint", side_effect=[3])
    def test_enemy_unsuccessfully_attacks_fleeing_player(self, _mock_randint, mock_stdout):
        character = {"Current HP": 5}
        enemy = {"Name": "Drone", "Attack": 3}
        game.enemy_attacks_fleeing_player(enemy, character)
        print_message = "You try running away...\n" \
                        "The Drone tries attacking you as you run...\n" \
                        "... and it misses! You're pretty lucky.\n"
        self.assertEqual(mock_stdout.getvalue(), print_message)
