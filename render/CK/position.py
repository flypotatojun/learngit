# coding=utf-8
'''
Created on 2017628

@author: CK
'''
# -*- coding: UTF-8 -*-
'''
在X方向依次排列所选择的物体，或将散乱的物体坐标归零

'''

import maya.cmds as mc
sels=mc.ls(sl=True)
start_position=[0,0,0]
total_distance = 0
together = True
for sel in sels:
    cur_position=mc.xform(sel,q=True,ws=True,rp=True)
    if  cur_position!=start_position:
        together=False
        break
for sel in sels:
    if together:
        print "separation"
        xmin,ymin,zmin,xmax,ymax,zmax = mc.xform(sel,q=True,ws=True,bb=True)
        width=abs(xmax-xmin)
        if sel !=sels[0]:
            total_distance += width/2
            mc.move(total_distance,sel,r=True,x=True)
        total_distance += width/2

    else:
        mc.move(start_position[0],start_position[1],start_position[2])