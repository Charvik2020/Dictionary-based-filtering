import os
for x in range(1, 375, 125):
       for y in range(1, 375, 125):
            os.system("gdal_translate -srcwin "+str(x)+" "+str(y)+" 125 125 C:\Users\Neel_puni\Downloads\koala\\Koala.tif C:\Users\Neel_puni\Downloads\koala\\"+str(x)+"_"+str(y)+".tif")
