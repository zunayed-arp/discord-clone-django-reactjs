from types import *


class Utils:
    # python treats strings as iterables; this utility casts a string as a list and ignores iterables

    def listify(arg):
        if Utils.is_sequence(arg) and not isinstance(arg, dict):
            return arg
        return [arg, ]

    def is_sequence(arg):
        if isinstance(arg, str):
            return False
        if hasattr(arg, "__iter__"):
            return True
