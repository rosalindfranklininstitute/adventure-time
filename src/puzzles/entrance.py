from escape_room import EscapeRoom
from adventurelib import Room, Item, say, Bag
from lock import Lock


class Entrance(EscapeRoom):

    def __init__(self):
        self.name = "entrance"


        # Define your room
        self.room = Room(""" You have entered an entrance hall.
                                It has a high vaulted ceiling and there is an ancient desk in the corner, papers scattered over its surface.
                                Above the desk is a clock, it has stopped. No one has been here for years. In
                                the north you see a pair of double doors and a key pad.""")

        self.escape_direction = "north"

        # Define the items in your room
        self.clock = Item("The clocks hands are stuck at 17 minutes past 11", "clock")
        self.papers = Item("The papers are a manuscript of a book. The title reads: 'Stopped Time Unlocks Doors'", "papers")
        self.desk = Item("There is an old mahogany desk, with yellowing papers scattered on the surface", "desk")
        self.doors = Item("The doors are locked and can be opened by a code typed into the keypad", "doors")

        #Define the Lock

        self.keypad = Lock(  "2317","The keypad requires a 4 digit code","keypad")

        #Add all your items to an iventory
        self.items = Bag({self.keypad, self.clock, self.papers, self.desk, self.doors})

        self.locked = True



    def room_completed(self):
        if self.keypad.locked:
            self.locked=True
        else:
            self.locked=False



    def escape(self):
        pass
