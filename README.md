# Blender Addon: Object Morph

## Description
This is a Blender addon that let's you transform one or more meshes into a single target mesh as long as each meshe has the same number of vertices.

## Installation
1. Download the 'Skao.py' file and save it somewhere you can remember on your computer.
2. Open Blender and go to the menu bar at the top of the screen and select "File"
3. Navigate to the, "User Preferences..." Option, click this
4. A window should appear with buttons at the top, one should say,"Addons" click on this button.
5. Look to the bottom of the window and there should be an, "Install From File" option, click this and navigate to where you saved the,"Skao.py" file. Select this file
6. The window should now have one section in it that says, "Mesh: Shape Key From Object" which will be grayed out with an unchecked box. Check the box and it should no longer be grayed out.
7. You're good to go!
  * If you open a new file or reload the file without saving, you will have to redo this process.
  * If you want this addon installed by default in all future projects, first open up a brand new file before following this, then hit "Save User Settings" in the "User Prefences" window. This will save whatever setup you have currently in Blender as your new startup file; so don't do this unless you want your current Blender configuration to be your new Default!
  
## Use
1. Shift-Click all of the objects that you want to transform, these will be known as your "Selected Objects"
2. Without deselecting your "Selected Objects", shift-click the object you want to transform them into, this will be highlighted a different color than them and be known as your "Active Object". You can only have one "Active Object"
3. Tap your Space-Bar and type in, "Shape Keys" until you find the option, "Shape Key: Active Object", click this.
4. Blender may now lock up based on how many items you selected and how many vertices they have. The lockup can take anywhere from less than a second to hours or more depending on how complex the objects are.
  * If you want to see if it has actually locked up, enable the system console before using this operation. Look below to see how to do so. The operator will continue to print out as long as it is working.
5. After Blender finishes, your Selected Objects should now be transformed into the shape of your Active Object!
  * They may be rotated differently, this is a hitch between softwares that sometimes happens, don't worry about it!

## Use with Shape-Keys
1. Select each of the objects you want to transform and give them a Shape-Key.
  * If you don't know how to give them a Shape-Key, then select the Object, click on the "Data" icon in the menu (It looks like 3 dots connected by lines) and you will see a "Shape Keys" section. Press then, '+' button in this section and a new entry will appear in the Shape Keys list named "Basis". This is your base Shape Key.
2. Deselect the objects, then perform the steps detailed in the "How To Use" section. Your objects may not transform visibly when this completes, but don't worry, just continue with the following steps.
3. Deselect your objects, then one-by-one click on them and add a second Shape Key in the same way you added the first. This new shape key will likely be named, "Shape Key 1".
4. Once you have added "Shape Key 1" to each object, click on the, "Value" slider and move the value towards 1.00. The mesh should transform into the desired shape.
  * If it doesn't change into the desired shape and just stays the same, then you may have missed a step. Try again if this happens.
  * If it continues to not work, this may be a glitch. Check the, "Known Issues" section of this document. If it cannot be found in the, "Known Issues", then sadly all I can suggest is to ask on a forum, or to wait and hopefully it will be fixed shortly.
5.If your mesh now transforms successfully with the movement of the "Value" Slider, you have successfully used this addon to make a shape key! Good job!

## Opening the System Console
1. In Blender, go to the menu bar at the top of the screen and find the, "Window" option, click it.
2. Find and select the, "Toggle System Console" option in the drop down list, this will open a console window that the addon will print to during operation.

## Some Extra Info
* Let me start by saying, your meshes all NEED to have the exact same vertex count as one another. This is working as intended and is not an issue, it just is necessary to make the system function properly. You will be told in the system console if they all match or not.
* For the best results, try to keep the topology similar and polygon counts the same as well. This addon is designed to work to transform a base mesh into another version of it that has been sculpted on. 

## Known Issues
* Selecting many objects to transform, or applying this to an object with a moderatly high vertex count will make this script lock up Blender and will take long amounts off time to finish, at which point it will unlock Blender. The System Console will continue to print as long as it is still working during these Lockups, but they can take hours even at around 16,000 polygons.
* Higher polygon counts seem to introduce glitches into the resulting meshes where they don't mimic the goal mesh perfectly.
* The more deformed the goal mesh is compared to the meshes you want to transform, the more likely glitches will arise. These glitches can vary from a few vertices being a little out of place, to the entire mesh being a mess of scattered triangles that have no resemblance to either mesh.

## Planned Updates & Fixes
* I hope to be fixing the run-time issues so that it can work with roughly 20,000 vertices in reasonable time spans.
* I hope to figure out how to resolve the glitches in the geometry that are showing up.
