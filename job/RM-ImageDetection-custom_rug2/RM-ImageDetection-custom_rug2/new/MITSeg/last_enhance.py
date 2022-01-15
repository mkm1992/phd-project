# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:42:30 2019

@author: mkm1992
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import atan , degrees
################################

def detect_lines(img):
        """
        Detects lines using OpenCV LSD Detector
        """
        # Convert to grayscale if required
        if len(img.shape) == 3:
            img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img_copy = img

        # Create LSD detector with default parameters
        lsd = cv2.createLineSegmentDetector(0)

        # Detect lines in the image
        # Returns a NumPy array of type N x 1 x 4 of float32
        # such that the 4 numbers in the last dimension are (x1, y1, x2, y2)
        # These denote the start and end positions of a line
        lines1 = lsd.detect(img_copy)[0]

        # Remove singleton dimension
        lines = lines1[:, 0]

        # Filter out the lines whose length is lower than the threshold
        dx = lines[:, 2] - lines[:, 0]
        dy = lines[:, 3] - lines[:, 1]
        lengths = np.sqrt(dx*dx + dy*dy)
        mask = lengths >= 50
        lines = lines[mask]

        # Return the lines
        return lines
def isInRug(img, y1, x1):
    flag = 0
    for i in range(-10,10):
        for j in range(-10,10):
            if img[x1+i,y1+j,0]== 255 and img[x1+i,y1+j,1]== 9 and img[x1+i,y1+j,2]== 92:
                flag = 1
    return flag
def isInFloor(img, y1, x1):
    flag = 0
    for i in range(-10,10):
        for j in range(-10,10):
            if img[x1+i,y1+j,0]== 80 and img[x1+i,y1+j,1]== 50 and img[x1+i,y1+j,2]== 50:
                flag = 1
    return flag
def diff_equal(line1, line2):
    dxdy1 = (line1[0]-line1[2])/(line1[1]-line1[3])
    dxdy2 = (line2[0]-line2[2])/(line2[1]-line2[3])
    teta1 = degrees(atan(dxdy1))
    teta2 = degrees(atan(dxdy2))
    flag_equal = 0
    if abs(teta1-teta2)<30:
        flag_equal == 1
    return flag_equal
def cluster_line(lines, k):
    line_final=np.zeros([k,5])
    lines1=np.zeros([k,5])
    line_final[0,0:4] = lines[0,:]
    line_final[0,4] = 1
    j = 0
    for i in range(1,k):
        if diff_equal(lines[i],line_final[j,0:4]):
            lines[i,4]= j
            line_final[j]
            
            
            
            
    
    
        
#################################
img = cv2.imread('output/n1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
############################
img1 = cv2.imread('input/n1.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img4 = np.copy(img1)
plt.imshow(img1)
plt.show()
############################
imax, jmax, ch = img.shape
#############################
lines = detect_lines(img1)
status = np.ones(lines.shape[0], dtype=np.bool)
ind = np.where(status)[0]
line_rug = np.zeros([100, 4])
line_floor = np.zeros([100, 4])
k_rug = 0
k_floor = 0
for (x1, y1, x2, y2) in lines[ind]:
    if y1< imax - 10 and x1< jmax -10 and y2< imax - 10 and x2< jmax -10:
        if isInRug(img, int(x1),int(y1)) and isInRug(img, int(x2),int(y2)):
            cv2.line(img1, (int(x1), int(y1)), (int(x2), int(y2)),
                    (100, 150, 40), 2, cv2.LINE_AA)
            print(x1,y1, x2, y2)
            line_rug[k_rug,0]= x1
            line_rug[k_rug,1]= y1
            line_rug[k_rug,2]= x2
            line_rug[k_rug,3]= y2
            k_rug += 1
        elif isInFloor(img, int(x1),int(y1)) and isInFloor(img, int(x2),int(y2)):
            cv2.line(img1, (int(x1), int(y1)), (int(x2), int(y2)),
                    (90, 50, 160), 2, cv2.LINE_AA)
            print(x1,y1, x2, y2)
            line_floor[k_floor,0]= x1
            line_floor[k_floor,1]= y1
            line_floor[k_floor,2]= x2
            line_floor[k_floor,3]= y2
            k_floor += 1
plt.imshow(img1)
plt.show()


