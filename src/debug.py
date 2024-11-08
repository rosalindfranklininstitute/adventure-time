from adventurelib import say, when, start, Bag
from adventurelib import *
from lock import Lock
from puzzles import *

########### Setting up inventories ##################

player_inventory = Bag() # Players can add Items to their bag
current_lock = Bag() # special bag that only contains the current lock the player is trying to solve

############ Define Player Actions #################

@when('examine ITEM')
def examine(item):
    """T
    Enter 'examine <item_name>' into game prompt to get the description of items in a room. e.g. > examine box

    Args:
        item (str): the name of the item.
    """

    if item in current_puzzle.items:
        current_item = current_puzzle.items.find(item)
        say(current_item)
    else:
        say(f'There is no {item} in this room')

@when('enter KEY')
def enter(key):
    """
    Enter 'enter <key>' into game prompt to try and unlock a lock, e.g. > enter abc
    The lock is defined in the puzzle. This function uses the Lock.unlock() function
    to return an answer

    Args:
        key (str): the code or item to unlock the lock.
    """
    if len(current_lock)==0:
        say("You are not trying any locks. \
            Please enter 'try <lock_name>'")
    else:
        obj=current_lock.take_random()
        obj.unlock(key)
        current_puzzle.room_completed()
        if not current_puzzle.locked:
            current_puzzle.escape()

@when('try LOCK')
def try_lock(lock):
    """
    Enter 'try <lock_name>' into the game prompt select the lock to solve. Returns prompt for the lock.


    Args:
        lock (str): name of lock
    """
    current_lock.clear()
    if lock in current_puzzle.items:
        obj = current_puzzle.items.find(lock)
        if type(obj) is Lock:
            current_lock.add(obj)
            say(f"Enter the key to unlock {lock}")
        else:
            say(f"{lock} is not a lock.")
    else:
        say(f"There is no {lock} in this room")

@when('go north', direction='north')
@when('go south', direction='south')
@when('go east', direction='east')
@when('go west', direction='west')
def go(direction):
    """
    Type 'go <direction>' in the game prompt to move in that direction.
       You can only exit from a particular direction, which will lead to another room.
       If a room is locked you will not be able to go in that direction.

    Args:
        direction (str): the direction to move in
    """
    global current_puzzle
    room = current_puzzle.room.exit(direction)
    if room:
        if current_puzzle.locked:
            say(f"You cannot go {direction}. The room is locked")
        else:
            current_puzzle = room
            say("You go %s." % direction)
            say(room.room)
    else:
        say(f"There is no exit to the {direction}")

@when('is it open')
def is_open():
    """
    Type 'is it open' into game prompt to find out if a room is open.
    Returns state of the room.
    """
    if current_puzzle.locked:
        say("The room is locked, continue to solve puzzles to unlock the room")
    else:
        say( "The room is open")

@when('where am i')
def whereami():
    """
    Enter 'where am i' into the game prompt to find the description of the you are in
    """
    say(current_puzzle.room)


############################## Game Loop ##########################################
def lock_the_room():

    ######################### Add Puzzles #########################

    my_puzzle = Entrance() # change this to be the name of your puzzle

    ############### Add directional relationship #################

    # This allows you to test escaping to another room
    finish_room = Finish()

    my_puzzle.room.north = finish_room  # You need to edit this line so it has the escape direction of your room
    #e.g my_puzzle.room.west = finish_room

    #############  Set start room and start game ####################
    global current_puzzle
    current_puzzle = my_puzzle
    say(current_puzzle.room)
    start()