from PIL import Image

import Image

import os



def crop(Path, input, height, width, k, page):

    im = Image.open(input)

    imgwidth, imgheight = im.size

    for i in range(0,imgheight,height):

        for j in range(0,imgwidth,width):

            box = (j, i, j+width, i+height)

            a = im.crop(box)

           

            #o = a.crop(area)

            a.save("IMG-%s_lowpass.png" % k)

            

            k +=1







crop(r"C:\Users\mahar\Desktop\dspp","test_lowpass.png",50,50,1,1)
