from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag

class StoreRoom(EscapeRoom):

    def __init__(self):

        self.name = "storeroom"

        self.room = Room("""Enter the description of your room here""")

        self.escape_direction = "north" # escape direction of the room. Do not delete of change this property

        ##### add some items to give clues of the puzzles ###########
        # self.pen = Item("description of item", "item name")
        # self.book = Item("description of item", "item name")


        ####### add a Lock ###############

        self.locked = True # start with the room locked
        # a lock is defined as Lock("puzzle_answer", "description", "name")
        self.padlock = Lock("9999",
                            "The padlock has a 4 number combination to unlock",
                            "padlock")

        # add as many locks as you like
        # e.g.
        # self.treasure_chest= Lock("answer","description of puzzle", "chest")

        ##### add all you items and locks to an inventory ###########
        self.items = Bag({self.padlock})

    # Unlock the room by setting this test lock method. Once all the locks are open
    # the puzzle can be unlocked. You can implement this method how you like. Delete pass
    # and put your code in the place. An example is in the comments.
    def room_completed(self):
        #e.g.
        # if self.padlock.locked:
        #     self.locked=True
        # else:
        #     self.locked=False
        pass

    # Define the escape in this method. This will be triggered once all the puzzles are completed
    def escape(self):
        self.escape_room("direction", "description of what happens next")
       # e.g  self.escape_room("east","The door slides open reavealing the next room")


