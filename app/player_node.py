from __future__ import annotations
from typing import Optional
from app.player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._next_player = None
        self._previous_player = None

    def __str__(self) -> str:
        return f"{self.player.uid} - {self.player.name}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(player={self.player!r})'

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: Player) -> None:
        self._player = value

    @property
    def next_player(self) -> Optional[PlayerNode]:
        return self._next_player

    @next_player.setter
    def next_player(self, node: Optional[PlayerNode]) -> None:
        self._next_player = node

    @property
    def previous_player(self) -> Optional[PlayerNode]:
        return self._previous_player

    @previous_player.setter
    def previous_player(self, node: Optional[PlayerNode]) -> None:
        self._previous_player = node

    @property
    def key(self) -> str:
        return self._player.uid
