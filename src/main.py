from adventurelib import say, when, start, Bag
from adventurelib import *
from lock import Lock
from rooms import *

#### Setting up inventories #####
play_inventory = Bag()
current_lock = Bag()


#### Useful verbs ####

@when('examine ITEM')
def examine(item):
    global current_room
    if item in current_room.items:
        current_item = current_room.items.take(item)
        say(current_item)
    else:
        say(f'There is no {item} in this room')

@when('enter KEY')
def enter(key):
    global current_room
    if len(current_lock)==0:
        say("You are not trying any locks. \
            Please enter 'try <lock_name>'")
    else:
        obj=current_lock.take_random()
        obj.unlock(key)
        current_room.test_lock()
        if not current_room.locked:
            current_room.escape()

@when('try LOCK')
def try_lock(lock):
    global current_room
    current_lock.clear()
    if lock in current_room.items:
        obj = current_room.items.take(lock)
        if type(obj) is Lock:
            current_lock.add(obj)
            say(f"Enter the key to unlock {lock}")
        else:
            say(f"{lock} is not a lock.")
    else:
        say(f"There is no {lock} in this room")

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        say(room.room)

@when('where am i')
def whereami():
    say(current_room.room)

def lock_the_room():

    entrance = Entrance()
    staircase =  Staircase()
    store_room =  StoreRoom()
    wet_lab =  WetLab()
    microscope_hall =  MicroscopeHall()

    global current_room



    entrance.room.north = staircase
    staircase.room.south = entrance

    staircase.room.east = store_room
    store_room.room.west = staircase

    store_room.room.north = wet_lab
    wet_lab.room.south = store_room


    wet_lab.room.west = microscope_hall
    microscope_hall.room.east = wet_lab

    microscope_hall.room.west = Room("""Congratulations you have escaped from the Lab!""")

    current_room = entrance
    say(current_room.room)
    print(current_room.room.exits())
    start()