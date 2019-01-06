#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:28:14 2019

MOUSE AS PAINT BRUSH

@author: ashwin
"""

import cv2
import numpy as np

#following are control variables
draw=False
prev_event=cv2.EVENT_MOUSEHWHEEL #use something we dont need.Using insted of 0

#this is default color can be changed
color=[0,255,0]

def paint_p(event,x,y,flags,param):
    #The function that draws
    global xp,yp,prev_event,draw
    
    if(event==cv2.EVENT_LBUTTONDOWN):
       xp=x
       yp=y
       draw=True
       
    if(event==cv2.EVENT_MOUSEMOVE and prev_event!=cv2.EVENT_LBUTTONDOWN and draw):
       
       cv2.line(img,(xp,yp),(x,y),color,1)
       xp=x
       yp=y
       return
        
    if(event==cv2.EVENT_LBUTTONUP):
        draw=False
        return
    #Recording previous event so we know when bursh is down and when its not.
    prev_event=event
    return 


# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Canvas')

#Display text
txt='by Pythonista7- ESC -> QUIT, r->reset , s-> save , j->Blue , k->Green , l-> Red'
#Font style for default text
font=cv2.FONT_HERSHEY_PLAIN

cv2.putText(img,txt,(10,500),font,.6,(255,255,255),1,cv2.LINE_AA)

#Monitoring mouse
cv2.setMouseCallback('Canvas',paint_p)

while(1):
   cv2.imshow('Canvas',img)
   k=cv2.waitKey(1)&0xFF
   if (k==27):
       break
   if (k==ord('s')):
       cv2.imwrite('MonaLisa.png',img)#'cause you DaVinci 
   if(k==ord('j')):#Blue
       color=[255,0,0]
   if(k==ord('k')):#Green
       color=[0,255,0] 
   if(k==ord('l')):#Red
       color=[0,0,255]    
   if(k==ord('r')):
       img = np.zeros((512,512,3), np.uint8)
       cv2.putText(img,txt,(10,500),font,.6,(255,255,255),1,cv2.LINE_AA)

cv2.destroyAllWindows()