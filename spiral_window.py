import maya.cmds as cmds
from create_spiral import create_spiral

def create_window():
    window = cmds.window(title="Create Spiral", widthHeight=(200, 300))
    cmds.columnLayout(columnAttach=('both', 5), rowSpacing=5, adjustableColumn=True)
    amp = cmds.floatFieldGrp(numberOfFields=1, label='Amp', value1=1.0)
    spin = cmds.floatFieldGrp(numberOfFields=1, label='Spin', value1=30) 
    count = cmds.intFieldGrp(numberOfFields=1, label='Count', value1=20) 
    width = cmds.floatFieldGrp(numberOfFields=1, label='Width', value1=3)
    
    cmds.button(label='Create', command=lambda k : create_spiral_button_command(amp, spin, count, width))
    cmds.showWindow(window)
    
def create_spiral_button_command(amp, spin, count, width):
    amp_value = cmds.floatFieldGrp(amp, query=True, value1=True)
    spin_value = cmds.floatFieldGrp(spin, query=True, value1=True) 
    count_value = cmds.intFieldGrp(count, query=True, value1=True) 
    width_value = cmds.floatFieldGrp(width, query=True, value1=True)
    create_spiral(amp_value, spin_value, count_value, width_value)
