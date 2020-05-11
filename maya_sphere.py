import maya.cmds as cmds
from maya_geometry import MayaGeometry

class Sphere(MayaGeometry):

    def __init__(self, name="Sphere", **kwargs):
        super(Sphere, self).__init__()
        kwargs['name'] = name
        kwargs['object'] = True
        self._kwargs = kwargs
        transform, shape = cmds.sphere(**kwargs)
        self.name = transform
