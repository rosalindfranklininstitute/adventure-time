from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod
    def exit_room(self):
        raise NotImplementedError
