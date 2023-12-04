import unittest
from app.player import Player


class TestPlayerClass(unittest.TestCase):
    def setUp(self) -> None:
        self.test_uid = "20069321"
        self.test_name = "Daniel"
        self.player = Player(self.test_uid, self.test_name)
        self.sample_password = "someones password"

    def test_player_creation(self):
        self.assertEqual(self.player.uid, self.test_uid)
        self.assertEqual(self.player.name, self.test_name)
        self.assertIsNone(self.player._hashed_password)

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




if __name__ == "__main__":
    unittest.main()
