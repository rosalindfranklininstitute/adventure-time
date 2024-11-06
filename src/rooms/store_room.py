from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag

class StoreRoom(EscapeRoom):

    def __init__(self):

        self.room = Room("""You enter a dingy storeroom...""")

    def escape(self):
        self.escape_room("east","you got out")

    def play_room(self):
        say(self.room)

    def test_lock(self):
        if self.padlock.locked:
            self.locked=True
        else:
            self.locked=False