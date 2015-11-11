# Generic grouping

class Group(tuple):
    __slots__ = ()
    def __neg__(s): return s.__class__(-a for a in s)
    def __pos__(s): return s.__class__(+a for a in s)
    def __ne__(s, v): return False if s == v else True
    def __nonzero__(s): return 1 != len(set(a for a in s if not a))
    def __add__(s, v): return s.__class__(a + b for a, b in zip(s, s._scale(v)))
    def __div__(s, v): return s.__class__(a / b for a, b in zip(s, s._scale(v)))
    def __mod__(s, v): return s.__class__(a % b for a, b in zip(s, s._scale(v)))
    def __mul__(s, v): return s.__class__(a * b for a, b in zip(s, s._scale(v)))
    def __sub__(s, v): return s.__class__(a - b for a, b in zip(s, s._scale(v)))
    def __pow__(s, v): return s.__class__(a ** b for a, b in zip(s, s._scale(v)))
    def __lt__(s, v): return False not in set(a < b for a, b in zip(s, s._scale(v)))
    def __gt__(s, v): return False not in set(a > b for a, b in zip(s, s._scale(v)))
    def __truediv__(s, v): return s.__class__(a / b for a, b in zip(s, s._scale(v)))
    def __eq__(s, v): return False not in set(a == b for a, b in zip(s, s._scale(v)))
    def __le__(s, v): return False not in set(a <= b for a, b in zip(s, s._scale(v)))
    def __ge__(s, v): return False not in set(a >= b for a, b in zip(s, s._scale(v)))
    def __floordiv__(s, v): return s.__class__(a // b for a, b in zip(s, s._scale(v)))
    def __new__(s, *args): return tuple.__new__(s, args[0] if len(args) == 1 else args)
    def _scale(s, v): return [v]*len(s) if type(v) == int or type(v) == float else v

if __name__ == '__main__':
    g1 = Group((1,2,3))
    g2 = Group((3,2,1))
    assert g1 == g1
    assert g1 != g2
    assert -g1 == (-1,-2,-3)
    assert +g1 == g1
    assert not Group((0,0,0))
    assert g1 + g2 == Group((4,4,4))
    assert g2 - g1 == Group((2,0,-2))
    assert g1 * g2 == Group((3,4,3))
    assert g1 / g2 == Group((0,1,3))
    assert g1 ** 2 == Group((1,4,9))
    g3 = g1 + g2
    assert g1 < g3
    assert g3 > g1
    print "All good!"
