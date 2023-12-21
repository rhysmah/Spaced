from unittest import TestCase
import game


class TestDisplayStats(TestCase):

    def test_display_stats(self):
        figure = {"Name": "John", "Class": "Medic", "Rank": "Resident"}
        actual = game.display_stats(figure)
        expected = "------------------------\n"
        "Name        |  John\n"
        "Class       |  Medic\n"
        "Rank        |  Resident\n"
        "------------------------\n"
        self.assertEqual(print(expected), actual)
