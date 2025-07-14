from functools import wraps


class Signal:
    def __init__(self):
        self.callables = []

    def trigger(self, context):
        for f in self.callables:
            f(context)

    def register(self, callable):
        self.callables.append(callable)
        return callable

