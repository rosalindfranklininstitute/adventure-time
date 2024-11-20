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

@when('take ITEM')
def take(item):
    TAKEABLE = ("carrot cake", "carrot", "red syringe", "blue syringe", "green syringe")

    if item not in TAKEABLE:
        say("You can't take that!")
        return

    obj = current_puzzle.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        player_inventory.add(obj)
    else:
        say('There is no %s here.' % item)

@when('talk to ITEM')
def talk_to(item):
    if item == "scientist":
        say("I really need help to immunise this llama. He won't stay still! If you help me with that, I'll give you the code to escape.")
    else:
        say("You can't talk to that, silly!")

@when('immunise ITEM')
def immunise(item):
    if item == "scientist":
        say("I don't think he'd like that!")
        return
    elif item != "llama":
        say("You can't immunise that!")
        return

    if "red syringe" not in player_inventory:
        say("You'll need the correct colour syringe for that.")
        return

    if "carrot" not in player_inventory:
        if "carrot cake" in player_inventory:
            say("The llama sniffs at the cake, but turns his nose up at it and spits at you. Typical.")
            return
        say("The llama refuses to stay still. Maybe you can placate him a carrot-based snack?")
        return

    say("You inject the llama with the red syringe. 'Thank you so much!' says the scientist. 'The code for the door is 2846'.")

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
            if lock =='lift':
                say(current_puzzle.lift_state)
        else:
            say(f"{lock} is not a lock.")
    else:
        say(f"There is no {lock} in this room")


@when('ascend')
def ascend():
    """
    Used for staircase puzzle
    """
    global current_puzzle
    if not isinstance(current_puzzle, Staircase):
        print("Cannot ascend in this room.")
    else:
        if current_puzzle.floor < 4:
            current_puzzle.floor += 1
            print(current_puzzle.floor_descriptions[current_puzzle.floor])
        else:
            print("Cannot ascend")


@when('descend')
def descend():
    """
    Used for staircase puzzle
    """
    global current_puzzle
    if not isinstance(current_puzzle, Staircase):
        print("Cannot ascend in this room.")
    else:
        if current_puzzle.floor > 0:
            current_puzzle.floor -= 1
            print(current_puzzle.floor_descriptions[current_puzzle.floor])
        else:
            print("Cannot descend")

@when('look')
def look():
    if current_puzzle.items:
        for i in current_puzzle.items:
            item_name = i.aliases[-1]
            if item_name[-1] == 's':
                say(f'Some {item_name} are here')
            else:
                say(f'A {item_name} is here')

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

    entrance = Entrance()
    staircase =  Staircase()
    store_room =  StoreRoom()
    wet_lab =  WetLab()
    microscope_hall =  MicroscopeHall()

    ############### Add directional relationship #################

    entrance.room.north = staircase
    staircase.room.south = entrance

    staircase.room.east = store_room
    store_room.room.west = staircase

    store_room.room.north = wet_lab
    wet_lab.room.south = store_room


    wet_lab.room.west = microscope_hall
    microscope_hall.room.east = wet_lab

    microscope_hall.room.north = Finish()

    #############  Set start room and start game ####################
    global current_puzzle
    current_puzzle = entrance
    say(current_puzzle.room)
    start()
