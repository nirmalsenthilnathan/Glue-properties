# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:47:47 2019

@author: Nirmal
"""

"""
==============
Blob Detection
==============

Blobs are bright on dark or dark on bright regions in an image. In
this example, blobs are detected using 3 algorithms. The image used
in this case is the Hubble eXtreme Deep Field. Each bright dot in the
image is a star or a galaxy.
"""

# import libraries
import math
import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")
im1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(im1,(5,5),0)
ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
im=thresh
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
#params.minThreshold = 10
#params.maxThreshold = 200


# Filter by Area.
#params.filterByArea = True
#params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.50    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.1

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imwrite("Keypoints2.jpg", im_with_keypoints)
cv2.imwrite("Thresold.jpg", thresh)

"""
==============
Hough Circle Transform
==============

Blur the image and Hough circle transform to find keypoints for air bubbles
"""
# load blob detection results and input image
image = im_with_keypoints
img1 = cv2.imread('input.jpg')

img=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

# Blur the image and Hough circle transform to find keypoints for air bubbles
img = cv2.medianBlur(thresh,5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    a = i[2]**2 * math.pi
    print(a)
    if (a>5000) and (a<15000):
        print('Air bubble size is large')
        # draw the outer circle
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img1,(i[0],i[1]),2,(0,0,255),3)
    elif a>15000:
      continue  
    elif a<5000:
        # draw the outer circle
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img1,(i[0],i[1]),2,(0,0,255),3)
        
#print(circles)
cv2.imwrite('detected circles.jpg',img1)
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()