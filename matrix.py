# Matrix

import group
import vector

def Identity(size):
    num = range(size)
    return Matrix(tuple(tuple(1 if a == b else 0 for b in num) for a in num))

class Matrix(group.Group):
    __slots__ = ()
    rows = None
    cols = None
    def __mul__(s, m):
        if type(m) == int or type(m) == float: return s.__class__(tuple(tuple(c * m for c in r) for r in s))
        return s.__class__(tuple(tuple(s.row(r).dot(m.col(c)) for c in range(m.cols)) for r in range(s.rows)))
    def __repr__(s):
        w = s.cols * 2 + 3 # Width
        return (":" * w) + "\n" + "\n".join( "::%s::" % " ".join(str(c) for c in r) for r in s) + "\n" + (":" * w)
    transpose = property(lambda s: s.__class__(zip(*s)))
    def col(s, c): return vector.Vector(r[c] for r in s)
    def __new__(s, m):
        m = tuple(vector.Vector(r) for r in m)
        s.rows = len(m); s.cols = len(m[0])
        return group.Group.__new__(s, m)
    def row(s, r): return s[r]

if __name__ == '__main__':
    m1 = Matrix([
        [1,2,3],
        [3,2,1]
    ])
    m2 = Matrix([
        [3,2,1],
        [1,2,3]
    ])
    m3 = Identity(3)
    assert m1 == m1
    assert m1 != m2
    assert m1.transpose == Matrix([[1,3], [2,2], [3,1]])
    assert -m1 == Matrix([[-1,-2,-3],[-3,-2,-1]])
    assert m1 * 2 == Matrix([[2,4,6],[6,4,2]])
    assert m1 + 2 == Matrix([[3,4,5],[5,4,3]])
    assert not Matrix([[0,0,0],[0,0,0]])
    assert m1 * m2 == Matrix([[5,6,7],[11,10,9]])
    assert m3 == Matrix([[1,0,0],[0,1,0],[0,0,1]])
    print "All good."
