# Rotations

import math
import matrix
import collections










def yaw(radian): # Z
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (cos,   sin,    0),
        (-sin,  cos,    0),
        (0,     0,      1)
    ))

def roll(radian): # X
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (1,     0,      0),
        (0,     cos,  sin),
        (0,    -sin,  cos)
    ))

def pitch(radian): # Y
    cos, sin = math.cos(radian), math.sin(radian)
    return matrix.Matrix((
        (cos,   0,   -sin),
        (0,     1,      0),
        (sin,   0,    cos)
    ))

def angle(m):
    # heading, attitude, bank
    return (
        math.atan2(m[0][2],m[2][2]) if m[1][0] == 1.0 or m[1][0] == -1 else math.atan2(-m[2][0],m[0][0]),
        math.asin(m[1][0]),
        0 if m[1][0] == 1.0 or m[1][0] == -1 else math.atan2(-m[1][2], m[1][1])
    )

m1 = pitch(math.radians(40))
m2 = yaw(math.radians(25))
m3 = yaw(math.radians(15))
m4 = m1 * m2 * m3
an = [math.degrees(a) for a in angle(m4)]
print an

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
