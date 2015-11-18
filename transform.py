# Transformation Matrix

import math
import itertools

class Matrix(tuple):
    __slots__ = ()
    def __new__(cls, *nums): return tuple.__new__(cls, nums[0] if len(nums) == 1 else nums)
    def __repr__(s):
        string = tuple(tuple(str(b) for b in a) for a in s)
        col = max(max(len(b) for b in a) for a in string)
        return "\n".join(" ".join(b.center(col) for b in a) for a in string)
    # Basic Math Operations
    def __truediv__(s, m): return s.__div__(m)
    def __ne__(s, m): return False if s == m else True
    def __neg__(s): return s.__class__(tuple(-b for b in a) for a in s)
    def __pos__(s): return s.__class__(tuple(+b for b in a) for a in s)
    def __add__(s, m): return s.__class__(tuple(c + d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))
    def __sub__(s, m): return s.__class__(tuple(c - d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))
    def __nonzero__(s): return True if tuple(b for a in s for b in a if b) else False
    def __mod__(s, m): return s.__class__(tuple(c % d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))
    def __pow__(s, m): return s.__class__(tuple(c ** d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))
    def __floordiv__(s, m): return s.__class__(tuple(c // d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))
    def __lt__(s, m): return test(s, m, lambda a, b: a < b)
    def __gt__(s, m): return test(s, m, lambda a, b: a > b)
    def __le__(s, m): return test(s, m, lambda a, b: a <= b)
    def __ge__(s, m): return test(s, m, lambda a, b: a >= b)
    def __eq__(s, m): return test(s, m, lambda a, b: a == b)
    def __mul__(s, m):
        try:
            return s.__class__(tuple(c * d for c, d in zip(a, b)) for a, b in zip(s, m.transpose))
        except AttributeError:
            return s.__class__(tuple(b * m for b in a) for a in s)
    def __div__(s, m):
        try:
            return s * m.inverse
        except AttributeError:
            return s.__class__(tuple(b / m for b in a) for a in s)
    # Extra functionality
    def row(s, r):
        """
        Return a single row.
        """
        return s[r]
    def col(s, c):
        """
        Return a single column
        """
        return tuple(r[c] for r in s)
    def submatrix(s, row, col):
        """
        Return the matrix with Row and Col removed.
        """
        return s.__class__(tuple(s[r][c] for c in range(s.cols) if c != col) for r in range(s.rows) if r != row)
    def cofactor(s, row, col):
        """
        Generate the cofactor of a specified Row/Col
        """
        m = s.submatrix(row, col).determinant
        return +m if row % 2 == col % 2 else -m
    def zip(m1, m2):
        """
        Allow Scalar and Vector Operations.
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
    # Matrix Properties
    @property
    def rows(s): return len(s)
    @property
    def cols(s): return len(s[0])
    @property
    def transpose(s):
        """
        Turn Matrix Rows into Columns.
        """
        return s.__class__(zip(*s))
    @property
    def determinant(s):
        """
        Calculate the determinant of the matrix.
        """
        if s.rows == 2: return s[0][0] * s[1][1] - s[0][1] * s[1][0]
        calc = tuple(s[0][top] * s.submatrix(0, top).determinant for top in range(s.rows))
        result = 0
        for i in range(len(calc)):
            result = result - calc[i] if i % 2 else result + calc[i]
        return result
    @property
    def inverse(s):
        """
        Generate the inverse of the matrix.
        """
        det = s.determinant
        return s.adjugate * ( 1.0 / det) if det else 0.0
    @property
    def cofactorMatrix(s):
        """
        Generate a matrix with a cofactor in each entry.
        """
        return s.__class__(tuple(s.cofactor(r,c) for c in range(s.cols)) for r in range(s.rows))
    @property
    def adjugate(s):
        """
        The transpose of the cofactor matrix
        """
        return s.cofactorMatrix.transpose


m1 = Matrix((
    (-3,2,-5),
    (-1,0,-2),
    (3,-4,1)
))
m2 = Matrix((1,2,3))
print m1
print m2
print m1 + m2


#
#
# class Transform(tuple):
#     """
#     Transformation Matrix
#
#     Transform() <--- Identity
#     Transform(
#         [1, 2, 3, 4 ],
#         [5, 6, 7, 8 ],
#         [9, 10,11,12],
#         [13,14,15,16]
#         ) <--- By Row
#     Transform(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) <--- a11, a12, a13, a21, a22, ... etc
#     Transform(tuple(c+r for c in range(4)) for r in range(1,17,4)) <--- generator / nested iterable
#     """
#     __slots__ = ()
#     cols = 4
#     rows = 4
#     def __new__(cls, *nums):
#         try:
#             l = len(nums)
#             if l == 16: # Full array of numbers
#                 return tuple.__new__(cls, (nums[r:r+4] for r in range(0,16,4)))
#             if l == 4: # Creation by rows
#                 return tuple.__new__(cls, nums)
#             if l == 1: # Iterable / Another matrix
#                 return tuple.__new__(cls, nums[0])
#             if l == 0: # Empty Matrix / Identity Matrix
#                 return tuple.__new__(cls, (tuple(1.0 if c == r else 0.0 for c in range(4)) for r in range(4)))
#             raise Exception
#         except:
#             raise ValueError, "Invalid arguments for Matrix."
#
# t1 = Transform()
# t2 = Transform(
#     (1,2,3,4),
#     (5,6,7,8),
#     (10,11,12,13),
#     (14,15,16,17)
# )
# t3 = t1 + 5
# print t1 * 4
#     #
