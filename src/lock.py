from adventurelib import Item

class Lock(Item):
    def __init__(self, answer, name, *aliases):
        super().__init__(name, *aliases)
        self.locked = True
        self.answer= answer

    def unlock(self, input):
        if input == self.answer:
            self.locked=False
