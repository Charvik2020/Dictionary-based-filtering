import sys
import glob,os
import re, math
import numpy as np
import random
import cv2


def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.
	
def sp_noise(image,prob):

#Add salt and pepper noise to image
#prob: Probability of the noise

	output = np.zeros(image.shape,np.uint8)
	thres = 1 - prob 
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			rdn = random.random()
			if rdn < prob:
				output[i][j] = 0
			elif rdn > thres:
				output[i][j] = 255
			else:
				output[i][j] = image[i][j]
	return output

full_file_paths = get_filepaths("original_Images")


count = 1

for f in full_file_paths:
	if (f.endswith(".tif") or f.endswith(".TIF")):
		
		image = cv2.imread(f,0) # Only for grayscale image
		noise_img = sp_noise(image,0.05)
		cv2.imwrite("noisy_Images\\"+str(count)+".tif", noise_img)
		count+=1
		
			

