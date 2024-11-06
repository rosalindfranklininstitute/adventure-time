from importlib.metadata import entry_points
from adventurelib import say, when, start, Bag
from lock import Lock

#### Setting up inventories #####
play_inventory = Bag()
current_lock = Bag()
#### Useful verbs ####

@when('examine ITEM')
def examine(item):
    if item in current_room.items:
        current_item = current_room.items.take(item)
        say(current_item)
    else:
        say(f'There is no {item} in this room')

@when('enter KEY')
def enter(key):
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



def lock_the_room():
    discovered_rooms = [ e.load() for e in entry_points(group="rooms")]

    for room in discovered_rooms:
        global current_room
        current_room = room()
        current_room.play_room()
        # ctr-c to  break)


    start()