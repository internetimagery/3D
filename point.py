# Point

import group

class Point(group.Group):
    __slots__ = ()
    def distance(s, v): return Vector(v - s).magnitude
    def __new__(s, *args): return tuple.__new__(s, args[0] if len(args) == 1 else args)
