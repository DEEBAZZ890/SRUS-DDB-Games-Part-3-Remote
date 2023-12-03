from app.player import Player
from app.player_node import PlayerNode
from typing import List, Optional


class PlayerList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    @property
    def head(self) -> Optional[PlayerNode]:
        return self._head

    @property
    def tail(self) -> Optional[PlayerNode]:
        return self._tail

    @tail.setter
    def tail(self, new_node: Optional[PlayerNode]) -> None:
        self._tail = new_node

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(Player Nodes={self.to_list()})'

    def is_empty(self) -> bool:
        """If no head is present, the list is empty"""
        return self._head is None

    def to_list(self) -> List[str]:
        """Returns a string repr of the linked list for each player"""
        my_list = []
        current_player = self._head
        while current_player:
            my_list.append(repr(current_player))
            current_player = current_player.next_player
        return my_list

    def display(self, forward=True) -> None:
        """Prints the contents of the linked list in a specified order"""
        if self.is_empty():
            raise ValueError("List is empty")
        if forward:
            current = self._head
            while current is not None:
                print(current)
                current = current.next_player
        else:
            current = self._tail
            while current is not None:
                print(current)
                current = current.previous_player

    def insert_head_node(self, player: Player) -> None:
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.next_player = self._head
            self._head.previous_player = new_player
            self._head = new_player

    def insert_tail_node(self, player: Player) -> None:
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.previous_player = self._tail
            self._tail.next_player = new_player
            self._tail = new_player

    def delete_head_node(self) -> None:
        if self.is_empty():
            raise ValueError("Deletion failed. List is empty; No head node exists")

        existing_head = self._head
        self._head = existing_head.next_player

        if self._head is None:
            self._tail = None
        else:
            self._head.previous_player = None

    def delete_middle_node_by_key(self, key: str) -> None:
        """Searches from the second node to the tail and deletes the matching player by key."""
        player_node = self._head.next_player

        while player_node is not None:
            if player_node.key == key:
                player_node.previous_player.next_player = player_node.next_player
                player_node.next_player.previous_player = player_node.previous_player
                return
            player_node = player_node.next_player
        raise ValueError(f"Player with UID: {key} not found. Deletion Failed")

    def delete_tail_node(self) -> None:
        if self._tail is None:
            raise ValueError("Deletion failed. List is empty; No tail node exists")
        else:
            existing_tail = self._tail
            self._tail = existing_tail.previous_player

            if self._tail is None:
                self._head = None
            else:
                self._tail.next_player = None

    def delete_player_node_by_key(self, key: str) -> None:
        if self.is_empty():
            raise ValueError(f"List is empty. Cannot delete player with key {key}.")

        if self._head.key == key:
            self.delete_head_node()
            return

        if self._tail.key == key:
            self.delete_tail_node()
            return

        self.delete_middle_node_by_key(key)
