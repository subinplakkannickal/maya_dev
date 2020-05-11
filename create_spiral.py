import maya.cmds as cmds

def create_spiral(amp, spin, count, width):
    height = 0
    angle = 0

    for i in range(count):
        transform_name = "sphere_{}".format(i)
        transform, shape = cmds.sphere(name=transform_name, pivot=[width, height, 0])
        height += amp
        _attr = "{}.rotateY".format(transform_name)
        cmds.setAttr(_attr, angle)
        angle += spin