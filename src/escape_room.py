from abc import ABC, abstractmethod
from adventurelib import say

class EscapeRoom(ABC):
    name: str
    locked: bool
    escape_direction: str

    @abstractmethod
    def escape(self):
         pass
    @abstractmethod
    def room_completed(self):
         pass


