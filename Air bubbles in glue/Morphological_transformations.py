# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:37:37 2019

@author: Nirmal
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("a9.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
dilation1 = cv2.dilate(tophat,kernel,iterations = 1)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
dilation2 = cv2.dilate(blackhat,kernel,iterations = 1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
dilation3 = cv2.morphologyEx(gradient, cv2.MORPH_GRADIENT, kernel)
ero_grad = cv2.erode(gradient,kernel,iterations = 1)

plt.imshow(dilation),plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(closing),plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(tophat),plt.title('tophat')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(dilation1),plt.title('dilation1')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(blackhat),plt.title('blackhat')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(dilation2),plt.title('dilation2')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(gradient),plt.title('gradient')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(dilation3),plt.title('dilation2')
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(ero_grad),plt.title('gradient_erosion')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('erosion.jpg', erosion)
cv2.imwrite('gradient.jpg', gradient)
cv2.imwrite('dilation.jpg', dilation)
cv2.imwrite('opening.jpg', opening)