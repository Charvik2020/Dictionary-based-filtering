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
import time

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

def median(Input,Output):
	im = cv2.imread(Input)
	final = cv2.medianBlur(im, 3)
	cv2.imwrite(Output,final)
start_time = time.time()
full_file_paths = get_filepaths("noisy_Images")
i = 1
data_file = open("direct.csv","w")
for f in full_file_paths:
	median(f,"C:\\Users\\mahar\\Desktop\\DBF\\direct_filtered_Images\\"+ntpath.basename(f))
	data_file.write(str(i)+","+str(time.time() - start_time)+"\n")
	i+=1