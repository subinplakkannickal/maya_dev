import maya.cmds as cmds


def move_sphere(sphere_list):
    """ Moving each spere in scene in z diretion.
    """
    for _sphere in sphere_list:
        cmds.select(_sphere, r=True)
        translate_z_attr = ".translateZ"
        current_translate_z = cmds.getAttr(translate_z_attr)
        current_translate_z += 1
        cmds.setAttr(translate_z_attr, current_translate_z)

if __name__ == "__main__":
    transform_1, shape_1 = cmds.sphere(r=0.5, name='my_sphere_1')
    transform_2, shape_2 = cmds.sphere(r=1, name='my_sphere_2')
    transform_3, shape_3 = cmds.sphere(r=2, name='my_sphere_3')

    sphere_list = [transform_1, transform_2, transform_3]
    
    move_sphere(sphere_list)