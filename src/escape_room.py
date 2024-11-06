from abc import ABC, abstractmethod
from adventurelib import say

class EscapeRoom(ABC):
    name: str
    locked: bool
    escape_direction: str

    locked=True



    @abstractmethod
    def escape(self):
         pass
    @abstractmethod
    def test_lock(self):
         pass


