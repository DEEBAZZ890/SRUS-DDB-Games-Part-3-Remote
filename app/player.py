from typing import Optional
from argon2 import PasswordHasher, exceptions


class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid = uid
        self._name = name
        self._hashed_password: Optional[str] = None
        self._score = 0

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        if value < 0:
            raise ValueError("Score must be a positive integer")
        self._score = value

    def __str__(self) -> str:
        return f"UID:{self._uid} NAME: {self._name}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'CLASS: {class_name}(UID: {self.uid!r}, NAME: {self.name!r})'

    def __eq__(self, other: 'Player') -> bool:
        return self.score == other.score

    def __ne__(self, other: 'Player') -> bool:
        return self.score != other.score

    def __lt__(self, other: 'Player') -> bool:
        return self.score < other.score

    def __le__(self, other: 'Player') -> bool:
        return self.score <= other.score

    def __gt__(self, other: 'Player') -> bool:
        return self.score > other.score

    def __ge__(self, other: 'Player') -> bool:
        return self.score >= other.score

    def add_password(self, password: str) -> None:
        """Takes a password as a string and from it, generate a hash that is stored for the player"""
        if not password.strip():
            raise ValueError("No password entered. The player must have a password")
        else:
            ph = PasswordHasher()
            hash_value = ph.hash(password)
            self._hashed_password = hash_value

    def verify_password(self, password: str) -> bool:
        """Uses the stored hash of the player's password to verify if a password is correct"""
        if self._hashed_password is None:
            raise ValueError("No password has been set for this player")
        ph = PasswordHasher()
        try:
            ph.verify(self._hashed_password, password)
            return True
        except exceptions.VerifyMismatchError:
            return False

    @staticmethod
    def sort_players_descending(players: list['Player']):
        """Takes a list of Player objects and sorts them in descending order using an Insertion Sort Algorithm"""
        for i in range(1, len(players)):
            current_player = players[i]
            next_slot = i - 1
            while next_slot >= 0 and players[next_slot].score < current_player.score:
                players[next_slot + 1] = players[next_slot]
                next_slot -= 1
            players[next_slot + 1] = current_player
        return None



