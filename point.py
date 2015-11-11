# Point

import group
import vector

class Point(group.Group):
    __slots__ = ()
    def distance(s, v): return vector.Vector(v - s).magnitude

if __name__ == '__main__':
    p1 = Point(1,2,3)
    p2 = Point(3,2,1)
    assert round(p1.distance(p2), 2) == 2.83
    print "All good."
