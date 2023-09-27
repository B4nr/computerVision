import cv2
import numpy as np
import glob
import re

img_array = []
files = sorted(glob.glob('C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\brighter\\*.png'))
files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
outputPath = 'C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\videos\\'

for filename in files:
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()