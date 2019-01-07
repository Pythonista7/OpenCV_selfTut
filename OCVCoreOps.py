#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:16:44 2019

    OPENCV CORE OPERATIONS

@author: ashwin
"""

import cv2

#%%
img=cv2.imread("/home/ashwin/OpenCVWorkSpace/Untitled Folder/assets/img.jpeg")
''' BASIC OPERATIONS '''

#General Image properties can be obtained as follows
print("Shape=> ",img.shape)
print("Size=> ",img.size)

#Displaying the image
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Segmenting the face using basic array slices
face=img[95:180,95:180]
cv2.imshow('face',face)
cv2.waitKey(0)
cv2.destroyAllWindows()

#overlaying on image using basic array ops
img[95:180,10:95]=face
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Do not use split/mergre unless needed.Computationally expensive.Use numpy ops insted.
img=cv2.imread('/home/ashwin/OpenCVWorkSpace/Untitled Folder/assets/img.jpeg')

#Splitting images into their seperate color channels
b,g,r=cv2.split(img)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Merging all the split channels
img=cv2.merge((b,g,r))
cv2.imshow('Merged',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Adding broders to image using cv2.copyMakeBorder function
img=cv2.copyMakeBorder(img,4,4,4,4,cv2.BORDER_WRAP)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''###################################################################### '''
#%%
''' ARITHMETIC OPERATIONS '''

#Lets consider 2 sample images
s1=cv2.imread('/home/ashwin/OpenCVWorkSpace/Untitled Folder/assets/samp1.jpeg')
s2=cv2.imread('/home/ashwin/OpenCVWorkSpace/Untitled Folder/assets/samp2.jpeg')
cv2.imshow('samp1',s1)
cv2.waitKey(0)
cv2.imshow('samp2',s2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Addition of 2 images
res=cv2.add(s1,s2)
cv2.imshow('Add',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Blending 2 images
res=cv2.addWeighted(s1,0.3,s2,0.7,0)
cv2.imshow('Blend',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################################
#%%
'''       Bit wise operations   '''

big=cv2.imread('/home/ashwin/OpenCVWorkSpace/Untitled Folder/assets/big.jpg')
s1=cv2.imread('/home/ashwin/OpenCVWorkSpace/Untitled Folder/assets/logo2.png')

#to insert s1 in big at top left corner
row,col,channel=s1.shape
#ROI=Regoin Of Intrest
roi=big[0:row,0:col]

#To create a mask
s1grey=cv2.cvtColor(s1,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(s1grey,10,255,cv2.THRESH_BINARY)     #Original mask
invmask=cv2.bitwise_not(mask)   #Inversted mask

cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.imshow('Inverted',invmask)
cv2.waitKey(0)

#black out space for logo from main big img
big_bg=cv2.bitwise_and(roi,roi,mask=invmask)
cv2.imshow('biglogo Background',big_bg)
cv2.waitKey(0)

big_fg=cv2.bitwise_and(s1,s1,mask=mask)

#Add both bg and fg
dst=cv2.add(big_bg,big_fg)

#Insert carved and placed logo into the ROI
big[0:row,0:col]=dst

cv2.imshow('Finally',big)
cv2.waitKey(0)
cv2.destroyAllWindows()