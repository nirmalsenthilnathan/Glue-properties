# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:47:47 2019

@author: Nirmal
"""

#import libraries
import cv2
import numpy as np
from skimage import img_as_float

#load input images
img1 = cv2.imread("Blend2.jpg")
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
res = img
img1 = img[:, 1000:1400]
img2 = img[:, 1600:1900]
img3 = img[:, 2100:2400]
img4 = img[:, 2700:3000]
Image = [img1, img2, img3, img4]
c = []

for i in range(len(Image)):
    img = Image[i]
    ret,thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
    y,x = list(thresh.shape)
    thresh[0:10] = 0
    thresh[y-10:y] = 0
    thresh[:,x-10:x] = 0
    thresh[:,0:10] = 0
    
    thresh_f = img_as_float(thresh)
    
    contours, h = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    #y,x = list(thresh_f.shape)
    #exm_pts = np.zeros((y,x, 3), np.uint8)
    #res = np.zeros((y,x, 3), np.uint8)
    contour_frame = np.zeros(thresh_f.shape, np.uint8)
    contour_copy  = np.zeros(thresh_f.shape, np.uint8)
    centers=[]
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if  area > 1000:
            print("Area: " + str(area))
            cnt_length = cv2.arcLength(cnt, True)
            epsilon = 0.0005 * cnt_length
            approx_cnt = cv2.approxPolyDP(cnt, epsilon, True)
            cv2.drawContours(contour_frame, [approx_cnt], -1, (255, 255, 255), 1)
            contour_copy = contour_frame
            cv2.fillPoly(contour_frame, pts =[approx_cnt], color=(255,255,255))
            cnt = np.squeeze(cnt)
    #        print(cnt)
            xmax = max(cnt, key=lambda x: x[0])
            xmin = min(cnt, key=lambda x: x[0])
            print("max: " + str(xmax))
            print("min: " + str(xmin))
            # Find center point of contours:
            M = cv2.moments(cnt)
            cX = int(M['m10'] /M['m00'])
            cY = int(M['m01'] /M['m00'])
            centers.append([cX,cY])
            print(centers)
        print(D)
    else:
        print("Glue distribution is not proper")
#print(c)
c[0][0] = c[0][0]+1000
c[1][0] = c[1][0]+1000
c[2][0] = c[2][0]+1600
c[3][0] = c[3][0]+1600
c[4][0] = c[4][0]+2100
c[5][0] = c[5][0]+2100
#cv2.line(res,tuple(centers[0]),tuple(centers[1]),(255,0,255),2)
#cv2.circle(res, tuple(centers[0]), 3, (0, 255, 0), 2)
#cv2.circle(res, tuple(centers[1]), 3, (0, 255, 0), 2)
for i in range(0, len(c), 2):
        cv2.line(res,tuple(c[i]),tuple(c[i+1]),(255,0,255),2)
        cv2.circle(res, tuple(c[i]), 3, (0, 255, 0), 2)
        cv2.circle(res, tuple(c[i+1]), 3, (0, 255, 0), 2)
        print(c[i],c[i+1])
        print(i)
cv2.imwrite('Thres.jpg', thresh)
cv2.imwrite('CONTOUR.jpg',contour_frame)
cv2.imwrite('RESULT.jpg',res)