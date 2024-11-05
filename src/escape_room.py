from abc import ABC, abstractmethod


class EscapeRoom(ABC):

    @abstractmethod
    def play_puzzle(self):
        raise NotImplementedError
