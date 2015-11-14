# Transformation Matrix

import math
import itertools

class Transform(tuple):
    """
    Transformation Matrix

    Transform() <--- Identity
    Transform(
        [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10,11,12],
        [13,14,15,16]
        ) <--- By Row
    Transform(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) <--- a11, a12, a13, a21, a22, ... etc
    Transform(tuple(c+r for c in range(4)) for r in range(1,17,4)) <--- generator / nested iterable
    """
    __slots__ = ()
    cols = 4
    rows = 4
    def __new__(cls, *nums):
        try:
            l = len(nums)
            if l == 16: # Full array of numbers
                return tuple.__new__(cls, (nums[r:r+4] for r in range(0,16,4)))
            if l == 4: # Creation by rows
                return tuple.__new__(cls, nums)
            if l == 1: # Iterable / Another matrix
                return tuple.__new__(cls, nums[0])
            if l == 0: # Empty Matrix / Identity Matrix
                return tuple.__new__(cls, (tuple(1.0 if c == r else 0.0 for c in range(4)) for r in range(4)))
            raise Exception
        except:
            raise ValueError, "Invalid arguments for Matrix."
    def __repr__(s):
        string = tuple(tuple(str(b) for b in a) for a in s)
        col = max(max(len(b) for b in a) for a in string)
        return "\n".join(" ".join(b.center(col) for b in a) for a in string)
