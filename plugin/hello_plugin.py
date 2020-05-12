import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

commandName = "hello"

class HelloCommand(OpenMayaMPx.MPxCommand):
    def __init__(self):
        super(HelloCommand, self).__init__()

    def doIt(self, *args):
        print("HelloNew")

    
def cmd_creater():
    return OpenMayaMPx.asMPxPtr(HelloCommand())

def initializePlugin(mobject):
    maya_plugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        maya_plugin.registerCommand(commandName, cmd_creater)
    except:
        sys.stderr.write('Failed to register: {}'.format(commandName))

def uninitializePlugin(mobject):
    maya_plugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        maya_plugin.deregisterCommand(commandName)
    except:
        sys.stderr.write('Failed to deregister: {}'.format(commandName))
