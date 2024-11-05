from importlib.metadata import entry_points
from adventurelib import *

def lock_the_room():
    discovered_rooms = [ e.load() for e in entry_points(group="rooms")]

    for room in discovered_rooms:
        room.play_room()
        # ctr-c to break


    start()