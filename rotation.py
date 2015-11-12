# Rotations

import math
import matrix
import collections

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


print angle.x(40)
