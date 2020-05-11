import random
import maya.cmds as cmds


def clear_scene():
    """ Delete all existing spheres from scene.
    """
    sphere_list = cmds.ls('my_sphere*')

    if len(sphere_list) > 0:
        cmds.delete(sphere_list)


def create_random_sphere(transform, limit):
    """
    """
    for i in range(limit):
        instance_ = cmds.instance(transform, name=transform + "_instance#") 

        x, y, z = random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)
        cmds.move(x, y, z, instance_) 

        scaling_factor = random.uniform(0.3, 1)
        cmds.scale(scaling_factor, scaling_factor, scaling_factor, instance_)

if __name__ == "__main__":
    clear_scene()
    transform, shape = cmds.polySphere(r=0.5, name='my_sphere#')
    create_random_sphere(transform, 50)