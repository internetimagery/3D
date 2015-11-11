# Matrix

import group
import vector

def Identity(size):
    num = range(size)
    return Matrix(tuple(tuple(1 if a == b else 0 for b in num) for a in num))

class Matrix(group.Group):
    __slots__ = ()
    rows = property(lambda s: len(s))
    cols = property(lambda s: len(s[0]))
    def __mul__(s, m):
        if type(m) == int or type(m) == float: return s.__class__(tuple(tuple(c * m for c in r) for r in s))
        return s.__class__(tuple(tuple(s.row(r).dot(m.col(c)) for c in range(m.cols)) for r in range(s.rows)))
    def __repr__(s):
        w = s.cols * 2 + 3 # Width
        return (":" * w) + "\n" + "\n".join( "::%s::" % " ".join(str(c) for c in r) for r in s) + "\n" + (":" * w)
    def _determinant(s):
        if s.rows != s.cols: raise ValueError, "Matrix must be square"
        if s.rows == 2: return s[0][0] * s[1][1] - s[0][1] * s[1][0]
        calc = tuple(s[0][top] * s.submatrix(0, top).determinant for top in range(s.rows))
        result = 0
        for i in range(len(calc)):
            result = result - calc[i] if i % 2 else result + calc[i]
        return result
    def __new__(cls, m): return group.Group.__new__(cls, tuple(vector.Vector(r) for r in m))
    def col(s, c): return vector.Vector(r[c] for r in s)
    transpose = property(lambda s: s.__class__(zip(*s)))
    determinant = property(lambda s: s._determinant())
    def row(s, r): return s[r]
    def __div__(s, m): raise NotImplementedError
    def cofactor(s, row, col):
        m = s.submatrix(row, col).determinant
        return +m if row % 2 == col % 2 else -m
    def submatrix(s, row, col): return Matrix(tuple(tuple(s[r][c] for c in range(s.cols) if c != col) for r in range(s.rows) if r != row))

m = Matrix([
    [1,4,7],
    [3,0,5],
    [-1,9,11]
])
sub = m.submatrix(1,2)
print sub.determinant
print m.cofactor(1,2)
# m = Matrix([
#     [1,2,3],
#     [0,4,5],
#     [1,0,6]
# ])
# c = m.minors()
# print c

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
    assert Matrix([[4,6],[3,8]]).determinant == 14
    assert Matrix([[6,1,1],[4,-2,5],[2,8,7]]).determinant == -306
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).determinant == 0
    print "All good."
