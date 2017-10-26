import maya.cmds as cmds
selection = cmds.ls(sl=True)
a=0
b=1
for sels in selection:
    sel = cmds.listRelatives(sels)
    if cmds.getAttr(sel[0]+'.overrideEnabled'):
            cmds.setAttr(sel[0]+'.overrideEnabled',a)
            cmds.setAttr(sel[0]+'.overrideLevelOfDetail',a)
    else:
            cmds.setAttr(sel[0]+'.overrideEnabled',b)
            cmds.setAttr(sel[0]+'.overrideLevelOfDetail',b)