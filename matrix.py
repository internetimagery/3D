# Matrix

import group
import vector

class Matrix(group.Group):
    __slots__ = ()
    def __new__(s, m):
        group.Group.__new__(s, tuple(vector.Vector(r) for r in m))

print tuple(vector.Vector(r) for r in [[1,2,4],[2,3,2]])

print Matrix([[1,2,3], [3,2,1]])
#
# class Matrix(collections.Sequence):
#     __slots__ = ("row", "col", "cols", "rows")
#     def __init__(s, row):
#         s.rows = row
#         s.row = range(len(row))
#         s.col = range(len(row[0]))
#         # Store transpose
#         s.cols = tuple(tuple(s.rows[b][a] for b in s.row) for a in s.col)
#     def __repr__(s): return "\n".join([repr(a) for a in s.rows])
#     def __len__(s): return (len(s.row), len(s.col))
#     def __getitem__(s, k):
#         try:
#             return s.rows[k[0]][k[1]]
#         except TypeError:
#             raise TypeError, "You must supply both x and y coordinates."
#     def __mul__(s, m): return s.__class__(tuple(tuple(sum([a * b for a, b in zip(s.rows[r], m.cols[c])]) for c in m.col) for r in s.row))
#     def __add__(s, m): return s.__class__(tuple(tuple(m[r,c] + s[r,c] for c in s.col) for r in s.row))
#     def __div__(s, m): return s * -v
#     def __mod__(s, m): raise NotImplementedError
#     def __sub__(s, m): return s.__class__(tuple(tuple(m[r,c] - s[r,c] for c in s.col) for r in s.row))
#     def __pow__(s, m): raise NotImplementedError
#     def __lt__(s, m): raise NotImplementedError
#     def __gt__(s, m): raise NotImplementedError
#     def __truediv__(s, m): raise NotImplementedError
#     def __eq__(s, m): return False not in set(s[r,c] == m[r,c] for r in s.row for c in s.col)
#     def __le__(s, m): raise NotImplementedError
#     def __ge__(s, m): raise NotImplementedError
#     def __floordiv__(s, m): raise NotImplementedError
#     def __nonzero__(s): return True if set(True for r in s.row for c in s.col if s[r,c]) else False
#     def __ne__(s, m): return s != m
#     def __neg__(s): return s.__class__(tuple(tuple(-s[r,c] for c in s.col) for r in s.row))
#     def __pos__(s): return s.__class__(tuple(tuple(+s[r,c] for c in s.col) for r in s.row))
#     def scalar(s, n): return s.__class__(tuple(tuple(n for c in s.col) for r in s.row))
#     # def _inv(s):
#     #     num = range(len(s.row)); num.reverse()
#     #     if len(s.row) != len(s.col): raise ValueError, "Matrix must be a square."
#     #     return s.__class__(tuple(tuple((r,c) for c in num) for r in num))
#     # inverse = property(lambda s: s._inv())
#
# def identity(size):
#     num = range(size)
#     return Matrix(tuple(tuple(1 if a == b else 0 for b in num) for a in num))
