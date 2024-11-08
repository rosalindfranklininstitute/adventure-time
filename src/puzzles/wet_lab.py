from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag, say

class WetLab(EscapeRoom):

    def __init__(self):

        self.name = "wet lab"

        self.room = Room("""You enter a vast lab space. As the special effects smoke clears (nice), you
        see a (mad?) scientist with a llama on a lead. Slightly perplexed, you look around the room
        in case you need to escape quickly, but there's a padlock on the exit door to the west.
        You see a lab bench with a tray and a fridge underneath.
        You take a moment to ponder your life choices before making your next move...
        The scientist looks like he wants to talk to you.
        """)

        self.escape_direction = "west" # escape direction of the room. Do not delete of change this property

        ##### add some items to give clues of the puzzles ###########
        # self.pen = Item("description of item", "item name")
        # self.book = Item("description of item", "item name")
        self.red_syringe = Item("pre-prepared red syringe","red syringe")
        self.blue_syringe = Item("pre-prepared blue syringe","blue syringe")
        self.green_syringe = Item("pre-prepared green syringe","green syringe")
        self.scientist = Item("grizzly but friendly-looking mad scientist", "scientist")
        self.llama = Item("""soft and cuddly llama with black fur and red hooves and a collar with the name alfie. Nice.""", "llama")
        self.carrot = Item("tasty orange snack", "carrot")
        self.tray = Item("tray with red, green and blue syringes", "tray")
        self.fridge = Item("fridge containing a tasty-looking carrot cake and a singular raw carrot", "fridge")
        self.carrot_cake = Item("a tasty-looking carrot cake with white icing. Yum.", "carrot cake")


        ####### add a Lock ###############

        self.locked = True # start with the room locked
        # a lock is defined as Lock("puzzle_answer", "description", "name")
        self.padlock = Lock("2846",
                            "The padlock has a 4 number combination to unlock",
                            "padlock")

        # add as many locks as you like
        # e.g.
        # self.treasure_chest= Lock("answer","description of puzzle", "chest")

        ##### add all you items and locks to an inventory ###########
        self.items = Bag({
            self.padlock, self.red_syringe, self.blue_syringe, self.green_syringe, self.tray, self.carrot_cake, self.scientist, self.llama, self.carrot, self.fridge
            })

    # Unlock the room by setting this test lock method. Once all the locks are open
    # the puzzle can be unlocked. You can implement this method how you like. Delete pass
    # and put your code in the place. An example is in the comments.
    def room_completed(self):
        if self.padlock.locked:
            self.locked=True
        else:
            self.locked=False

    # Define the escape in this method. This will be triggered once all the puzzles are completed
    def escape(self):
        self.locked =False
        say("You push the door, it yields and slowly creeps open to reveal a shadowy room.")
        say(f"Go { self.escape_direction} for next room")

