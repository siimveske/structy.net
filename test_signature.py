import inspect


class Animal:

    _age  = 0
    _size = 0

    def __init__(self, age, size) -> None:
        self._age = age
        self._size = size

def work():
    sig = inspect.signature(Animal.__init__)
    print(sig)


if __name__ == '__main__':
    work()

'''
class PhysicsCommand(omni.kit.commands.Command):
    """wrapper for base omnikit Command class that adds an execute helper to not force the user
    to use only keyword arguments"""
    @classmethod
    def execute(cls, *args, **kwargs):
        sig = inspect.signature(cls.__init__)
        bound = sig.bind(0, *args, **kwargs)
        bound.arguments.pop("self")
        return omni.kit.commands.execute(cls.__name__, **bound.kwargs)
'''
