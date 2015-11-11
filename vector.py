# Vectors

import math
import group

class Vector(group.Group):
    __slots__ = ()
    def dot(s, v): return sum(s * v)
    def cross(s, v): return s.__class__(
        s[1] * v[2] - s[2] * v[1],
        s[2] * v[0] - s[0] * v[2],
        s[0] * v[1] - s[1] * v[0])
    magnitude = property(lambda s: math.sqrt(sum(s * s))) # |s|
    def __repr__(s): return "Vector: %s" % group.Group.__repr__(s)
    def angle(s, v): return math.degrees(math.acos(s.dot(v) / (s.magnitude * v.magnitude)))
    normalized = property(lambda s: s / ([s.magnitude]*len(s)) if s else s.__class__([0]*len(s)))
    # def mean(s, *v):
    #     for v1 in v: s += v1
    #     return s.__class__(s / ([len(v)]*len(s)))

if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(3,2,1)
    assert v1.dot(v2) == 10
    assert v1.cross(v2) == Vector(-4,8,-4)
    assert round(v1.magnitude, 2) == 3.74
    assert round(v1.angle(v2), 2) == 44.42
    assert v1.normalized < Vector(1,1,1)
    print "All good."
