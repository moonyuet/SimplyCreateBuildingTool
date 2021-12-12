############################################
########Author : Kayla Man##################
############################################
import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def maya_main_window():
	"""
	Return the Maya main window widget as a Python object
	"""
	main_window_ptr = omui.MQtUtil.mainWindow()
	if sys.version_info.major >= 3:
		return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
	else:
		return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
class GroupDialog(QtWidgets.QDialog):
    LOCATOR_NAME = ["widthA", "widthB", "heightA", "heightB"]
    def __init__(self, parent=maya_main_window()):
        super(GroupDialog, self).__init__(parent)
        self.setWindowTitle("Simply Create Building Tool")
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
    
    def create_widgets(self):
        self.locator_btn = QtWidgets.QPushButton("Create Locators")
        self.create_distance_btn = QtWidgets.QPushButton("Measure Distances")
        self.delete_measurement_btn = QtWidgets.QPushButton("Delete Measurement")
        self.group_name_le = QtWidgets.QLineEdit()
        self.group_btn = QtWidgets.QPushButton("Group")

        self.widthSection = QtWidgets.QDoubleSpinBox()
        self.widthSection.setRange(0, 50)
        self.widthSection.setDecimals(0)
        self.widthSection.setSingleStep(1)

        self.depthSection = QtWidgets.QDoubleSpinBox()
        self.depthSection.setRange(0, 50)
        self.depthSection.setDecimals(0)
        self.depthSection.setSingleStep(1)


        self.heightSection = QtWidgets.QDoubleSpinBox()
        self.heightSection.setRange(0, 200)
        self.heightSection.setDecimals(0)
        self.heightSection.setSingleStep(1)

        self.duplicate_storey_btn = QtWidgets.QPushButton("Duplicate Storey")
        self.duplicate_floor_btn = QtWidgets.QPushButton("Duplicate Floor")
    
    def create_layout(self):
        locator_layout = QtWidgets.QHBoxLayout()
        locator_layout.addWidget(self.locator_btn)
        locator_layout.addSpacing(10)
        locator_layout.addWidget(self.create_distance_btn)
        locator_layout.addSpacing(10)
        locator_layout.addWidget(self.delete_measurement_btn)

        group_layout = QtWidgets.QHBoxLayout()
        group_layout.addWidget(self.group_name_le)
        group_layout.addWidget(self.group_btn)

        group_name_layout = QtWidgets.QFormLayout()
        group_name_layout.addRow("Group: ", group_layout)

        create_storey_layout = QtWidgets.QHBoxLayout()
        create_storey_layout.addWidget(QtWidgets.QLabel("Width Section:"))    
        create_storey_layout.addWidget(self.widthSection)
        create_storey_layout.addWidget(QtWidgets.QLabel("Depth Section:")) 
        create_storey_layout.addWidget(self.depthSection)
        create_storey_layout.addWidget(self.duplicate_storey_btn)

        create_floor_layout = QtWidgets.QHBoxLayout()
        create_floor_layout.addWidget(QtWidgets.QLabel("Height Section:"))
        create_floor_layout.addWidget(self.heightSection)
        create_floor_layout.addWidget(self.duplicate_floor_btn)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(locator_layout)
        main_layout.addLayout(create_storey_layout)
        main_layout.addLayout(group_name_layout)
        main_layout.addLayout(create_floor_layout)

    def create_connections(self):
        self.locator_btn.clicked.connect(self.create_locator)
        self.create_distance_btn.clicked.connect(self.create_measurement)
        self.delete_measurement_btn.clicked.connect(self.delete_measurement)
        self.group_btn.clicked.connect(self.set_group_name)
        self.duplicate_storey_btn.clicked.connect(self.duplicate_pieces)
        self.duplicate_floor_btn.clicked.connect(self.duplicate_floor)
    
    def create_locator(self):
        for name in self.LOCATOR_NAME:
            cmds.spaceLocator(n = name)
    def get_transform(self, name):
        attr_list = []
        x_pos = cmds.getAttr(name + ".translateX")
        y_pos = cmds.getAttr(name + ".translateY")
        z_pos = cmds.getAttr(name + ".translateZ")
        attr_list.append(x_pos)
        attr_list.append(y_pos)
        attr_list.append(z_pos)
        return attr_list

    def create_measurement(self):
        locator_list = self.LOCATOR_NAME
        get_widthA = self.get_transform(locator_list[0])
        get_widthB = self.get_transform(locator_list[1])
        get_heightA = self.get_transform(locator_list[2])
        get_heightB = self.get_transform(locator_list[3])
        distance_dimension_width_shape = cmds.distanceDimension(sp = get_widthA, ep = get_widthB)
        distance_dimension_height_shape = cmds.distanceDimension(sp = get_heightA, ep = get_heightB)
        distance_width_transform = cmds.listRelatives(distance_dimension_width_shape, parent=True)
        distance_height_transform = cmds.listRelatives(distance_dimension_height_shape, parent=True)
        cmds.rename(distance_width_transform[0],"distanceDimension_width")
        cmds.rename(distance_height_transform[0],"distanceDimension_height")
    
    def delete_measurement(self):
        locator_list = self.LOCATOR_NAME
        for locator in locator_list:
            cmds.delete(locator)
        cmds.delete("distanceDimension_width")
        cmds.delete("distanceDimension_width")
      
    def duplicate_pieces(self):

        number_widthSection = self.widthSection.value()
        number_depthSection = self.depthSection.value()
        
        i = 1

        while i <=number_widthSection:
            sectionWidth = cmds.getAttr("distanceDimension_width.distance") 
            cmds.duplicate()
            cmds.move(-sectionWidth,0,0,relative=True)

            i+=1
        cmds.rotate(0,-90,0,relative=True)

        i = 1

        while i <= number_depthSection:
            sectionWidth = cmds.getAttr("distanceDimension_width.distance") 
            cmds.duplicate()
            cmds.move(0,0,-sectionWidth,relative=True)

            i+=1
        cmds.rotate(0,-90,0,relative=True)
        
        i = 1
        while i <=number_widthSection:
            sectionWidth = cmds.getAttr("distanceDimension_width.distance") 
            cmds.duplicate()
            cmds.move(sectionWidth,0,0,relative=True)

            i+=1
        cmds.rotate(0,-90,0,relative=True)
        
        i = 1

        while i< number_depthSection:
            sectionWidth = cmds.getAttr("distanceDimension_width.distance") 
            cmds.duplicate()
            cmds.move(0,0,sectionWidth,relative=True)

            i+=1
        

    def duplicate_floor(self):
        i = 1
        number_heightSection = self.heightSection.value()
        while i < number_heightSection:
            sectionHeight = cmds.getAttr("distanceDimension_height.distance") 
            cmds.duplicate()
            cmds.move(0,sectionHeight,0,relative=True)

            i+=1

    def set_group_name(self):
        group_name = self.group_name_le.text()

        if not group_name:
            print("Please name the group!")
            return
        group_obj = cmds.ls(selection=True)
        cmds.group(group_obj, n = group_name)


if __name__ == "__main__":

	try:
		group_dialog.close() # pylint: disable=E0601
		group_dialog.deleteLater()
	except:
		pass

	group_dialog = GroupDialog()
	group_dialog.show()
