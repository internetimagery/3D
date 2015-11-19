# Matrix

import math

# Matrix Operations

def square(m):
    """ Test if a Matrix is square """
    return len(m) == len(m[0])

def multiply(m1, m2):
    """ Multiply two matricies """
    return tuple(tuple(c1 * r2 for c1, r2 in zip(r1, c2)) for r1, c2 in zip(m1, zip(*m2)))

def multiplyVector(m, v):
    """ Multiply Matrix with Vector """
    return tuple(sum(tuple(c1 * c2 for c1, c2 in zip(r, v))) for r in m)

def submatrix(m, row, col):
    """ Return Matrix absent Row / Col """
    return tuple(tuple(c for ci, c in enumerate(r) if ci != col) for ri, r in enumerate(m) if ri != row)

def determinant(m):
    """ Matrix determinant |m| """
    if not square(m): raise TypeError, "Matrix must be square."
    if len(m) == 2:
        flat = tuple(c for r in m for c in r)
        return flat[0] * flat[3] - flat[1] * flat[2]
    calc = tuple(c * determinant(submatrix(m, 0, ci)) for ri, r in enumerate(m) for ci, c in enumerate(r) if not ri)
    result = 0
    for a, b in enumerate(calc): # Negative / Positive
        result = result - b if a % 2 else result + b
    return result

def cofactor(m, row, col):
    """ Find the cofactor of a cell in matrix """
    m = determinant(submatrix(m, row, col))
    return +m if row % 2 == col % 2 else -m

def cofactorMatrix(m):
    """ Generate a Matrix with the cofactor of each cell """
    return tuple(tuple(cofactor(m, ri, ci) for ci, c in enumerate(r)) for ri, r in enumerate(m))

def transpose(m):
    """ Transpose a matrix """
    return zip(*m)

def inverse(m):
    """ Generate the inverse of a matrix """
    det = determinant(m)
    adjugate = transpose(cofactorMatrix(m))
    scalar = (1.0 / det) if det else 0.0
    return tuple(tuple(c * scalar for c in r) for r in adjugate)


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
            return tuple.__new__(cls, (tuple(1.0 if c == r else 0.0 for c in range(kwargs["rows"])) for r in range(kwargs["rows"])))
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
                return tuple.__new__(cls, (tuple(args[c+r] for c in range(int(cols))) for r in range(0, int(rows * cols), int(rows))))
        raise ValueError, "Invalid Arguments to create Matrix."
    def __repr__(s):
        st = tuple(tuple(str(c) for c in r) for r in s)
        length = max(max(len(c) for c in r) for r in st)
        return "\n" + "\n".join(" ".join(c.center(length) for c in r) for r in st) + "\n"

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
        return tuple(r[c] for r in s)
    def cell(s, r, c):
        """ Specified Cell from Matrix. Row, Col """
        return s[r][c]

    # Matrix Utilities

    def test(s, m, func):
        """ Test Function for truthiness against other Matrix """
        for r in range(s.rows):
            for c in range(s.cols):
                if func(s[r][c], m[r][c]): return True
        return False

    # Matrix Operations

    def __neg__(s): return s.__class__(tuple(-c for c in r) for r in s)
    def __pos__(s): return s.__class__(tuple(+c for c in r) for r in s)
    def __rsub__(s, m): return m + -s
    def __sub__(s, m): return s + -m
    def __radd__(s, m): return s.__add__(m)
    def __add__(s, m):
        try: # Adding Matrix
            return s.__class__(tuple(c1 + c2 for c1, c2 in zip(r1, r2)) for r1, r2 in zip(s, m))
        except TypeError: # Adding Scalar
            return s.__class__(tuple(c + m for c in r) for r in s)
    def __rne__(s, m): return s.test(m, lambda b, a: a != b)
    def __ne__(s, m): return s.test(m, lambda a, b: a != b)
    def __req__(s, m): return s.test(m, lambda b, a: a != b)
    def __eq__(s, m): return s.test(m, lambda a, b: a == b)
    def __rlt__(s, m): return s.test(m, lambda b, a: a != b)
    def __lt__(s, m): return s.test(m, lambda a, b: a < b)
    def __rle__(s, m): return s.test(m, lambda b, a: a != b)
    def __le__(s, m): return s.test(m, lambda a, b: a <= b)
    def __rgt__(s, m): return s.test(m, lambda b, a: a != b)
    def __gt__(s, m): return s.test(m, lambda a, b: a > b)
    def __rge__(s, m): return s.test(m, lambda b, a: a != b)
    def __ge__(s, m): return s.test(m, lambda a, b: a >= b)
    def __nonzero__(s): return s.test(s, lambda a, b: True if a else False)
    def __truediv__(s): return s.__div__(m)
    def __rmul__(s, m): return s.__mul(m, s)
    def __mul__(s, m): return s.__mul(s, m)
    def __mul(s, m1, m2):
        try: # Multiplying a Matrix
            return s.__class__(multiply(m1, m2))
        except TypeError: # Perhaps we're trying for a Vector Product?
            try:
                return multiplyVector(m1, m2)
            except TypeError: # Perhaps we're mutiplying by a Scalar?
                return s.__class__(tuple(c * m2 for c in r) for r in m1)
    def __div__(s, m): return s.__div(s, m)
    def __rdiv__(s, m): return s.__div(m, s)
    def __div(s, m1, m2):
        try: # Another matrix
            return m1 * inverse(m2)
        except AttributeError: # Scalar
            return s.__class__(tuple(c / m2 for c in r) for r in m1)

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
    3 * m1
    assert m3.row(1) == (4,5,6)
    assert m3.rows == 3
    assert m3.col(0) == (1,4,7)
    assert m3.cols == 3
    assert m3.cell(1,1) == 5
    assert square(m3)
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
    assert Matrix(3,0,2,2,0,-2,0,1,1).inverse == Matrix(0.2,0.2,0.0,-0.2,0.3,1.0,0.2,-0.3,0.0)
    print "Ok!"
