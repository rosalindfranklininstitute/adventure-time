from escape_room import EscapeRoom
from adventurelib import Room, Item, say

class EntrancePuzzle(EscapeRoom):

    def __init__(self) -> None:
        super().__init__()

        # Define your room
        self.entrance_hall = Room(""" You have entered an entrance hall.
                                It has a high vaulted ceiling and there is an ancient desk in the corner, papers scattered over its surface.
                                Above the desk is a clock, it has stopped. No one has been here for years. In
                                the north you see a pair of double doors and a key pad.""")

        # Define the items in your room
        self.keypad = Item("The keypad requires a 4 digit code", "keypad")
        self.clock = Item("The clocks hands are stuck at 17 minutes past 11", "clock")


    def play_room(self):
        # this is where you script your game, essentially your main method. It is used in the code like the statement
        # if __name__=='__main__'

        say(self.entrance_hall)

