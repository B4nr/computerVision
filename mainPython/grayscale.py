import cv2
import os

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"

image = cv2.imread(path)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Normal Image', image)
cv2.imshow('Grayscale Image', grayImage)
cv2.waitKey(0)