from abc import ABC, abstractmethod
from adventurelib import say

class EscapeRoom(ABC):
    name: str
    locked: bool
    direction: str


    def escape_room(self,direction,
                    escape_message="Congratulations you have escaped the room"):
            self.direction = direction
            say(escape_message)
            say(f"Go {self.direction} for next room")

    @abstractmethod
    def escape(self):
         pass
    @abstractmethod
    def test_lock(self):
         pass
    @abstractmethod
    def play_room(self):
        pass

