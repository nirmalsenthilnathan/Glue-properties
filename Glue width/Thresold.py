# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:47:47 2019

@author: Nirmal
"""


import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread("a9.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

ret,thresh = cv2.threshold(img, 150, 255, cv2.THRESH_TRUNC)
ret,thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 500, 255, cv2.THRESH_TOZERO)
ret,thresh4 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO_INV)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret,thresh5 = cv2.threshold(blur,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
ret,thresh6 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh7 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
ret,thresh8 = cv2.threshold(blur,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
ret,thresh9 = cv2.threshold(blur,0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)

plt.imshow(thresh, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh1, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh2, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh3, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh4, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh5, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh6, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh7, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh8, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh9, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.imwrite('Tozero_Inv_Threshold.jpg', thresh4)
cv2.imwrite('Binary_Threshold.jpg', thresh1)
cv2.imwrite('Otsu__Trunc_Threshold.jpg', thresh5)
