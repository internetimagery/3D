"""
A Vector in 3D space
"""
import math
import collections

Vector3D = collections.namedtuple("Vector", ("x","y","z"))
class Vector(Vector3D):
    """
    A Simple Vector that allows math operations to be performed on it.
    """
    def __new__(cls, *pos):
        """
        Create a new Vector after each operation.
        """
        try:
            x, y, z = pos if len(pos) == 3 else pos[0]
        except:
            raise ValueError, "3D Vector must consist of three numbers. X, Y, Z."
        return Vector3D.__new__(cls, float(x), float(y), float(z))
    def _scalar(func):
        """
        Allow scalar operations.
        """
        def wrapper(s, v):
            t = type(v)
            if t == int or t == float:
                v = (v, v, v)
            elif t != s.__class__:
                raise TypeError, "Operation requires a scalar or Vector."
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
    def __mul__(s, v): return s.dot(v) # (*)
    def dot(s, v):
        """
        Create a Dot product between two vectors.
        """
        if type(v) != s.__class__: raise TypeError, "Dot Product requires two Vectors."
        return sum(a * b for a, b in zip(s, v))
    def __xor__(s, v): return s.cross(v) # (^)
    def cross(s, v):
        """
        Create a Cross product between two vectors.
        """
        if type(v) != s.__class__: raise TypeError, "Cross Product requires two Vectors."
        return s.__class__(
            s[1] * v[2] - v[1] * s[2],
            s[2] * v[0] - v[2] * s[0],
            s[0] * v[1] - v[0] * s[1])
    def angle(s, v):
        """
        Calculate the angle between two Vectors. Result in Radians.
        """
        if type(v) != s.__class__: raise TypeError, "Angle requires two Vectors."
        m = s.magnitude * v.magnitude
        return math.acos((s.dot(v) / m) if m else 0.0)
    @property
    def unit(s): return s.magnitude
    @property
    def length(s): return s.magnitude
    @property
    def magnitude(s):
        """
        Calculate the magnitude / length / unit of the vector. |s|
        """
        return math.sqrt(sum(s ** 2))
    @property
    def normal(s): return s.normalized
    @property
    def normalized(s):
        """
        Create a Normalized Vector out of an existing vector.
        """
        m = s.magnitude
        return (s / m) if m else s.__class__(0,0,0)

v1 = Vector([3,3,0])
v2 = Vector(2,3,1)
# v3 = v2 + 1
print math.acos(0)

# rot
#
# 	Operation: Returns a vector that represents the position of a point after it's rotated a specified number of radians about a specified axis.
# 	                   Rotation is counter-clockwise as viewed downward from the axis end position.
# 	Supported Data types: vector, float
# 		vector rot(vector point, vector axis, float angle )
# 		point is the position of a point in the world coordinate system.
# 		axis is the axis around which the point rotates. The axis is a line that passes through the origin and the specified axis position.
# 		angle is the number of radians the point rotates.
#
# 	Example: rot(<<3,3,0>>,<<1,0,0>>,0.5) Returns <<3, 2.633, 1.438>>
# 	               This is a vector representing the position of point <<3,3,0>> after rotating it 0.5 radians around the axis represented by <<1,0,0>>
