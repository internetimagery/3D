# Testing local rotation
import maya.cmds as cmds
import math

def makeAttrs(node):
    for ax in ["locx","locy","locz"]:
        if not cmds.attributeQuery(ax, n=node, ex=True):
            cmds.addAttr(node, sn=ax, k=True)

def rotate(node):
    xyz = (cmds.getAttr(node + "." + ax) for ax in ["locx","locy","locz"])
    matrix = cmds.xform(node, q=True, m=True)
    matrix = [[matrix[r+c] for c in range(4)] for r in range(0,16,4)]
    cosx, cosy, cosz = (math.cos(angle) for angle in xyz)
    sinx, siny, sinz = (math.sin(angle) for angle in xyz)
    rotMatrix = (
        (cosy + cosz, -sinz,  siny),
        (0, cosx,  -sinx),
        (-siny, sinx,  cosx + cosy)
    )


    print x, y, z
sel = cmds.ls(sl=True)
makeAttrs(sel[0])
print getAxis(sel[0])
