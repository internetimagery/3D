# Matrix

import math

# Matrix Operations

def square(m):
    """ Test if a Matrix is square """
    return len(m) == len(m[0])

def multiply(m1, m2):
    """ Multiply two matricies """
    return tuple(tuple(i * j for i, j in zip(k, l)) for k, l in zip(m1, zip(*m2)))

def multiplyVector(m, v):
    """ Multiply Matrix with Vector """
    return tuple(sum(tuple(i * j for i, j in zip(k, v))) for k in m)

def submatrix(m, row, col):
    """ Return Matrix absent Row / Col """
    return tuple(tuple(j for i, j in enumerate(l) if i != col) for k, l in enumerate(m) if k != row)

def determinant(m):
    """ Matrix determinant |m| """
    if not square(m): raise TypeError, "Matrix must be square."
    if len(m) == 2:
        flat = tuple(i for j in m for i in j)
        return flat[0] * flat[3] - flat[1] * flat[2]
    calc = tuple(l * determinant(submatrix(m, 0, k)) for i, j in enumerate(m) for k, l in enumerate(j) if not i)
    result = 0
    for i, j in enumerate(calc): # Negative / Positive
        result = result - j if i % 2 else result + j
    return result

def cofactor(m, row, col):
    """ Find the cofactor of a cell in matrix """
    m = determinant(submatrix(m, row, col))
    return +m if row % 2 == col % 2 else -m

def cofactorMatrix(m):
    """ Generate a Matrix with the cofactor of each cell """
    return tuple(tuple(cofactor(m, k, i) for i, j in enumerate(l)) for k, l in enumerate(m))

def transpose(m):
    """ Transpose a matrix """
    return zip(*m)

def inverse(m):
    """ Generate the inverse of a matrix """
    det = determinant(m)
    adjugate = transpose(cofactorMatrix(m))
    scalar = (1.0 / det) if det else 0.0
    return tuple(tuple(i * scalar for i in j) for j in adjugate)

# Matrix Datatype

class Matrix(tuple):
    """
    Matrix Datatype
    """
    __slots__ = ()

    # Matrix Creation and Visualization

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

    # Matrix Cell Access and Sizing

    @property
    def rows(s):
        """ Number of Rows in Matrix """
        return len(s)
    @property
    def cols(s):
        """ Number of Columns in Matrix """
        return len(s[0])
    def row(s, r):
        """ Specified Row from Matrix """
        return s[r]
    def col(s, c):
        """ Specified Column from Matrix """
        return tuple(j[c] for j in s)
    def cell(s, r, c):
        """ Specified Cell from Matrix. Row, Col """
        return s[r][c]

    # Matrix Utilities

    def test(s, m, func):
        """ Test Function for truthiness against other Matrix """
        for i in range(s.rows):
            for j in range(s.cols):
                if func(s[i][j], m[i][j]): return True
        return False

    # Matrix Operations

    def __neg__(s): return s.__class__(tuple(-i for i in j) for j in s)
    def __pos__(s): return s.__class__(tuple(+i for i in j) for j in s)
    def __sub__(s, m): return s + -m
    def __add__(s, m):
        try: # Adding Matrix
            return s.__class__(tuple(i + j for i, j in zip(k, l)) for k, l in zip(s, m))
        except TypeError: # Adding Scalar
            return s.__class__(tuple(i + m for i in j) for j in s)
    def __ne__(s, m): return False if s == m else True
    def __eq__(s, m): return s.test(m, lambda i, j: i == j)
    def __lt__(s, m): return s.test(m, lambda i, j: i < j)
    def __le__(s, m): return s.test(m, lambda i, j: i <= j)
    def __gt__(s, m): return s.test(m, lambda i, j: i > j)
    def __ge__(s, m): return s.test(m, lambda i, j: i >= j)
    def __nonzero__(s): return s.test(s, lambda i, j: True if i else False)
    def __truediv__(s): return s.__div__(m)
    def __mul__(s, m):
        try: # Multiplying a Matrix
            return s.__class__(multiply(s, m))
        except TypeError: # Perhaps we're trying for a Vector Product?
            try:
                return multiplyVector(s, m)
            except TypeError: # Perhaps we're mutiplying by a Scalar?
                return s.__class__(tuple(i * m for i in j) for j in s)
    def __div__(s, m):
        try: # Another matrix
            return s * inverse(m)
        except AttributeError: # Scalar
            return s.__class__(tuple(i / m for i in j) for j in s)

    # Other Properties

    @property
    def transpose(s): return s.__class__(transpose(s))
    @property
    def determinant(s): return s.__class__(determinant(s))
    @property
    def inverse(s): return s.__class__(inverse(s))

    #
    # def __mod__(s, m): return s.__class__(tuple(c % d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))
    # def __pow__(s, m): return s.__class__(tuple(c ** d for c, d in s.zip(a, b)) for a, b in s.zip(s, m))

m = Matrix(3,0,2,2,0,-2,0,1,1)
print m.inverse



if __name__ == '__main__':
    m1 = Matrix(1,2,3,4,5,6,7,8,9)
    m2 = Matrix(rows=3)
    m3 = Matrix(
        (1,2,3),
        (4,5,6),
        (7,8,9)
    )
    v1 = (1,2,3) # Vector
    s1 = 2 # Scalar
    assert m3.row(1) == (4,5,6)
    assert m3.rows == 3
    assert m3.col(0) == (1,4,7)
    assert m3.cols == 3
    assert m3.cell(1,1) == 5
    assert m3.square
    assert -m3 == Matrix(-1,-2,-3,-4,-5,-6,-7,-8,-9)
    assert m1 + m2 == Matrix(2,2,3,4,6,6,7,8,10)
    assert m2 + s1 == Matrix(3,2,2,2,3,2,2,2,3)
    assert m3 - m2 == Matrix(0,2,3,4,4,6,7,8,8)
    assert m1 == m3
    assert m2 <= m1
    assert True if m1 else False
    assert False if Matrix(0,0,0,0) else True
    assert m1 * m2 == Matrix(1,0,0,0,5,0,0,0,9)
    assert m1 * s1 == Matrix(2,4,6,8,10,12,14,16,18)
    assert m1 * v1 == (14,32,50)
