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

main_thresh = 90

def merge(Input):
	file = open("C:\\Users\\mahar\\Desktop\\DBF\\fimage_temp\\dimension.txt","r")
	n1 = int(file.readline().strip())
	n2 = int(file.readline().strip())
	imgWidth = int(file.readline().strip())
	imgHeight = int(file.readline().strip())
	width = int(file.readline().strip())
	height = int(file.readline().strip())

	im1 = Image.new('L', (n2*width,n1*height))

	for i in xrange(0,n1*height,height):
		for j in xrange(0,n2*width,width):
		
			im = Image.open("C:\\Users\\mahar\\Desktop\\DBF\\fimage_temp\\"+str(i/height+1)+"_"+str(j/width+1)+".tif")
		
			im1.paste(im,(j,i))

	area = (0, 0,imgWidth, imgHeight)
	im1 = im1.crop(area)
	
	im1.save("C:\\Users\\mahar\\Desktop\\DBF\\filtered_Images\\"+ntpath.basename(Input))

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.
	




def crop(input, height, width, k, page):

	im = Image.open(input)

	imgwidth, imgheight = im.size
	a1=0
	b1=0
	file  = open("C:\\Users\\mahar\\Desktop\\DBF\\fimage_temp\\dimension.txt","w")
	for i in range(0,imgheight,height):
		a1 = a1+1
		b1 = 0
		for j in range(0,imgwidth,width):
			b1 =b1+1
			box = (j, i, j+width, i+height)

			a = im.crop(box)

		   

			#o = a.crop(area)

			a.save("C:\\Users\\mahar\\Desktop\\DBF\\image_temp\\"+str(a1)+"_"+str(b1)+".tif")
			
			

			

	file.write(str(a1)+"\n"+str(b1)+"\n"+str(imgwidth)+"\n"+str(imgheight)+"\n"+str(width)+"\n"+str(height))



def calculateDistance(i1, i2):
	im1 = cv2.imread(i1)
	im2 = cv2.imread(i2)
	width,height =im1.shape[:2]
	dist = np.sum((im1-im2)**2)/	(width*height)
	print dist,"\n"
	return dist
	
def median(Input,Output):
	im = cv2.imread(Input)
	final = cv2.medianBlur(im, 3)
	cv2.imwrite(Output,final)
	
def dict_add(Input):
	file = open("Dictionary\\sequence.txt","r")
	n = int(file.readline().strip())
	#n = int(n)
	file.close()
	copyfile(Input,"Dictionary\\Original\\"+str(n)+".tif")
	median("Dictionary\\Original\\"+str(n)+".tif","Dictionary\\Filtered\\"+str(n)+".tif")
	#copyfile("Dictionary\\Filtered\\"+str(n)+".tif","Dictionary\\fimage_temp\\"+ntpath.basename(Input))
	im = Image.open("Dictionary\\Filtered\\"+str(n)+".tif")
	im1 = im
	im1.save("C:\\Users\\mahar\\Desktop\\DBF\\fimage_temp\\"+ntpath.basename(Input))
	n+=1
	file = open("Dictionary\\sequence.txt","w")
	file.write(str(n))
	file.close()
	
	

def dict_search(Input):
	f1 = open("Dictionary\\sequence.txt","r")
	temp_thresh = 1
	n = int(f1.readline().strip())
	f1.close()
	file = ""
	if n == 0:
		dict_add(Input)
	else:
		temp_thresh = 256*256
		full_file_paths = get_filepaths("Dictionary\\Original")
		for f in full_file_paths:
			if (f.endswith(".tif") or f.endswith(".TIF")):
				temp_dist = calculateDistance(Input,f)
				if(temp_dist<temp_thresh):
					temp_thresh = temp_dist
					file = f
			

		if(temp_thresh<main_thresh):
			f1 = open("Dictionary\\sequence.txt","r")
			n = int(f1.readline().strip())
			f1.close()
			im_tem = Image.open("Dictionary\\Filtered\\"+ntpath.basename(file))
			im_tem.save("fimage_temp\\"+ntpath.basename(Input))
		else:
			dict_add(Input)
			


count = 1
full_file_paths = get_filepaths("noisy_Images")
file = open("Dictionary\\sequence.txt","w")
file.write(str(0))
file.close()
start_time = time.time()
data_file = open("indirect100.csv","w")
i = 1
for f in full_file_paths:
	if (f.endswith(".tif") or f.endswith(".TIF")):
		crop(f,100,100,1,1)
		full_file_paths_temp = get_filepaths("image_temp")
		for f1 in full_file_paths_temp:
			if (f1.endswith(".tif") or f1.endswith(".TIF")):
				dict_search(f1)
		merge(f)
	data_file.write(str(i)+","+str(time.time() - start_time)+"\n")
	i+=1
		