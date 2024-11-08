from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag

class MicroscopeHall(EscapeRoom):

    def __init__(self):
        self.name = "miscroscope hall"

        self.room = Room("""The Microscope Hall. You have entered a dimly lit, dusty room with a large disassembled microscope in the middle, seemingly unused for many years. There is a locked chest underneath the microscope. On one side of the room, there is a sample prep table with 3 test tubes and a mouldy book. Beneath the table is a brightly coloured guinea pig.""")

        self.escape_direction="north" # escape direction of the room. Do not delete of change this property

        ##### add some items to give clues of the puzzles ###########
        self.pen = Item("A pen leaking ink.", "pen")
        self.book = Item("This is a well-thumbed copy of Microscopes for Dummies. A parchment falls out of the book.", "book")
        self.fragment = Item("This code could be the key to help you unlock the door, reveal a map, or open a chest as part of their adventure!\nI - 3 = F\nL - 3 = I\nT - 3 = Q\nU - 3 = R\nY - 3 = V", "fragment")
        self.table = Item("On the table are 3 test tubes. The test tubes are labelled Germanium, Sulfur, Tantalum", "table")
        ####### add a Lock ###############

        self.locked = True # start with the room locked
        # a lock is defined as Lock("puzzle_answer", "description", "name")
        self.parchment = Lock("utility",
                "You see an old piece of parchment. It is very fragile and a fragment falls off it. On it, written in an elegant script, is the following message: In science, the true key lies in UTILITY - uncovering knowledge that serves a purpose. Use the code of *Caesar* to find the path forward by stepping back three steps in your quest. Here is the encrypted message: RQFIFQV. ",
                            "parchment")
        
        self.guinea_pig = Lock("2018", "As you examine the guinea pig, you squeeze it and it speaks to you: In a year, not long ago, a vision took its flight. To push the bounds of science with technology in sight. Named for a pioneer, whose work we now commend, this institute was founded, a future to transcend. What year did this journey begin?", "guinea_pig")
        
        self.chest = Lock("stage", "The chest is an ancient wooden box with a large alphabetic lock. There's a note pinned to the chest saying: Enter the microscope component that the elements spell.", "chest")
        
        
        # add as many locks as you like
        # e.g.
        #self.book = Lock("A","description of puzzle", "book")

        ##### add all you items and locks to an inventory ###########
        self.items = Bag({self.parchment, self.guinea_pig,self.book, self.fragment, self.chest, self.table})

    # Unlock the room by setting this test lock method. Once all the locks are open
    # the puzzle can be unlocked. You can implement this method how you like. Delete pass
    # and put your code in the place. An example is in the comments.
    def room_completed(self):
        if not self.parchment.locked and not self.guinea_pig.locked and not self.chest.locked:
                self.locked = False
        else:
                self.locked = True
        #e.g.
        # if self.padlock.locked:
        #     self.locked=True
        # else:
        #     self.locked=False
        pass

    # Define the escape in this method. This will be triggered once all the puzzles are completed
    def escape(self):
            print("A loud grinding sound as the door to the north slides open.")
            pass
        #self.escape_room("direction", "description of what happens next")
        #self.escape_room("west","The door slides open reavealing the next room")


