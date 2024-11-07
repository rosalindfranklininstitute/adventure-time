from abc import ABC, abstractmethod
from adventurelib import say

class EscapeRoom(ABC):
    @abstractmethod
    def __init__(self) -> None:
         self.name = None
         self.locked = True
         self.escape_direction = None


    @abstractmethod
    def escape(self):
         pass
    @abstractmethod
    def room_completed(self):
         pass


