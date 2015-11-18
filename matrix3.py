# Column First Matrix

import itertools

class Matrix(tuple):
    """
    Column first Matrix Datatype
    Cell Access [Col][Row]
    """
    __slots__ = ()
    def __new__(cls, *args):
        """
        Generate a new Matrix
        """
        l = len(args)
        if l == 1: # Likely this is another matrix creating this.
            return tuple.__new__(cls, args[0])
        else:
            try:
                return tuple.__new__(cls, zip(*args)) # Rows provided
            except TypeError:
                return tuple.__new__(cls, args) # Probably vector
    @property
    def rows(s):
        """
        Get number of Rows in the Matrix
        """
        try:
            return len(s[0])
        except TypeError:
            return 1
    def row(s, r):
        """
        Grab a specific row
        """
        return tuple(s[c][r] for c in range(s.cols))
    @property
    def cols(s):
        """
        Get the number of columns in the Matrix
        """
        return len(s)
    def col(s, c):
        """
        Grab a specific column
        """
        return s[c]
    def __repr__(s):
        """
        Make the Matrix look nice.
        """
        try:
            string = tuple(tuple(str(s[c][r]) for c in range(s.cols)) for r in range(s.rows))
        except TypeError:
            string = tuple(tuple(str(s[c]) for c in range(s.cols)) for r in range(s.rows))
        longest = max(max(len(b) for b in a) for a in string)
        return "\n" + "\n".join(" ".join(b.center(longest) for b in a) for a in string)
    @property
    def transpose(s):
        """
        Change rows to columns and vice versa
        """
        return s.__class__(*s)
    def _zip(s, m1, m2):
        """
        Allow Scalar Operations.
        """
        try:
            return zip(m1, m2)
        except TypeError:
            return zip(m1, itertools.repeat(m2))
    def _test(s, m1, m2, func):
        """
        Test Matrix for truthiness.
        """
        for a, b in sZip(m1, m2):
            for c, d in sZip(a, b):
                if func(c, d): return True
        return False

m1 = Matrix(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
m2 = Matrix(1,2,3)
print m1
print m1.transpose
