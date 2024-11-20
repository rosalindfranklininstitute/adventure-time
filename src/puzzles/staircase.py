from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag, say

class Staircase(EscapeRoom):
    def __init__(self):
        self.name = "staircase"
        self.floor_descriptions = [
"""
You find yourself at the foot of a staircase. It looks like it hasn't been used in a hundred years. Wasn't the RFI built more recently than that?
I certiainly don't think that the stairs were built out of wood, and surrounded by torchces. Huh. Paul Matthews must have remodelled over the weekend.
Along the opposite wall to the torches, you see a picture of MS image of a brain, an electron microscope, and a 96 well plate.
At the top of the flight of stairs, you see a sign for Mass Spec. Since when do they get their own floor?
To your right you see a lift with the doors already open.
""",

"""
You find yourself at the foot of another flight of stairs. There are ten pictures along the wall, and the penultimate is a microscope.
At the top of the stairs you see a sign for CI. I thought they had to share a floor too?
""",

"""
You find youself at the foot of another flight of stairs. There are ten more pictures.
You spend a while looking at a lovely landscape before realising that you should move on. You've stayed here too long.
The second picture was much more boring so it's fine, it was just a server rack or something.
At the top you see a sign for AI&I.
""",

"""
You find yourself at the foot of another flight of stairs. There are more pictures and another sign.
The sign is for SB this time. You're starting to notice the themes. It's a shame that this staircase doesn't have pictures of llamas.
""",

"""
You have reached the top floor. Hang on, why isn't there any chemistry?
There's a keypad here.
"""

        ]
        self.floor = 0
        self.room = Room(self.floor_descriptions[0])
        self.lift_state = "The lift judders, but doesn't move. You suppose you'll have to try the stairs."


        self.escape_direction = "east" # escape direction of the room. Do not delete of change this property

        ##### add some items to give clues of the puzzles ###########
        # self.pen = Item("description of item", "item name")
        # self.book = Item("description of item", "item name")
        self.floor = 0


        ####### add a Lock ###############

        self.locked = True # start with the room locked
        # a lock is defined as Lock("puzzle_answer", "description", "name")
        self.keypad = Lock("1920",
                           "The padlock has a 4 number combination to unlock",
                           "keypad"
                           )
        self.lift = Lock("ben davis",
                         "There is surprisingly a high tech lift in the corner. You can press buttons to ascend or descend",
                         "lift")

        # add as many locks as you like
        # e.g.
        # self.treasure_chest= Lock("answer","description of puzzle", "chest")

        ##### add all you items and locks to an inventory ###########
        self.items = Bag({self.keypad, self.lift})



    # Unlock the room by setting this test lock method. Once all the locks are open
    # the puzzle can be unlocked. You can implement this method how you like. Delete pass
    # and put your code in the place. An example is in the comments.
    def room_completed(self):
        if not self.keypad.locked:
                say("The lift sounds like it is working now.")
                msg = \
"""
A booming voice shouts out:
ANSWER MY RIDDLE, IF YOU WOULD LIKE TO DESCEND BELOW:
MY NAME YOU SEEK, IF YOU WISH TO PASS.
I AM HEAD OF THE THEME THAT IS LAST.
ALL SHALL FEAR ME, AND MY CRAFT.
SPEAK, AND ENTER, FOR CONICAL FLASKS.
"""
                self.lift_state = msg

        if not self.lift.locked:
                self.locked = False
                print("The lift takes you to the next room.")

    # Define the escape in this method. This will be triggered once all the puzzles are completed
    def escape(self):
            say("Go east from the lift")
        #self.escape_room("direction", "description of what happens next")
       # e.g  self.escape_room("east","The door slides open reavealing the next room")
