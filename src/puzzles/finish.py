from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag

class Finish(EscapeRoom):

    def __init__(self):
        self.name = "finish"

        self.room = Room("""You find yourself on a lawn surrounded by bright sunlight. In the distance you see people wandering around the campus. You breathe a sigh of relief. Congratulations you have escaped from the Lab!""")

        self.escape_direction = None # escape direction of the room. Do not delete of change this property


        self.locked = False # start with the room locked


    def room_completed(self):

        pass

    def escape(self):
        pass