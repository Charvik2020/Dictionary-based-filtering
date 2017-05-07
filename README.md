
## Project Title
Dictionary Based Filtering

## Member Group - 8
- Maharsh Patel-1401109
- Charvik Patel-1401079
- Neel Puniwala-1401024
- Himanshu Budhia-1401039

## Mentor's And Teaching Assistant
- Dr. Mehul raval
- Vaibhav Joshi 


## Abstract
Digital image processing refers to the process of
digital images by means of digital computer. The main application
area in digital image processing is to enhance the pictorial data
for human interpretation. In image some of the unwanted information
is present that will be removed by several preprocessing
techniques. Filtering helps to enhance the image by removing
noise.Initially By creating Dictionary we will store two form of
matrix.now when We add new image in dictionary we don’t need
to pass image from filter instead we will just Dictionary Learn
form the Previous Dictionary and just map into.

## Introduction:
- Basically the idea of Dictionary based filtering is instead of doing classical convolution every time,we directly take de–noise image from the dictionary using searching algorithm and time after time Learning of dictionary is also done by the same algorithm. We are planning to do low pass or high pass filtering to de–noise the noisy image. Low pass filter is used to remove salt and paper noise while high pass filter is used to separate of edges.We use OpenCV libraries and Python libraries to implement the low pass filter and to create blocks of image.
- Initially we take some training and filter them by using classical convolution.Both filtered and non-filtered images are divided into blocks which are stored in a dictionary.In the dictionary the key is noisy part of the image and the value is filtered part of the image.


## Methodology
![Output](https://github.com/Charvik2020/Dictionary-based-filtering/blob/master/Report/Midterm%20Report/2.jpg)

## Algorithm
```python
First of all we have to take n x n training image.
Create m x m blocks.
Create dictionary using blocks.
Dictionary:
	Key - Noisy image
	value - filtered image
Search algorithm
if Nearest Possible Match then
	Noisy Patch Replaced with this Image
else
	Add to Dictionary
end
return Final Filtered Image
```


## Requirements
- Python 2.7+
- PIL
- skimage
- numpy
- OpenCV

## Output
- KSVD
![Output](https://github.com/Charvik2020/Dictionary-based-filtering/blob/master/output/KSVD.jpg)
- On-line Dictionary Learning
![Output](https://github.com/Charvik2020/Dictionary-based-filtering/blob/master/output/OnlineDictionaryLearning.jpg)



Note:Image are Not display on GIT Page 



