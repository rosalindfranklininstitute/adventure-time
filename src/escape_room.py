from abc import ABC, abstractmethod


class EscapeRoom(ABC):
    name: str

    @abstractmethod
    def play_room(self):
        pass

