import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestLevelUpCharacter(TestCase):

    @patch("game.assign_character_rank")
    @patch("game.assign_character_stats")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_up_at_10_xp(self,  _mock_stdout, _mock_assign_rank, _mock_assign_stats):
        character = {"XP": 8}
        enemy = {"XP": 2}
        game.level_up_character(character, enemy)
        print_message = "You earned 2XP!\n" \
                        "\nYou leveled up!\n"
        self.assertEqual(_mock_stdout.getvalue(), print_message)

    @patch("game.assign_character_rank")
    @patch("game.assign_character_stats")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_up_at_20_xp(self, _mock_stdout, _mock_assign_rank, _mock_assign_stats):
        character = {"XP": 18}
        enemy = {"XP": 2}
        game.level_up_character(character, enemy)
        print_message = "You earned 2XP!\n" \
                        "\nYou leveled up!\n" \
                        "You've hit the maximum level!\n"
        self.assertEqual(_mock_stdout.getvalue(), print_message)
