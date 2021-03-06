# Vector

import math
import itertools

# Vector Functionality

def Magnitude(v):
    """
    Calculate the magnitude / length / unit of a Vector. |s|
    """
    return math.sqrt(sum(a ** 2 for a in v))

def Normalize(v):
    """
    Normalize a Vector.
    """
    m = Magnitude(v)
    return tuple(a / m for a in v) if m else (0.0,)*len(v)

def Dot(v1, v2):
    """
    Calculate the Dot Product between two Vectors.
    """
    try:
        return sum(a * b for a, b in zip(v1, v2))
    except TypeError:
        raise TypeError, "Dot Product requires two Vectors."

def Cross(v1, v2):
    """
    Get the Normal / Cross Product of two vectors.
    """
    try:
        x1, y1, z1 = v1
        x2, y2, z2 = v2
        return (
            y1 * z2 - y2 * z1,
            z1 * x2 - z2 * x1,
            x1 * y2 - x2 * y1)
    except ValueError:
        raise TypeError, "Cross Product requires two Vectors of 3 dimensions."

def Angle(v1, v2):
    """
    Get the angle between two Vectors. Result in Radians.
    """
    try:
        m = Magnitude(v1) * Magnitude(v2)
        d = Dot(v1, v2)
        return math.acos((d / m) if m else 0.0)
    except AttributeError:
        raise TypeError, "Angle requires two Vectors."

def Rotate(v1, v2, a):
    """
    Rotate Vector around another Vector by a specified Angle in Radians.
    """
    try:
        cos, sin = math.cos(a), math.sin(a)
        up = Normalize(v2)
        right = Cross(up, v1)
        out = Cross(right, up)
        return tuple( _up * (_v1 * _up) + (_out * _cos) + (_right * _sin) for _up, _right, _out, _v1, _sin, _cos in zip(up, right, out, v1, (sin,)*len(v1), (cos,)*len(v1)))
    except TypeError:
        raise TypeError, "Rotate requires two Vectors and an Angle."

def Parallel(v1, v2, tolerance=0):
    """
    Test if two Vectors are parallel
    """
    try:
        return 1 - tolerance < Dot(Normalize(v1), Normalize(v2))
    except TypeError:
        raise TypeError, "Check requires two Vectors"

def Iterate(v1, v2):
    """
    Iterate Vector with Vector / Scalar
    """
    try: # Vector
        return zip(v1, v2)
    except TypeError: # Scalar
        return zip(v1, itertools.repeat(v2))

def MatrixMultiply(v, m):
    """
    Multiply Vector by Matrix
    """
    try:
        return tuple(Dot(v, r) for r in m)
    except TypeError:
        raise TypeError, "A Vector and Matrix are required to multiply."

def Equal(v1, v2, tolerance=0):
    """
    Test equality of Vectors
    """
    try:
        return False not in set(abs(a - b) <= tolerance for a, b in zip(v1, v2))
    except TypeError:
        return False


def Test(func, v1, v2):
    """
    Test individual elements in Vector(s) for truthiness
    """
    return False not in set(func(a, b) for a, b in Iterate(v1, v2))

