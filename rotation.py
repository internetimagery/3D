# Rotations

import math
import matrix
import collections


# http://mathworld.wolfram.com/EulerAngles.html

def D(radian): # Z
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (cos,   sin,    0),
        (-sin,  cos,    0),
        (0,     0,      1)
    ))

def C(radian): # X
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (1,     0,      0),
        (0,     cos,  sin),
        (0,     -sin, cos)
    ))

B = D

# http://www.euclideanspace.com/maths/geometry/rotations/euler/index.htm

def heading(radian): # Azimuth | Yaw | Theta
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (cos,   -sin,   0),
        (sin,  cos,     0),
        (0,     0,      1)
    ))
def attitude(radian): # Elevation | Pitch | Phi
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (cos,   0,    sin),
        (0,     1,      0),
        (-sin,  0,    cos)
    ))
def bank(radian): # Tilt | Roll | Psi
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (1,     0,      0),
        (0,     cos, -sin),
        (0,     sin,  cos)
    ))

def euler(m):
    if m[1][0] > 0.9998: # North pole singularity
        heading = math.atan2(m[0][2], m[2][2])
        attitude = math.pi/2
        bank = 0
    elif m[1][0] < -0.9998: # Singularity at south pole
        heading = math.atan2(m[0][2], m[2][2])
        attitude = -math.pi/2
        bank = 0
    else:
        heading = math.atan2(-m[2][0], m[0][0])
        attitude = math.asin(m[1][0])
        bank = math.atan2(-m[1][2], m[1][1])
    return (bank, attitude, heading)

# m1 = heading(math.radians(30)) # z
# m2 = attitude(math.radians(40)) # y
# m3 = bank(math.radians(50)) # x
# m4 = (m1 * m2) * m3
# print euler(m4)
# e = euler(m4)[0]
# print math.degrees(e)
# m5 = bank(e * -1)
# m4 *= m5
# e = euler(m4)[1]
# print math.degrees(e)
# m5 = attitude(e * -1)
# m4 *= m5
# e = euler(m4)[2]
# print math.degrees(e)


# the dot product of two normalized vectors is the COSINE of the angle between them; arccos(dot(a,b)) would give you the angle (in radians)

#
#
#
#
# def angle(axis, angle):
#     angle = math.radians(angle)
#     cos, sin = math.cos(angle), math.sin(angle)
#     base = [[cos,sin],[sin,cos]]
#     a = []
#     print a.insert(axis, )
#
# print angle(1, 50)

class angle(collections.Mapping): # degrees
    __slots__ = ("_funcs")
    def sincos(f):
        def wrapper(s, a):
            a = math.radians(a)
            return f(s, math.cos(a), math.sin(a))
        return wrapper
    def __init__(s): s._funcs = {"x" : s.x, "y" : s.y, "z" : s.z}
    @sincos
    def x(s, sin, cos): return matrix.Matrix(((1,0,0),(0,cos,-sin),(0,sin,cos)))
    @sincos
    def y(s, sin, cos): return matrix.Matrix(((cos,0,sin),(0,1,0),(-sin,0,cos)))
    @sincos
    def z(s, sin, cos): return matrix.Matrix(((cos,-sin,0),(sin,cos,0),(0,0,1)))
    def __getitem__(s, k): return s._funcs[k]
    def __iter__(s): return iter(s._func)
    def __len__(s): return 3
angle = angle()
