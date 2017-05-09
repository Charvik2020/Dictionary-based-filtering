import numpy as np
import Image
import scipy
import cv2
import math

def calculateDistance(i1, i2):
	width,height =i1.shape[:2]
	return np.sum((i1-i2)**2)*100/(width*height)

i1 = cv2.imread("direct.tif")
i2 = cv2.imread("100.tif")
 
print calculateDistance(i1,i2)

