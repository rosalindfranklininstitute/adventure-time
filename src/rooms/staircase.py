from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag

class Staircase(EscapeRoom):

    def __init__(self):

        self.padlock= Lock("key1", "A rusty padlock holds the door", "padlock")
        self.room = Room("""You are on a dusty staircase""")

    def escape(self):
        self.escape_room("east","you got out")

    def play_room(self):
        say(self.room)

    def test_lock(self):
        if self.padlock.locked:
            self.locked=True
        else:
            self.locked=False