class Vector(tuple):
    """
    A Simple Vector that allows math operations to be performed on it.
    """
    __slots__ = ()
    def __new__(cls, *pos):
        """
        Create a new Vector.
        Instantiate:
            Vector(1,2,3) # Positional
            Vector(a for a in range(3)) # Generator
        """
        return tuple.__new__(cls, pos[0] if len(pos) == 1 else pos)

    # Vector Operations

    def __req__(s, v): return s == v
    def __rne__(s, v): return s != v
    def __eq__(s, v): return Equal(s, v)
    def __ne__(s, v): return False if s == v else True
    def __lt__(s, v): return Test((lambda x,y: x < y ), s, v)
    def __gt__(s, v): return Test((lambda x,y: x > y ), s, v)
    def __le__(s, v): return Test((lambda x,y: x <= y ), s, v)
    def __ge__(s, v): return Test((lambda x,y: x >= y ), s, v)
    def __rlt__(s, v): return Test((lambda x,y: y < x ), s, v)
    def __rgt__(s, v): return Test((lambda x,y: y > x ), s, v)
    def __rle__(s, v): return Test((lambda x,y: y <= x ), s, v)
    def __rge__(s, v): return Test((lambda x,y: y >= x ), s, v)
    def __nonzero__(s): return Test((lambda x,y: True if x else False ), s, s)
    def __neg__(s): return s.__class__( -a for a in s )
    def __pos__(s): return s.__class__( +a for a in s )
    def __add__(s, v): return s.__class__( a + b for a, b in Iterate(s, v))
    def __div__(s, v): return s.__class__( a / b for a, b in Iterate(s, v))
    def __mod__(s, v): return s.__class__( a % b for a, b in Iterate(s, v))
    def __sub__(s, v): return s.__class__( a - b for a, b in Iterate(s, v))
    def __radd__(s, v): return s.__class__( b + a for a, b in Iterate(s, v))
    def __rsub__(s, v): return s.__class__( b - a for a, b in Iterate(s, v))
    def __rmod__(s, v): return s.__class__( b % a for a, b in Iterate(s, v))
    def __rdiv__(s, v): return s.__class__( b / a for a, b in Iterate(s, v))
    def __pow__(s, v): return s.__class__( a ** b for a, b in Iterate(s, v))
    def __rpow__(s, v): return s.__class__( b ** a for a, b in Iterate(s, v))
    def __truediv__(s, v): return s.__class__( a / b for a, b in Iterate(s, v))
    def __rtruediv__(s, v): return s.__class__( b / a for a, b in Iterate(s, v))
    def __floordiv__(s, v): return s.__class__( a // b for a, b in Iterate(s, v))
    def __rfloordiv__(s, v): return s.__class__( b // a for a, b in Iterate(s, v))
    def __mul__(s, v): # (*)
        try:
            return MatrixMultiply(s, v)
        except TypeError:
            try:
                return Dot(s, v)
            except TypeError:
                return s.__class__(a * v for a in s)
    def __rmul__(s, v): # (*)
        try:
            return MatrixMultiply(v, s)
        except TypeError:
            try:
                return Dot(v, s)
            except TypeError:
                return s.__class__(v * a for a in s)

    # Vector Functionality

    def dot(s, v): return Dot(s, v)
    def __rxor__(s, v): return s.__class__(Cross(v, s)) # (^)
    def __xor__(s, v): return s.__class__(Cross(s, v)) # (^)
    def cross(s, v): return s.__class__(Cross(s, v))
    def angle(s, v): return Angle(s, v)
    def rotate(s, v, a): return s.__class__(Rotate(s, v, a))
    def isEquivalent(s, v, t=0.99988888): return Equal(s, v, t)
    def isParallel(s, v, t=0.99988888): return Parallel(s, v, t)
    def distance(s, v):
        """
        Distance between two Vectors
        """
        try:
            between = (b - a for a, b in zip(s, v))
            return Magnitude(between)
        except TypeError:
            raise TypeError, "Distance requires two Vectors."

    # Vector Properties

    @property
    def length(s): return Magnitude(s)
    @property
    def magnitude(s): return Magnitude(s)
    @property
    def normalize(s): return s.__class__(Normalize(s))
    @property
    def normal(s): return s.__class__(Normalize(s))
    @property
    def unit(s): return s.__class__(Normalize(s))


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(3,2,1)
    m1 = (
        (1,2,3),
        (4,5,6),
        (7,8,9)
    ) # Matrix
    v3 = v1 + v2
    assert v1 == v1
    assert v1 != v2
    assert v3 == (4,4,4)
    assert 3 < v3
    assert v3 > v1
    assert v1 != 1
    assert 2 * v1 == (2,4,6)
    assert v1 ** 2 == (1,4,9)
    assert v1 * v2 == 10
    assert v1 * m1 == (14,32,50)
    assert (1,2,3) ^ v2 == (-4,8,-4)
    assert Angle((1,0,0),(0,0,1)) == math.radians(90)
    assert Equal(Rotate((1,0,0), (0,1,0), math.radians(90)), (0,0,-1), 0.00001)
    print "Ok!"
