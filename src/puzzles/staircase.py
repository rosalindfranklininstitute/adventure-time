from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag, say

class Staircase(EscapeRoom):
    def __init__(self):
        self.name = "staircase"
        self.floor_descriptions = [
"""
You find yourself at the foot of a staircase. It looks like it hasn't been used in a hundred years. Wasn't the RFI built more recently than that?
I certiainly don't think that the stairs were built out of wood, and surrounded by torchces. Huh. They must have remodelled over the weekend.
Along the opposite wall to the torches, you see a picture of Mass Spectrometry image of a brain, an electron microscope, and a 96 well plate.
At the top of the flight of stairs, you see a sign for the Mass Spectrometry theme. Since when do they get their own floor?
To your right you see a lift with the doors already open.
""",

"""
You find yourself at the foot of another flight of stairs. There are ten pictures along the wall, and the penultimate is a microscope.
At the top of the stairs you see a sign for the theme of Correlated Imaging. I thought they had to share a floor too?
""",

"""
You find youself at the foot of another flight of stairs. There are ten more pictures.
You spend a while looking at a lovely landscape before realising that you should move on. You've stayed here too long.
The second picture was much more boring so it's fine, it was just a server rack or something.
At the top you see a sign for the Artificial Intelligence theme.
""",

"""
You find yourself at the foot of another flight of stairs. There are more pictures and another sign.
The sign is for Structural Biology this time. You're starting to notice the themes. It's a shame that this staircase doesn't have pictures of llamas.
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
        self.lift = Lock("mendeleev",
                         "There is surprisingly a high tech lift in the corner. It has a buttons for the floors and a basement",
                         "lift")

        self.pictures = Item("A code lies within us, over all floors, ascend to find out more", "pictures")

        # add as many locks as you like
        # e.g.
        # self.treasure_chest= Lock("answer","description of puzzle", "chest")

        ##### add all you items and locks to an inventory ###########
        self.items = Bag({self.keypad, self.lift, self.pictures})



    # Unlock the room by setting this test lock method. Once all the locks are open
    # the puzzle can be unlocked. You can implement this method how you like. Delete pass
    # and put your code in the place. An example is in the comments.
    def room_completed(self):
        if not self.keypad.locked:
                say("The lift sounds like it is working now.")
                msg = \
                        """
                        A booming voice shouts out: \n
                        MY NAME YOU SEEK, IF YOU WISH TO PASS. \n
                        I INVENTED AN ITEM YOU NEED IN CHEMISTRY CLASS. \n
                        NOT FURNITURE, BUT STILL KNOWN AS A TABLE. \n
                        CONTAINS ALL ELEMENTS, ROBUST AND UNSTABLE. \n
                        """
                self.lift_state = msg

        if not self.lift.locked:
                self.locked = False
                print("The lift descends to the basement, taking you to the next floor.")

    # Define the escape in this method. This will be triggered once all the puzzles are completed
    def escape(self):
            say("Here is Chemistry. The floor is well lit and modern, but the doors to the labs are access controlled. There are another set of doors to the east , where do they lead?")
        #self.escape_room("direction", "description of what happens next")
       # e.g  self.escape_room("east","The door slides open reavealing the next room")
