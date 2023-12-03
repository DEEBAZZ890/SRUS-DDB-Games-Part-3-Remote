from typing import Optional
from argon2 import PasswordHasher, exceptions


class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid = uid
        self._name = name
        self._hashed_password: Optional[str] = None

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"UID:{self._uid} NAME: {self._name}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'CLASS: {class_name}(UID: {self.uid!r}, NAME: {self.name!r})'

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
