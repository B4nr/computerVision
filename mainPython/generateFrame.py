import numpy as np
import cv2
import colorChange as cg

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"
outputPath = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\"

image = cv2.imread(path)

def generateFrame(ammount, function):
    for x in range(ammount):