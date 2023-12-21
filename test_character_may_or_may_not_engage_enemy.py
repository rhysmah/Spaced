from unittest import TestCase
from unittest.mock import patch

import game


class TestPlayerMayOrMayNotEngageEnemy(TestCase):

    @patch("game.generate_enemy")
    @patch("random.randint", side_effect=[3])
    def test_character_does_not_engage_enemy(self, _mock_randint, _mock_generate_enemy):
        character = {}
        game.character_may_or_may_not_engage_enemy(character)

    @patch("game.generate_enemy")
    @patch("random.randint", side_effect=[3])
    @patch("game.character_fights_enemy")
    def test_character_does_engage_enemy(self, _mock_randint, _mock_generate_enemy,
                                         _mock_character_fights_enemy):
        character = {}
        game.character_may_or_may_not_engage_enemy(character)
