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


