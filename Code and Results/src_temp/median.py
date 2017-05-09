from cv2 import *
import cv2

def median(Input,Output)
	im = cv2.imread(Input)
	final = cv2.medianBlur(im, 3)
	cv2.imwrite(Output,final)
