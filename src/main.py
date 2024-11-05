from importlib.metadata import entry_points
from adventurelib import start

def lock_the_room():
    discovered_rooms = [ e.load() for e in entry_points(group="rooms")]
    print(discovered_rooms)

    for room in discovered_rooms:
        room.play_room()
        # ctr-c to break
    start()