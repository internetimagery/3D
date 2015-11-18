# Matrix

import math
import itertools

class Matrix(tuple):
    """
    Matrix Datatype
    """
    __slots__ = ()
    def __new__(cls, *args, **kwargs):
        """
        Generate a new Matrix
        Instantiate:
            Matrix(1,2,3,4,5,6,7,8,9,rows=3) # Flattened
            Matrix(1,2,3,4,5,6,7,8,9) # Flattened. No row specified, assumed Square
            Matrix([j+i for j in range(4)] for i in range(0,16,4)) # Generator
            Matrix([1,2,3],[4,5,6],[7,8,9]) # Rows
            Matrix(rows=3) # Identity matrix
        """
        l = len(args)
        if l == 0 and "rows" in kwargs: # Identity Matrix
            return tuple.__new__(cls, (tuple(1.0 if i == j else 0.0 for i in range(kwargs["rows"])) for j in range(kwargs["rows"])))
        if l == 1: # Assumed Generator
            return tuple.__new__(cls, args[0])
        try: # Rows
            inner = len(args[0])
            for i in args:
                if len(i) != inner: break
            else:
                return tuple.__new__(cls, args)
        except TypeError: # Flattened
            rows = kwargs["rows"] if "rows" in kwargs else math.sqrt(l) # Rows
            cols = float(l) / rows
            if not cols % 1: # Ensure the matrix fits the size
                return tuple.__new__(cls, (tuple(args[i+j] for i in range(int(cols))) for j in range(0, int(rows * cols), int(rows))))
        raise ValueError, "Invalid Arguments to create Matrix."
    def __repr__(s):
        st = tuple(tuple(str(i) for i in j) for j in s)
        length = max(max(len(i) for i in j)for j in st)
        return "\n" + "\n".join(" ".join(i.center(length) for i in j) for j in st)

if __name__ == '__main__':
    m1 = Matrix(1,2,3,4,5,6,7,8,9)
    m2 = Matrix(rows=3)
    m3 = Matrix(
        (1,2,3),
        (4,5,6),
        (7,8,9)
    )
    print m1
