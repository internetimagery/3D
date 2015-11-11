# Matrix

import group
import vector

def Identity(size):
    num = range(size)
    return Matrix(tuple(tuple(1 if a == b else 0 for b in num) for a in num))

class Matrix(group.Group):
    # __slots__ = ()
    def __new__(s, m):
        m = tuple(vector.Vector(r) for r in m)
        s.rows = len(m); s.cols = len(m[0])
        return group.Group.__new__(s, m)
    def __repr__(s):
        w = s.cols * 2 + 3 # Width
        return (":" * w) + "\n" + "\n".join( "::%s::" % " ".join(str(c) for c in r) for r in s) + "\n" + (":" * w)
    def row(s, r): return s[r]
    def col(s, c): return vector.Vector(r[c] for r in s)
    transpose = property(lambda s: s.__class__(zip(*s)))

if __name__ == '__main__':
    m1 = Matrix([
        [1,2,3],
        [3,2,1]
    ])
    m2 = Matrix([
        [3,2,1],
        [1,2,3]
    ])
    m3 = Matrix([
        [1,3], [2,2], [3,1]
    ])
    assert m1 == m1
    assert m1 != m2
    assert m1.transpose == m3
    assert -m1 == Matrix([[-1,-2,-3],[-3,-2,-1]])
    assert m1 * 2 == Matrix([[2,4,6],[6,4,2]])
    assert not Matrix([[0,0,0],[0,0,0]])

#     def __mul__(s, m): return s.__class__(tuple(tuple(sum([a * b for a, b in zip(s.rows[r], m.cols[c])]) for c in m.col) for r in s.row))


#     # def _inv(s):
#     #     num = range(len(s.row)); num.reverse()
#     #     if len(s.row) != len(s.col): raise ValueError, "Matrix must be a square."
#     #     return s.__class__(tuple(tuple((r,c) for c in num) for r in num))
#     # inverse = property(lambda s: s._inv())
#
