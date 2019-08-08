# Deep Unclone

import FreeCAD, Draft, Arch


objClone = FreeCAD.ActiveDocument.ActiveObject

# this line does not work. I am not sure what the API name is of BIM_unclone from here:
# https://github.com/yorikvanhavre/BIM_Workbench/blob/d2613c1c802f9e374ab32f8a7857b7df719a0fdf/BimUnclone.py
objNew = Arch.Unclone(objClone)

objNew.Placement.Base.X =  objClone.Placement.Base.X
objNew.Placement.Base.Y =  objClone.Placement.Base.Y
objNew.Placement.Base.Z =  objClone.Placement.Base.Z

if objNew.Base == True:
   sketchExisting = objNew.base
   sketchNew = sketchExiting copy # not sure what the code is to copy
   objNew.base = sketchNew