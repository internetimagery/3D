# Vector

import math

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
        for i in range(len(s)):
            if func(s[i], v[i]): return True
        return False

    def zip(s, v1, v2):
        """
        Allow Scalar Operations.
        """
        try:
            return zip(v1, v2)
        except TypeError:
            return zip(v1, (v2,)*len(v1))

    # Vector Operations

    def __neg__(s): return s.__class__(-a for a in s)
    def __pos__(s): return s.__class__(+a for a in s)
    def __ne__(s, v): return False if s == v else True
    def __nonzero__(s): return s.test(s, lambda a, b: True if a else False)
    def __add__(s, v): return s.__class__(a + b for a, b in s.zip(s, v))
    def __div__(s, v): return s.__class__(a / b for a, b in s.zip(s, v))
    def __mod__(s, v): return s.__class__(a % b for a, b in s.zip(s, v))
    def __sub__(s, v): return s.__class__(a - b for a, b in s.zip(s, v))
    def __pow__(s, v): return s.__class__(a ** b for a, b in s.zip(s, v))
    def __truediv__(s, v): return s.__class__(a / b for a, b in s.zip(s, v))
    def __lt__(s, v): return True if s[0] < v[0] and s[1] < v[1] and s[2] < v[2] else False
    def __gt__(s, v): return True if s[0] > v[0] and s[1] > v[1] and s[2] > v[2] else False
    def __eq__(s, v): return True if s[0] == v[0] and s[1] == v[1] and s[2] == v[2] else False
    def __le__(s, v): return True if s[0] <= v[0] and s[1] <= v[1] and s[2] <= v[2] else False
    def __ge__(s, v): return True if s[0] >= v[0] and s[1] >= v[1] and s[2] >= v[2] else False
    def __floordiv__(s, v): return s.__class__(a // b for a, b in s.zip(s, v))
    # More Functionality
    def __mul__(s, v): # (*)
        try: # Multiplying a Matrix
            return s.__class__(sum(tuple(b * c  for b, c in zip(a, s))) for a in v)
        except TypeError:
            try: # Multiplying a Vector
                return s.dot(v)
            except TypeError:
                return s.__class__(a * v for a in s)
    def dot(s, v):
        """
        Create a Dot product between two vectors.
        """
        try:
            return sum(a * b for a, b in zip(s, v))
        except TypeError:
            raise TypeError, "Dot Product requires two Vectors."
    def __xor__(s, v): return s.cross(v) # (^)
    def cross(s, v):
        """
        Create a Cross product between two vectors.
        """
        try:
            return s.__class__(
                s[1] * v[2] - v[1] * s[2],
                s[2] * v[0] - v[2] * s[0],
                s[0] * v[1] - v[0] * s[1])
        except IndexError:
            raise TypeError, "Cross Product requires two Vectors of 3 dimensions."
    def angle(s, v):
        """
        Get the angle between two Vectors. Result in Radians.
        """
        try:
            return math.acos(s.unit * v.unit)
        except AttributeError:
            raise TypeError, "Angle requires two Vectors."
    def rotate(s, v, a):
        """
        Rotate Vector around another Vector by a specified number of Radians.
        """
        try:
            cos, sin = math.cos(a), math.sin(a)
            up = v.unit
            right = up.cross(s)
            out = right.cross(up)
            return up * (s * up) + (out * cos) + (right * sin)
        except (TypeError, AttributeError):
            raise TypeError, "Rotate requires two Vectors and an Angle."
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
            return 1 - t < s.unit * v.unit
        except (TypeError, AttributeError):
            raise TypeError, "\"Is Parallel\" requires two Vectors and a Float."
    # Vector Properties
    @property
    def length(s): return s.magnitude
    @property
    def magnitude(s):
        """
        Calculate the magnitude / length / unit of the vector. |s|
        """
        return math.sqrt(sum(s ** 2))
    @property
    def normalized(s): return s.unit
    @property
    def normal(s): return s.unit
    @property
    def unit(s):
        """
        Create a Normalized Vector.
        """
        return (s / s.magnitude) if s else s.__class__(0, 0, 0)

class Point(Vector):
    """
    A single point in 3D space.
    """
    def distance(s, v):
        return Vector(b - a for a, b in zip(s, v)).magnitude

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
    assert v1 * 2 == (2,4,6)
    assert v1 ** 2 == (1,4,9)
    assert v1 * v2 == 10
    assert v1 * m1 == (14,32,50)
    assert v1 ^ v2 == (-4,8,-4)
    print "Ok!"
