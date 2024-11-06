from abc import ABC, abstractmethod


class EscapeRoom(ABC):
    name: str
    locked: True

    @abstractmethod
    def play_room(self):
        pass

