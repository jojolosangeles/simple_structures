from collections import deque

class Jqueue(deque):
    """Jqueue is a very thin wrapper over deque.

    It allows only "enqueue" and "dequeue" operations,
    with the option to queue multiple values in one call,
    or in the constructor"""
    def __init__(self, *args):
        """Examples:  Jqueue(), Jqueue('a'), Jqueue(1,3,8,44)"""
        super().__init__()
        self.enqueue(*args)

    def enqueue(self, *args):
        """Same args as constructor, but also returns self,
        allowing calls to chain:

          q = Jqueue().enqueue(8).enqueue(447)
        """
        for val in args:
            super().append(val)
        return self

    def dequeue(self):
        return super().popleft()
