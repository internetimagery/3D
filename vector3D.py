"""
A Vector in 3D space
"""
import math
import collections

_3D = collections.namedtuple("Vector", ("x","y","z"))
class Vector(_3D):
    """
    A Simple Vector that allows math operations to be performed on it.
    """
    __slots__ = ()
    def __new__(cls, *pos):
        """
        Create a new Vector after each operation.
        """
        try:
            x, y, z = pos if len(pos) == 3 else pos[0] if pos else (0.0,0.0,0.0)
        except:
            raise ValueError, "3D Vector must consist of three numbers. X, Y, Z."
        return _3D.__new__(cls, float(x), float(y), float(z))
    def _scalar(func):
        """
        Allow scalar operations.
        """
        def wrapper(s, v):
            t = type(v)
            if t == int or t == float:
                v = (v, v, v)
            return func(s, v)
        return wrapper
    # Basic Math Operations
    def __neg__(s): return s.__class__(-a for a in s)
    def __pos__(s): return s.__class__(+a for a in s)
    def __ne__(s, v): return False if s == v else True
    def __nonzero__(s): return True if s[0] or s[1] or s[2] else False
    @_scalar
    def __add__(s, v): return s.__class__(a + b for a, b in zip(s, v))
    @_scalar
    def __div__(s, v): return s.__class__(a / b for a, b in zip(s, v))
    @_scalar
    def __mod__(s, v): return s.__class__(a % b for a, b in zip(s, v))
    @_scalar
    def __sub__(s, v): return s.__class__(a - b for a, b in zip(s, v))
    @_scalar
    def __pow__(s, v): return s.__class__(a ** b for a, b in zip(s, v))
    @_scalar
    def __truediv__(s, v): return s.__class__(a / b for a, b in zip(s, v))
    @_scalar
    def __lt__(s, v): return True if s[0] < v[0] and s[1] < v[1] and s[2] < v[2] else False
    @_scalar
    def __gt__(s, v): return True if s[0] > v[0] and s[1] > v[1] and s[2] > v[2] else False
    @_scalar
    def __eq__(s, v): return True if s[0] == v[0] and s[1] == v[1] and s[2] == v[2] else False
    @_scalar
    def __le__(s, v): return True if s[0] <= v[0] and s[1] <= v[1] and s[2] <= v[2] else False
    @_scalar
    def __ge__(s, v): return True if s[0] >= v[0] and s[1] >= v[1] and s[2] >= v[2] else False
    @_scalar
    def __floordiv__(s, v): return s.__class__(a // b for a, b in zip(s, v))
    # More Functionality
    def __mul__(s, v): # (*)
        t = type(v)
        if t == int or t == float: return s.__class__(a * v for a in s)
        return s.dot(v)
    def dot(s, v):
        """
        Create a Dot product between two vectors.
        """
        if len(v) != 3: raise TypeError, "Dot Product requires two Vectors."
        return sum(a * b for a, b in zip(s, v))
    def __xor__(s, v): return s.cross(v) # (^)
    def cross(s, v):
        """
        Create a Cross product between two vectors.
        """
        if len(v) != 3: raise TypeError, "Cross Product requires two Vectors."
        return s.__class__(
            s[1] * v[2] - v[1] * s[2],
            s[2] * v[0] - v[2] * s[0],
            s[0] * v[1] - v[0] * s[1])
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
    def isEquivalent(s, v, t):
        """
        Returns True if this vector and another are within a given tolerance of being equal.
        """
        return False not in set(abs(a - b) < t for a, b in zip(s, v))
    def isParallel(s, v, t):
        """
        Returns True if this vector and another are within the given tolerance of being parallel.
        """
        try:
            return 1 - t < s.unit * v.unit
        except (TypeError, AttributeError):
            raise TypeError, "Is Parallel requires two Vectors and a Tolerance."
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

class Point(_3D):
    """
    A single point in 3D space.
    """
    def distance(s, v):
        return Vector(b - a for a, b in zip(s, v)).length

v1 = Vector(1,2,3)
v2 = Vector(1.1,2,3)
print v1.isParallel(v1, 0.1)
