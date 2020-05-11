import maya.cmds as cmds 

class MayaGeometry(object):

    def __init__(self):
        self.name = ""

    def __str__(self):
        return self.name

    def set_translation(self, x=None, y=None, z=None):
        self._get_transformation(cmds.move, x, y, z)

    def get_translation(self):
        return cmds.xform(self.name, query=True, translation=True)

    def set_rotation(self, x=None, y=None, z=None):
        self._get_transformation(cmds.rotate, x, y, z)

    def get_rotation(self):
        return cmds.xform(self.name, query=True, rotation=True)
        
    def set_scale(self, x=None, y=None, z=None):
        self._get_transformation(cmds.scale, x, y, z)

    def get_scale(self):
        return cmds.xform(self.name, query=True, scale=True)

    def __del__(self):
        self.delete()

    def delete(self):
        if self.exist():
            cmds.delete(self.name)

    def exist(self):
        return cmds.objExists(self.name)

    def _get_transformation(self, command, x=None, y=None, z=None):
        for axis in ('x', 'y', 'z'):
            value = locals()[axis]
            if value:
                options = {axis : True, 'objectSpace' : True, 'absolute' : True}
                command(value, self.name, **options)
