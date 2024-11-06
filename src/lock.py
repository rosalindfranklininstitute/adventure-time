from adventurelib import Item, say

class Lock(Item):
    def __init__(self, answer, name, *aliases):
        super().__init__(name, *aliases)
        self.locked = True
        self.answer= answer

    def unlock(self,
                input,
                success_message="The answer is correct. You have unlocked the lock",
                failure_message="The lock remains shut, try again"):
        if input == self.answer:
            self.locked=False
            say( success_message)
        else:
            say(failure_message)
