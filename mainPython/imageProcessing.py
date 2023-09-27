import numpy as np
import cv2

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"
outputPath = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\"


apple = cv2.imread(path)

def lighter(image, percent):
    '''assumes color is rgb between (0, 0, 0) and (255, 255, 255)'''
    color = np.array(image)
    white = np.array([255, 255, 255])
    vector = white-color
    return image + vector * percent

def threshold(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 1)
    
    return(thresh)

cv2.imwrite(outputPath+"threshold\\"+".png", threshold(apple))