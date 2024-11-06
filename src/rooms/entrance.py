from escape_room import EscapeRoom
from adventurelib import Room, Item, say, Bag
from lock import Lock


class EntrancePuzzle(EscapeRoom):

    def __init__(self):

        # Define your room
        self.room = Room(""" You have entered an entrance hall.
                                It has a high vaulted ceiling and there is an ancient desk in the corner, papers scattered over its surface.
                                Above the desk is a clock, it has stopped. No one has been here for years. In
                                the north you see a pair of double doors and a key pad.""")

        # Define the items in your room
        self.clock = Item("The clocks hands are stuck at 17 minutes past 11", "clock")
        self.papers = Item("The papers are a manuscript of a book. The title reads: 'Stopped Time Unlocks Doors'", "papers")

        #Define the Lock

        self.keypad = Lock(  "2317","The keypad requires a 4 digit code","keypad")

        self.items = Bag({self.keypad, self.clock, self.papers})

        self.locked = self.keypad.locked


    def play_room(self):
        # this is where you script your game, essentially your main method. It is used in the code like the statement
        # if __name__=='__main__'



        say(self.room)

            # say("You tentitatively push the door, it creaks open.\
            #      To the north lies the next room.")
            # self.direction = 'north'
