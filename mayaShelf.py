import sys
from importlib import reload
import maya.cmds as cmds
import mtoa.utils as utils

path = r"YOUR PATH"
sys.path.append(path)
IMG_PATH = path + "/img/"


MENU = "CreateBuildingTool"

def delete_plugin_shelf():
    if cmds.shelfLayout(MENU, exists=True):
        cmds.deleteUI(MENU)


def plugin_shelf():
    delete_plugin_shelf()
    cmds.shelfLayout(MENU, parent="ShelfLayout")
    cmds.shelfButton(parent=MENU, annotation='CreateBuildingTool',
                     image1=IMG_PATH + "shelf_logo.png",
                     command='import group_dialog;reload(group_dialog);group_dialog = GroupDialog(); group_dialog.show();')
                     
plugin_shelf()