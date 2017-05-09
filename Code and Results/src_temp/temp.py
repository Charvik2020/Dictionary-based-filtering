import sys
import glob,os
import re, math
import numpy as np
import random
import cv2
from PIL import Image
import Image
import ntpath
import math
import scipy
from shutil import copyfile

def calculateDistance(i1, i2):
	im1 = cv2.imread(i1)
	im2 = cv2.imread(i2)
	width,height =im1.shape[:2]
	dist = np.sum((im1-im2)**2)/(width*height)
	print dist,"\n"
	
calculateDistance("t1.tif","t2.tif")	
