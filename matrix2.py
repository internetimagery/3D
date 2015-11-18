
# Testing changable dimension matrix
import itertools
import collections

class Matrix(collections.Sequence):
    """
    Matrix Datatype
    """
    __slots__ = ("rows", "cols")
    def __init__(s, *args, **kwargs):
        if args:
            s.rows = kwargs.get("rows", 1)
            s.cols = len(args) / s.rows
            s.cells = args
        else:
            raise ValueError, "No Cells provided."
    def __getitem__(s, k): return s.cells[k]
    def __len__(s): return len(s.cells)
    def row(s, r):
        """
        Get a specified row
        """
        start = r * s.cols
        end = start + s.cols
        return s.cells[start:end]
    def col(s, c):
        """
        Get a specified column
        """
        return tuple(s.cells[r + c] for r in range(0, s.rows * s.cols, s.cols))
        


m1 = Matrix(
    1,2,3,
    4,5,6,
    7,8,9,
    rows=3
)
m2 = Matrix(1,2,3)
m3 = 3
print m1.col(1)
