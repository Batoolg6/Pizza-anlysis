# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 14:49:56 2025

@author: USER
"""

import cv2
img = cv2.imread(r"images.jpg")

print(img.shape)
print(img.size)
resize_img = cv2.resize(img,(100,100))
cv2.imshow("original imag",img)
#cv2.imshow("resize img",resize_img) 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #same1
cv2.imshow("gray_imag", gray_img)
#img_g = cv2.imread(r"C:\Users\USER\Downloads\images.jpg",0) # same1
#cv2.imshow("gray imag",img_g)

h,w,c = img.shape
rotat_matriex = cv2.getRotationMatrix2D((w//2,h//2),180 , 1)
rotated_img = cv2.warpAffine(img , rotat_matriex,(w,h))
cv2.imshow("rotated imag",rotated_img)












cv2.waitKey()

