from importlib.metadata import entry_points
from adventurelib import *



#### Useful verbs ####

@when('examine ITEM')
def examine(item):
    if item in current_room.items:
        current_item = current_room.items.take(item)
        say(current_item)
    else:
        say(f'There is no {item} in this room')


def lock_the_room():
    discovered_rooms = [ e.load() for e in entry_points(group="rooms")]




    for room in discovered_rooms:
        global current_room
        current_room = room()
        current_room.play_room()
        # ctr-c to  break)





    start()