# SimplyCreateBuildingTool
A Maya Plugin briefly helps to create a building within a minute. This plugin takes reference from Autodesk Maya Modeling Tutorial- Create a Building with Python by Daniel Peter, attempting to make the process easier for artists to create simple building. 


# Installation
1. Download the zip file of this project/Clone the scripts to your computer and add it into scripts/your maya project
2. Edit "YOUR PATH" in mayaShelf.py to locate the project path(if you clone your project in C:/Users/{YourUserName}, then your path would be "C:/Users/{YourUserName}/SimplyCreateBuildingTool/SimplyCreateBuildingTool"; if you download a zipped file and unzip it in in C:/Users/{YourUserName}, then your path would be "C:/Users/{YourUserName}/SimplyCreateBuildingTool-main/SimplyCreateBuildingTool")
3. Save the edited mayaShelf.py.
4. Open Maya and go to Script Editor
![alt text](https://github.com/moonyuet/SimplyCreateBuildingTool/blob/main/SimplyCreateBuildingTool/img/screenCapture/script_editor_maya.png?raw=true)

5. Go to "File", Click "Open Script", locate mayaShelf.py 
6. Execute the script by selecting all content and hit "Ctrl + Enter"

![alt text](https://github.com/moonyuet/SimplyCreateBuildingTool/blob/main/SimplyCreateBuildingTool/img/screenCapture/script_editor_open_script_screencap.png?raw=true)

7. You will see new custom menu in your maya shelf and a new shelf button inside
8. Click the shelf button and enjoy creating simple building. 

![alt text](https://github.com/moonyuet/SimplyCreateBuildingTool/blob/main/SimplyCreateBuildingTool/img/screenCapture/maya_shelf_screencap.png?raw=tr)

# Plugin Panel
The screenshot below shows the panel after hitting the shelf button

![alt text](https://github.com/moonyuet/SimplyCreateBuildingTool/blob/main/SimplyCreateBuildingTool/img/screenCapture/layout_screencap.png?raw=true)

**Create Locator**: Create 4 locators named "widthA", "widthB", "heightA", "heightB"

**Create Measurement**: Measuring distance between "widthA" and "widthB" and distance between "heightA" and "heightB"

**Delete Measurement**: Delete all 4 locators and measurements

**Width Section**: Number of sections you want for front and back side of the storey.

**Depth Section**: Number of sections you want for left and right side of the storey.

**Duplicate Storey**: Create a storey with the data from **Width Section** and **Depth Section**

**Group**: Group the meshes (Good to use after creating the storey)

**Height Section**: Number of floor you want for the building. 

**Duplicate Floor**: Duplicate the floor based on **Height Section**.

# Future Goal
I will add one more feature after this release, meaning that version 2.0 will be around in the future.
The feature allows the users to select the certain modular pieces and delete them. The user can add other different modular pieces to the deleted area and makes the building more believable. 
