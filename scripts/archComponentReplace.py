# Deep Unclone

import FreeCAD, Draft, Arch


# select first the element to be replaced and then the element to replace it

sel = Gui.Selection.ActiveObject

# check if objects are architectural components

oldObj = sel[0]
newObj = sel[1]

# get subtractions
subs = oldObj.Subtractions


# Check where the object is in the tree

# possible to replace the contents of the object instead of replacing the object?

# assing subtractions to new object
newObj.Subtractions = subs

# replace element in the tree structre
