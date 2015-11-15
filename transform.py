# Transformation Matrix

import math
import itertools

def sZip(m1, m2):
    """
    Allow Scalar Operations.
    """
    try:
        return zip(m1, m2)
    except TypeError:
        return zip(m1, itertools.repeat(m2))

def test(m1, m2, func):
    """
    Test Matrix for truthiness.
    """
    for a, b in sZip(m1, m2):
        for c, d in sZip(a, b):
            if func(c, d): return True
    return False

class Transform(tuple):
    """
    Transformation Matrix

    Transform() <--- Identity
    Transform(
        [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10,11,12],
        [13,14,15,16]
        ) <--- By Row
    Transform(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) <--- a11, a12, a13, a21, a22, ... etc
    Transform(tuple(c+r for c in range(4)) for r in range(1,17,4)) <--- generator / nested iterable
    """
    __slots__ = ()
    cols = 4
    rows = 4
    def __new__(cls, *nums):
        try:
            l = len(nums)
            if l == 16: # Full array of numbers
                return tuple.__new__(cls, (nums[r:r+4] for r in range(0,16,4)))
            if l == 4: # Creation by rows
                return tuple.__new__(cls, nums)
            if l == 1: # Iterable / Another matrix
                return tuple.__new__(cls, nums[0])
            if l == 0: # Empty Matrix / Identity Matrix
                return tuple.__new__(cls, (tuple(1.0 if c == r else 0.0 for c in range(4)) for r in range(4)))
            raise Exception
        except:
            raise ValueError, "Invalid arguments for Matrix."
    def __repr__(s):
        string = tuple(tuple(str(b) for b in a) for a in s)
        col = max(max(len(b) for b in a) for a in string)
        return "\n".join(" ".join(b.center(col) for b in a) for a in string)
    # Basic Math Operations
    def __truediv__(s, m): return s.__div__(m)
    def __ne__(s, m): return False if s == m else True
    def __neg__(s): return s.__class__(tuple(-b for b in a) for a in s)
    def __pos__(s): return s.__class__(tuple(+b for b in a) for a in s)
    def __add__(s, m): return s.__class__(tuple(c + d for c, d in sZip(a, b)) for a, b in sZip(s, m))
    def __sub__(s, m): return s.__class__(tuple(c - d for c, d in sZip(a, b)) for a, b in sZip(s, m))
    def __nonzero__(s): return True if tuple(b for a in s for b in a if b) else False
    def __mod__(s, m): return s.__class__(tuple(c % d for c, d in sZip(a, b)) for a, b in sZip(s, m))
    def __pow__(s, m): return s.__class__(tuple(c ** d for c, d in sZip(a, b)) for a, b in sZip(s, m))
    def __floordiv__(s, m): return s.__class__(tuple(c // d for c, d in sZip(a, b)) for a, b in sZip(s, m))
    def __lt__(s, m): return test(s, m, lambda a, b: a < b)
    def __gt__(s, m): return test(s, m, lambda a, b: a > b)
    def __le__(s, m): return test(s, m, lambda a, b: a <= b)
    def __ge__(s, m): return test(s, m, lambda a, b: a >= b)
    def __eq__(s, m): return test(s, m, lambda a, b: a == b)

    def __mul__(s, m):
        try:
            return s.__class__(tuple(c * d for c, d in zip(a, b)) for a, b in zip(s, m.transpose))
        except AttributeError:
            return s.__class__(tuple(c * d for c, d in sZip(a, b)) for a, b in sZip(s, m))
    #     if type(m) == int or type(m) == float: return s.__class__(tuple(tuple(c * m for c in r) for r in s))
    #     return s.__class__(tuple(tuple(s.row(r).dot(m.col(c)) for c in range(m.cols)) for r in range(s.rows)))

    @property
    def transpose(s): return s.__class__(zip(*s))
    def __div__(s, v): return s.__class__(a / b for a, b in sZip(s, v))


t1 = Transform()
t2 = Transform(
    (1,2,3,4),
    (5,6,7,8),
    (10,11,12,13),
    (14,15,16,17)
)
t3 = t1 + 5
print t1 * 4
    #
    # def __mul__(s, m):
    #     if type(m) == int or type(m) == float: return s.__class__(tuple(tuple(c * m for c in r) for r in s))
    #     return s.__class__(tuple(tuple(s.row(r).dot(m.col(c)) for c in range(m.cols)) for r in range(s.rows)))
    # cofactorMatrix = property(lambda s: s.__class__(tuple(tuple(s.cofactor(r,c) for c in range(s.cols)) for r in range(s.rows))))
    # def submatrix(s, row, col): return s.__class__(tuple(tuple(s[r][c] for c in range(s.cols) if c != col) for r in range(s.rows) if r != row))
    # def __div__(s, m):
    #     if type(m) == float or type(m) == int: raise ValueError, "Can only divide by another matrix"
    #     return s * m.inverse
    # def __new__(cls, m): return group.Group.__new__(cls, tuple(vector.Vector(r) for r in m))
    # def __repr__(s):
    #     string = tuple(tuple(str(c) for c in r) for r in s)
    #     col_size = max(max(len(c) for c in r) for r in string)
    #     border = "\n%s\n" % (":" * (col_size * s.cols + s.cols + 3))
    #     m = "\n".join("::%s::" % " ".join(c.center(col_size) for c in r) for r in string)
    #     return border + m + border
    # @property
    # def determinant(s):
    #     if s.rows != s.cols: raise ValueError, "Matrix must be square"
    #     if s.rows == 2: return s[0][0] * s[1][1] - s[0][1] * s[1][0]
    #     calc = tuple(s[0][top] * s.submatrix(0, top).determinant for top in range(s.rows))
    #     result = 0
    #     for i in range(len(calc)):
    #         result = result - calc[i] if i % 2 else result + calc[i]
    #     return result
    # adjoint = property(lambda s: s.cofactorMatrix.transpose)
    # @property
    # def inverse(s):
    #     det = s.determinant
    #     return s.adjoint * ( 1.0 / det) if det else 0.0
    # def col(s, c): return vector.Vector(r[c] for r in s)
    # transpose = property(lambda s: s.__class__(zip(*s)))
    # def row(s, r): return s[r]
    # def cofactor(s, row, col):
    #     m = s.submatrix(row, col).determinant
    #     return +m if row % 2 == col % 2 else -m
