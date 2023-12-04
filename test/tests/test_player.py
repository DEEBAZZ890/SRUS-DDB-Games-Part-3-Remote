import unittest
from app.player import Player


class TestPlayerClass(unittest.TestCase):
    def setUp(self) -> None:
        self.test_uid = "20069321"
        self.test_name = "Daniel"
        self.test_score = 4
        self.sample_password = "someones password"
        self.player = Player(self.test_uid, self.test_name)

        # List of player objects for the sorting test
        self.test_player_list = [
            Player("10472204", "John"),
            Player("29543305", "Brayden"),
            Player("10983546", "Sarah"),
            Player("12345678", "Michaela"),
            Player("11111111", "Alex")
        ]

        # Using the score setter to set the scores for the test_player_list player objects
        self.test_player_list[0].score = 30
        self.test_player_list[1].score = 20
        self.test_player_list[2].score = 25
        self.test_player_list[3].score = 15
        self.test_player_list[4].score = 30

    def test_player_creation(self):
        self.assertEqual(self.player.uid, self.test_uid)
        self.assertEqual(self.player.name, self.test_name)
        self.assertIsNone(self.player._hashed_password)

    def test_score_is_set(self):
        """Test that a score is correctly added for a player using the Player class Score setter"""
        self.player.score = self.test_score
        self.assertEqual(self.player.score, self.test_score)

    def test_str_representation(self):
        expected_str = f"UID:{self.test_uid} NAME: {self.test_name}"
        self.assertEqual(str(self.player), expected_str)

    def test_repr_representation(self):
        expected_repr = f"CLASS: Player(UID: '{self.test_uid}', NAME: '{self.test_name}')"
        self.assertEqual(repr(self.player), expected_repr)

    def test_add_password(self):
        self.player.add_password(self.sample_password)
        self.assertIsNotNone(self.player._hashed_password)

    def test_add_empty_password_raises_error(self):
        self.assertRaises(ValueError, self.player.add_password, "")

    def test_verify_password(self):
        self.player.add_password(self.sample_password)
        self.assertTrue(self.player.verify_password(self.sample_password))
        self.assertFalse(self.player.verify_password("wrongPassword"))

    def test_verify_password_before_setting_raises_error(self):
        """Test that verification fails if password has not been set"""
        self.assertRaises(ValueError, self.player.verify_password, "anyPassword")

    def test_invalid_password_is_strictly_false(self):
        self.player.add_password(self.sample_password)
        self.assertIs(self.player.verify_password("wrongPassword"), False)

    def test_valid_password_is_strictly_true(self):
        self.player.add_password(self.sample_password)
        self.assertIs(self.player.verify_password(self.sample_password), True)

    def test_eq_operator(self):
        player1 = self.test_player_list[0]
        player2 = self.test_player_list[4]
        self.assertTrue(player1 == player2)

    def test_ne_operator(self):
        player1 = self.test_player_list[0]
        player2 = self.test_player_list[1]
        self.assertTrue(player1 != player2)

    def test_lt_operator(self):
        player1 = self.test_player_list[1]
        player2 = self.test_player_list[0]
        self.assertTrue(player1 < player2)

    def test_le_operator(self):
        player1 = self.test_player_list[4]
        player2 = self.test_player_list[0]
        self.assertTrue(player1 <= player2)

    def test_gt_operator(self):
        player1 = self.test_player_list[0]
        player2 = self.test_player_list[1]
        self.assertTrue(player1 > player2)

    def test_ge_operator(self):
        player1 = self.test_player_list[0]
        player2 = self.test_player_list[4]
        self.assertTrue(player1 >= player2)

    def test_sort_players_descending(self):
        """Test that sorting method correctly sorts the list of players in descending order"""
        sorted_list = sorted(self.test_player_list, key=lambda x: x.score, reverse=True)
        Player.sort_players_descending(self.test_player_list)
        self.assertEqual(self.test_player_list, sorted_list)


if __name__ == "__main__":
    unittest.main()
