from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag

class StoreRoom(EscapeRoom):

    def __init__(self):

        self.name = "storeroom"

        self.room = Room(
                """
                You walk into a dimly lit storeroom. The dust that fills your lungs tells that this room hasn't been opened in many years.
                You pull a crusty string beside you and a flickering light reveals a small, crowded room filled with cupboards and boxes.
                The items inside the boxes range from old monitors to unlabelled jars with gooey substances, some glowing and other not.
                Out of the corner of your eye, you spot a large spider, watching you. The spider hisses at you when you go closer


                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢉⡉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⣉⣥⣤⣤⣶⣶⣶⣦⣤⣤⣉⡉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⣉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⡿⠛⢁⣠⣶⣿⣿⣿⣿⣶⣤⡈⠛⢿⣿⣿⠿⠋⣁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡉⠻⢿⣿⣿⠟⠉⣠⣴⣾⣿⣿⣿⣷⣦⣄⠙⠻⣿⣿⣿⣿⣿
                ⣿⣿⡿⠉⣠⡾⠟⠋⣉⣁⣀⣈⠙⠻⣿⣿⣷⣄⠉⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠉⢀⣴⣿⣿⠿⠟⢉⣀⣀⣉⡉⠛⠷⣦⡈⠻⣿⣿⣿
                ⣿⣿⠀⠈⢁⣤⣾⣿⣿⣿⣿⣿⣿⣦⣄⠙⠿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠻⠟⢁⣴⣾⣿⣿⣿⣿⣿⣷⣦⣄⠙⠀⢸⣿⣿
                ⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿
                ⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢹⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⡟⠁⣠⣶⣶⣶⣶⣶⣦⣤⣈⡁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣉⣠⣤⣶⣶⣶⣶⣶⣦⣀⠙⣿⣿⣿⣿
                ⣿⣿⠋⣠⣾⡿⠟⠛⠛⠛⠿⠿⠿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡿⠿⠿⠟⠛⠛⠛⢿⣿⣦⠀⢻⣿⣿
                ⡿⠃⣴⡿⠋⣠⣶⣿⣿⣿⣿⣶⣤⣤⡀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠛⢋⣁⣠⣤⣤⣤⣤⣤⣤⣄⣉⡛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣠⣤⣶⣾⣿⣿⣿⣷⣤⡈⠻⣷⡀⢹⣿
                ⠃⣸⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⡿⠋⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣈⠙⠻⣿⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⢷⡀⢿
                ⠀⠁⣰⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠓⠀⢿⣿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠈⢻⣿⣿⣿⠃⠘⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣷⡈⠃⢸
                ⣿⣿⣿⣿⣿⣿⡿⠋⣀⣤⣶⣶⣾⣿⣿⣧⠈⢿⠃⣰⣿⣿⠟⢁⣀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠻⣿⠏⣠⣿⣿⣿⣶⣶⣦⣄⡈⢻⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⡿⠁⣼⣿⡿⠿⠛⠛⢛⣛⣛⡃⠀⣰⣿⣿⡇⢰⣿⠁⠀⢼⣿⡆⠹⣿⣿⣿⣿⡟⢉⣀⡀⠀⢄⠉⢻⣿⣿⡀⠉⢀⣛⣛⣛⠛⠛⠻⠿⣿⣷⡀⢹⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⠃⣸⣿⠋⣠⣶⣿⣿⣿⣿⣿⡏⢀⣿⣿⣿⡇⠹⣿⣄⠀⠀⠀⠀⢰⣿⣿⣿⣿⠀⠘⠯⠃⠀⢸⣷⠀⣿⣿⣧⠈⢿⣿⣿⣿⣿⣿⣷⣦⠈⢿⣷⡀⢿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⡟⢠⡿⠁⣰⣿⣿⣿⣿⣿⣿⠟⠁⠸⣿⣿⣿⣷⣄⠙⠛⠿⠒⠉⣠⣿⣿⣿⣿⣿⠀⢄⡀⢀⣠⣾⡿⠀⣿⣿⣿⠀⡄⠙⢿⣿⣿⣿⣿⣿⣷⡀⢻⣇⠈⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⠁⢸⠃⣸⣿⣿⣿⣿⣿⣿⠃⣠⣧⠀⢿⣿⣿⣿⣿⣿⣶⣶⣶⡿⢻⣦⣾⣿⣉⣹⣷⣄⠙⠛⠛⠋⣠⣾⣿⣿⣿⠀⣿⣦⠈⢻⣿⣿⣿⣿⣿⣷⠀⢻⠀⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣄⠈⢠⣿⣿⣿⣿⣿⣿⠃⣰⣿⡿⠃⡈⠻⣿⣿⣿⣿⣿⣟⣋⠀⡈⠛⠿⠿⠿⠗⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢻⣿⣷⠀⢻⣿⣿⣿⣿⣿⣧⡈⢀⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢰⣿⣿⠃⣰⣷⣦⡈⠛⠿⣿⣿⣿⣿⣦⣁⣴⣶⣶⡀⢂⣤⣤⣿⣿⣿⣿⣿⣿⣿⠏⢀⣶⡀⢿⣿⣧⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠏⢰⣿⣿⣿⣿⣷⣦⣄⣉⡙⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠋⣀⣴⣿⣿⣧⠈⣿⣿⡆⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣿⣿⣿⣿⣿⡟⢀⣿⣿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠹⣿⡄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣾⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠘⢿⣄⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⡾⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡙⠣⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠰⠋⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                """
        )

        self.escape_direction = "north" # escape direction of the room. Do not delete of change this property

        ##### add some items to give clues of the puzzles ###########
        self.spider = Item(
                "A spider looms, its jet black body absorbing the light, casting an unsettling shadow. Its eyes glint with an unnatural intelligence, dark and watchful, as if peering straight into your soul. It has pincers long and razor-sharp, and it hovers over an impressive network of spider webs circling the entire room. You listen carefully to the spiders's hiss.\n < hiss hiss ...... hiss hiss hiss hiss hiss ...... hiss hiss hiss hiss hiss hiss... > \n It's eyes now glare INTENSELY between two objects, the door to the exit and a cupboard in the corner of the room. The spider scutters away out of sight.",
                "spider"
                )
        self.tome = Item(
                "The old book rests with a cracked, faded leather cover and yellow pages that smell faintly musty. The spine is worn and each delicate page whispers softly, holding secrets from long ago. As you open the cover of the tome, and flip the pages. Most of the pages are stuck together, apart from pages 3, 6, 12.",
                "tome"
                )
        self.page3 = Item(
                "This page doesn't seem to include any useful information",
                "page 3",
        )
        self.page6 = Item(
                "This page doesn't seem to include any useful information",
                "page 6",
        )
        self.page12 = Item(
                "As you turn to this page, you notice the spider reappear and hiss at you again. At the top of the page, there's a date: 24th January 1939",
                "page 12",
        )
        self.exitdoor = Item(
                "There is another keypad, this time with 6 digits",
                "exit"
        )
        self.cupboard = Item(
                "A spooky cupboard stands in the corner, its dark wood weathered and creaking, with dusty shadowed shelves cloaked in cobwebs. It's locked with a padlock",
                "cupboard",
                )


        ####### add a Lock ###############

        self.locked = True # start with the room locked
        # a lock is defined as Lock("puzzle_answer", "description", "name")
        self.keypad = Lock(
                "390124",
                "The keypad has a 6 number combination to unlock",
                "keypad"
        )
        self.padlock = Lock(
                "256",
                "The cupboard is locked with a padlock with a 3-digit code",
                "padlock"
        )

        # add as many locks as you like
        # e.g.
        # self.treasure_chest= Lock("answer","description of puzzle", "chest")

        ##### add all you items and locks to an inventory ###########
        self.items = Bag({
                self.spider,
                self.tome,
                self.page3,
                self.page6,
                self.page12,
                self.exitdoor,
                self.keypad,
                self.padlock,
                self.cupboard,
        })

    # Unlock the room by setting this test lock method. Once all the locks are open
    # the puzzle can be unlocked. You can implement this method how you like. Delete pass
    # and put your code in the place. An example is in the comments.
    def room_completed(self):
        #e.g.
        # if self.padlock.locked:
        #     self.locked=True
        # else:
        #     self.locked=False

        if self.padlock.locked and self.keypad.locked:
                self.locked = True
                print("The cupboard is locked")
        elif not self.padlock.locked and self.keypad.locked:
                self.locked = True
                print("As you enter the code, the cupboard doors swing open and the only thing inside is a leather bound old tome")
                print("The exit remains locked ")
        else:
                self.locked = False

    # Define the escape in this method. This will be triggered once all the puzzles are completed
    def escape(self):
        print("The door opens, the spider squawks with joy and returns to settle in the centre of its web")



