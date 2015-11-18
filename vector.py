# Vector

import math

# Vector Functionality

def magnitude(v):
    """
    Calculate the magnitude / length / unit of a Vector. |s|
    """
    return math.sqrt(sum(a ** 2 for a in v))

def normalize(v):
    """
    Normalize a Vector.
    """
    m = magnitude(v)
    return tuple(a / m for a in v) if m else (0.0,)*len(v)

def dot(v1, v2):
    """
    Calculate the Dot Product between two Vectors.
    """
    try:
        return sum(a * b for a, b in zip(v1, v2))
    except TypeError:
        raise TypeError, "Dot Product requires two Vectors."

def cross(v1, v2):
    """
    Get the Normal / Cross Product of two vectors.
    """
    try:
        return (
            v1[1] * v2[2] - v2[1] * v1[2],
            v1[2] * v2[0] - v2[2] * v1[0],
            v1[0] * v2[1] - v2[0] * v1[1])
    except IndexError:
        raise TypeError, "Cross Product requires two Vectors of 3 dimensions."

def angle(v1, v2):
    """
    Get the angle between two Vectors. Result in Radians.
    """
    try:
        return math.acos(a * b for a, b in zip(normalize(v1), normalize(v2)))
    except AttributeError:
        raise TypeError, "Angle requires two Vectors."

def rotate(v1, v2, a):
    """
    Rotate Vector around another Vector by a specified Angle in Radians.
    """
    try:
        cos, sin = math.cos(a), math.sin(a)
        up = normalize(v2)
        right = cross(up, v1)
        out = cross(right, up)
        return tuple( _up * (_v1 * _up) + (_out * _cos) + (_right * _sin) for _up, _right, _out, _v1, _sin, _cos in zip(up, right, out, v1, (sin,)*len(v1), (cos,)*len(v1)))
    except TypeError:
        raise TypeError, "Rotate requires two Vectors and an Angle."

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

    # Vector Utility

    def test(s, v, func):
        """
        Test Func for truthiness.
        """
        for a, b in zip(s, v):
            if func(a, b): return True
        return False

    def zip(s, v1, v2):
        """
        Allow Scalar Operations.
        """
        try:
            return zip(v1, v2)
        except TypeError:
            try:
                return zip(v1, (v2,)*len(v1))
            except TypeError:
                return zip((v1,)*len(v2), v2)

    # Vector Operations

    def __neg__(s): return s.__class__(-a for a in s)
    def __pos__(s): return s.__class__(+a for a in s)
    def __nonzero__(s): return s.test(s, lambda a, b: True if a else False)
    def __radd__(s, v): return s.__class__(b + a for a, b in s.zip(s, v))
    def __add__(s, v): return s.__class__(a + b for a, b in s.zip(s, v))
    def __rdiv__(s, v): return s.__class__(b / a for a, b in s.zip(s, v))
    def __div__(s, v): return s.__class__(a / b for a, b in s.zip(s, v))
    def __rmod__(s, v): return s.__class__(b % a for a, b in s.zip(s, v))
    def __mod__(s, v): return s.__class__(a % b for a, b in s.zip(s, v))
    def __rsub__(s, v): return s.__class__(b - a for a, b in s.zip(s, v))
    def __sub__(s, v): return s.__class__(a - b for a, b in s.zip(s, v))
    def __rpow__(s, v): return s.__class__(b ** a for a, b in s.zip(s, v))
    def __pow__(s, v): return s.__class__(a ** b for a, b in s.zip(s, v))
    def __rlt__(s, v): return s.test(v, lambda b, a: a < b)
    def __lt__(s, v): return s.test(v, lambda a, b: a < b)
    def __rtruediv__(s, v): return s.__class__(b / a for a, b in s.zip(s, v))
    def __truediv__(s, v): return s.__class__(a / b for a, b in s.zip(s, v))
    def __rgt__(s, v): return s.test(v, lambda b, a: a > b)
    def __gt__(s, v): return s.test(v, lambda a, b: a > b)
    def __rne__(s, v): return s.test(v, lambda b, a: a != b)
    def __ne__(s, v): return s.test(v, lambda a, b: a != b)
    def __req__(s, v): return s.test(v, lambda b, a: a == b)
    def __eq__(s, v): return s.test(v, lambda a, b: a == b)
    def __rle__(s, v): return s.test(v, lambda b, a: a <= b)
    def __le__(s, v): return s.test(v, lambda a, b: a <= b)
    def __rge__(s, v): return s.test(v, lambda b, a: a >= b)
    def __ge__(s, v): return s.test(v, lambda a, b: a >= b)
    def __rfloordiv__(s, v): return s.__class__(b // a for a, b in s.zip(s, v))
    def __floordiv__(s, v): return s.__class__(a // b for a, b in s.zip(s, v))
    # More Functionality
    def __rmul__(s, v): return s.__mul__(v) # (*)
    def __mul__(s, v): # (*)
        try: # Multiplying a Matrix
            return s.__class__(sum(tuple(b * c  for b, c in zip(a, s))) for a in v)
        except TypeError:
            try: # Multiplying a Vector
                return dot(s, v)
            except TypeError: # Scalar
                return s.__class__(a * v for a in s)
    def dot(s, v): return dot(s, v)
    def __rxor__(s, v): return s.__class__(cross(v, s)) # (^)
    def __xor__(s, v): return s.__class__(cross(s, v)) # (^)
    def cross(s, v): return s.__class__(cross(s, v))
    def angle(s, v): return angle(s, v)
    def rotate(s, v, a): return s.__class__(rotate(s, v, a))
    def isEquivalent(s, v, t=0.99988888):
        """
        Returns True if this vector and another are within a given tolerance of being equal.
        """
        return False not in set(abs(a - b) < t for a, b in zip(s, v))
    def isParallel(s, v, t=0.99988888):
        """
        Returns True if this vector and another are within the given tolerance of being parallel.
        """
        try:
            return 1 - t < dot(normalize(s), normalize(v))
        except TypeError:
            raise TypeError, "\"Is Parallel\" requires two Vectors and a Float."
    def distance(s, v):
        """
        Distance between two Vectors
        """
        try:
            between = (b - a for a, b in zip(s, v))
            return magnitude(between)
        except TypeError:
            raise TypeError, "Distance requires two Vectors."

    # Vector Properties

    @property
    def length(s): return magnitude(s)
    @property
    def magnitude(s): return magnitude(s)
    @property
    def normalized(s): return s.__class__(normalize(s))
    @property
    def normal(s): return s.__class__(normalize(s))
    @property
    def unit(s): return s.__class__(normalize(s))

if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(3,2,1)
    m1 = (
        (1,2,3),
        (4,5,6),
        (7,8,9)
    ) # Matrix
    assert v1 == v1
    assert v1 != v2
    v3 = v1 + v2
    assert v3 == (4,4,4)
    assert 2 * v1 == (2,4,6)
    assert v1 ** 2 == (1,4,9)
    assert v1 * v2 == 10
    assert v1 * m1 == (14,32,50)
    assert (1,2,3) ^ v2 == (-4,8,-4)
    print "Ok!"
