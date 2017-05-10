
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
<img src="https://github.com//Charvik2020/Dictionary-based-filtering/raw/master/Report/Midterm%20Report/2.jpg" alt="https://github.com//Charvik2020/Dictionary-based-filtering/raw/master/Report/Midterm%20Report/2.jpg">



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
<img src="https://github.com//Charvik2020/Dictionary-based-filtering/raw/master/output/KSVD.jpg" alt="https://github.com//Charvik2020/Dictionary-based-filtering/raw/master/output/KSVD.jpg">

- on-line Dictionary Learning
<img src="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Report/FinalTerm%20Report/OnlineDictionaryLearning.jpg" alt="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Report/FinalTerm%20Report/OnlineDictionaryLearning.jpg">

<img src="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Report/FinalTerm%20Report/OnlineDictionaryLearningCopy.jpg" alt="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Report/FinalTerm%20Report/OnlineDictionaryLearningCopy.jpg">


- our own approach Dictionary Based Filtering
<img src="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Code%20and%20Results/Analysis/imageanalysis/output1.jpg" alt="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Code%20and%20Results/Analysis/imageanalysis/output1.jpg">

<img src="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Code%20and%20Results/Analysis/imageanalysis/output2.jpg" alt="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Code%20and%20Results/Analysis/imageanalysis/output2.jpg">

<img src="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Code%20and%20Results/Analysis/imageanalysis/Timeanalysis.jpg" alt="https://github.com/Charvik2020/Dictionary-based-filtering/raw/master/Code%20and%20Results/Analysis/imageanalysis/Timeanalysis.jpg">

<table class="tg">
  <tr>
    <th class="tg-yw4l">Dimension(m)<br></th>
    <th class="tg-yw4l">Thresold<br></th>
    <th class="tg-yw4l">Error</th>
  </tr>
  <tr>
    <td class="tg-yw4l">50 x 50<br></td>
    <td class="tg-yw4l">175</td>
    <td class="tg-yw4l">9.89 %<br></td>
  </tr>
  <tr>
    <td class="tg-yw4l">75 x 75<br></td>
    <td class="tg-yw4l">140</td>
    <td class="tg-yw4l">9.19%<br></td>
  </tr>
  <tr>
    <td class="tg-yw4l">100 x 100<br></td>
    <td class="tg-yw4l">90</td>
    <td class="tg-yw4l">3.5%</td>
  </tr>
</table>
