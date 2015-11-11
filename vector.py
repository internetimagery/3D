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
    def __new__(s, *args): return tuple.__new__(s, args[0] if len(args) == 1 else args)
    def angle(s, v): return math.degrees(math.acos(s.dot(v) / (s.magnitude * v.magnitude)))
    normalized = property(lambda s: s / ([s.magnitude]*len(s)) if s else s.__class__([0]*len(s)))
    # def mean(s, *v):
    #     for v1 in v: s += v1
    #     return s.__class__(s / ([len(v)]*len(s)))
#
if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(3,2,1)
