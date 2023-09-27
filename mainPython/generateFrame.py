import numpy as np
import cv2
import colorChange as cg

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"
outputPath = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\"

image = cv2.imread(path)

def generateFrame(ammount, entry):
    for x in range(ammount):
        cv2.imwrite(outputPath+"brighter\\"+str(x)+".png", cg.lighter(entry, x/ammount))

generateFrame(180, image)
