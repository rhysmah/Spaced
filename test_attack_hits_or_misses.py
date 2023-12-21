from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestAttackHitsOrMisses(TestCase):

    @patch('random.randint', side_effect=[9])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_attack_misses(self, _mock_stdout, _mock_randint):
        attacker = {"Name": "Drone", "Hit Chance": 8, "Attack": 3}
        attackee = {"Name": "John", "Current HP": 5}
        game.attack_hits_or_misses(attacker, attackee)
        print_message = "Drone tries attacking John...\n" \
                        "... and misses!\n"
        self.assertEqual(_mock_stdout.getvalue(), print_message)

    @patch('random.randint', side_effect=[7])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_attack_hits_and_attackee_lives(self, _mock_stdout, _mock_randint):
        attacker = {"Name": "Drone", "Hit Chance": 8, "Attack": 3}
        attackee = {"Name": "John", "Current HP": 5}
        actual = game.attack_hits_or_misses(attacker, attackee)
        expected = {"Name": "John", "Current HP": 2}
        print_message = "Drone tries attacking John...\n" \
                        "... and succeeds!\n" \
                        "\nJohn loses 3HP.\n" \
                        "John has 2HP remaining.\n\n"
        self.assertEqual(_mock_stdout.getvalue(), print_message)
        self.assertEqual(print(expected), actual)

    @patch('random.randint', side_effect=[7])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_attack_hits_and_attackee_dies(self, _mock_stdout, _mock_randint):
        attacker = {"Name": "Drone", "Hit Chance": 8, "Attack": 3}
        attackee = {"Name": "John", "Current HP": 3}
        actual = game.attack_hits_or_misses(attacker, attackee)
        expected = {"Name": "John", "Current HP": 0}
        print_message = "Drone tries attacking John...\n" \
                        "... and succeeds!\n" \
                        "\nJohn loses 3HP.\n" \
                        "John has been defeated!\n"
        self.assertEqual(_mock_stdout.getvalue(), print_message)
        self.assertEqual(print(expected), actual)

