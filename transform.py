# Transformation

import matrix

class Transform(matrix.Matrix):
    pass

if __name__ == '__main__':
    t1 = matrix.Identity(4)
    print t1



#  Assuming a row major 3x3 matrix, where the first row is 3-vector ''X'', then ''Y'', then ''Z''.
#
# X.Normalise();
# Y.Normalise();
# Z = X cross Y;
# Y = Z cross X;
#
# That should make an orthonormal 3x3 matrix.
