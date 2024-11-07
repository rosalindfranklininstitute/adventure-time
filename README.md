─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████████████─██████████████─██████████████────██████████████─██████──██████─██████████████────██████─────────██████████████─██████████████───
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██────██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██───
─██░░██████████─██░░██████████─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████████────██████░░██████─██░░██──██░░██─██░░██████████────██░░██─────────██░░██████░░██─██░░██████░░██───
─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██────────────────██░░██─────██░░██──██░░██─██░░██────────────██░░██─────────██░░██──██░░██─██░░██──██░░██───
─██░░██████████─██░░██████████─██░░██─────────██░░██████░░██─██░░██████░░██─██░░██████████────────██░░██─────██░░██████░░██─██░░██████████────██░░██─────────██░░██████░░██─██░░██████░░████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██────────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██────██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░░░██─
─██░░██████████─██████████░░██─██░░██─────────██░░██████░░██─██░░██████████─██░░██████████────────██░░██─────██░░██████░░██─██░░██████████────██░░██─────────██░░██████░░██─██░░████████░░██─
─██░░██─────────────────██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██────────────────██░░██─────██░░██──██░░██─██░░██────────────██░░██─────────██░░██──██░░██─██░░██────██░░██─
─██░░██████████─██████████░░██─██░░██████████─██░░██──██░░██─██░░██─────────██░░██████████────────██░░██─────██░░██──██░░██─██░░██████████────██░░██████████─██░░██──██░░██─██░░████████░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██────────██░░██─────██░░██──██░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─
─██████████████─██████████████─██████████████─██████──██████─██████─────────██████████████────────██████─────██████──██████─██████████████────██████████████─██████──██████─████████████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Text-based adventure with a modern twist! Build an escape room where to exit you have to solve a series of puzzles.
This game uses the package `adventurelib` which provides nice decorators and classes for easily writing text based adventure games.
This project is designed to be used as a team building activity, where each team creates a puzzle and together you build a set of
escape rooms for another team to play.

# Developers

## Getting started

In the lab there are 6 puzzles that follow this map:


[ Map ](docs/Escape_Room_Map.png)


Puzzles contain a Room, Items and Locks. A puzzle can contain as many Items and Locks as you wish, but can only contain a single Room. If you define more than one Room variable then your
puzzle will not play correctly. Each puzzle has an `escape_direction` which corresponds to the direction you need to go to make it to the next room. Please do not change this variable as the map
is set. The flow of play is indicated on the map. There are two special puzzles the Entrance and the Finish. Entrance is a prepopulated example to show you how to set puzzle and the Finish puzzle is
an unlocked puzzle which lets the user finish the game.

When a player has completed all the Locks in a puzzle, the room unlocks and the player can move onto the next room. When a room is locked a player cannot move in any direction, including the direction
they came from until the room has been played through. Only when all the puzzles are complete can a player move through the entire Lab.

## Playing the Game

To play the game:
1. clone the repository
2. `pip install .` in the `adventure-time` folder
3. Once the game has been installed type `adventure-time` in the terminal and the game entrance and prompt will appear.

You can find what commands you can run in the game by typing `help` into the game prompt.
To exit the game, type `quit` into the game prompt.

### Development mode

To play the game in development mode use `pip intall -e .`. You can make changes to the code which will be entered into the game every time you launch `adventure-time`.
You can also test your room by playing in debug mode. To play in debug mode type `adventure-time-debug` into the console. The debug mode allows you to play a single puzzle,
and not work your way through the rooms.  You can edit the `debug.py` file to play the puzzle you are developing and test that the methods are working.

## The Game Playing script

They game playing script is based on

## Creating your Puzzle

You can create your puzzle by editing the puzzle files in `src/puzzles`. (advanced) The puzzles are each based on the `EscapeRoom` metaclass, if you don't know what this means don't worry.
Open a file for a puzzle and they all have the same layout.

Starting at the top:

### Import statements

```
from escape_room import EscapeRoom
from lock import Lock
from adventurelib import Room, Item, Bag
```
These statments import the objects needed for Game Play . If you want to import more packages please use them here. If you want to use more functions from `adventurelib` please add the line `from adventurelib import *`.
Please note you CANNOT use the `@when` decorator from `adventurelib` in the Puzzle class. For more information on how to add player actions see here.

### Define your room
Next you need to define your puzzle Room:
```
    def __init__(self):
        self.name = "staircase"

        self.room = Room("""Enter the description of your room here""")
```
All you need to do is delete the text between the three quotation marks and enter the description of the room. Don't delete the quotations. You can be as descriptive as you like, the more descriptive the better. There is no limit of characters, but don't bore your audience. e.g.
```
    def __init__(self):
        self.name = "entrance"

        self.room = Room(""" You have entered an entrance hall.
                                It has a high vaulted ceiling and there is an ancient desk in the corner, papers scattered over its surface.
                                Above the desk is a clock, it has stopped. No one has been here for years. In
                                the north you see a pair of double doors and a key pad."""
```
### Define your Items

Now you can add items to your room. An item is defined by a description and a name. In the puzzle file an example of this commented out, but gives an example of how to implement items. You can edit this section
by deleting the # and writing your description and names in the quotations. You can also change the name of the item , but make sure you keep the `self.` in front of it.
```
# self.pen = Item("description of item", "item name")
# self.book = Item("description of item", "item name")
```


Players of your game can `examine` these items. When they do this command the description of your item appears.
Use items to create clues and descriptions for you puzzle.

For example:
```
self.clock = Item("The clocks hands are stuck at 17 minutes past 11", "clock")
self.papers = Item("The papers are a manuscript of a book. The title reads: 'Stopped Time Unlocks Doors'", "papers")
self.desk = Item("There is an old mahogany desk, with yellowing papers scattered on the surface", "desk")
```
The first two items: `clock` and `papers`, give the player clues to the puzzle. The third item, `desk`, is a purely descriptive item to slow game progress.

When the player enters into the game prompt
```
examine clock
```
They will get the following returned:
```
The clocks hands are stuck at 17 minutes past 11
```

### Defining you Locks and unlocking the room

Locks are a special type of item. They have all the same properties of Items and an extra property which is the answer you need to unlock them. To escape from the room you first need to unlock all the locks.
The first thing you need to do is define your lock in the same way that you define your item giving the extra answer field.
e.g.
```
self.padlock = Lock("9999",
                            "The padlock has a 4 number combination to unlock",
                            "padlock")

```


