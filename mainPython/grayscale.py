import cv2
import os

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"

image = cv2.imread(path)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def manualGrayScaleConverterG2G(img, constant):
    (row, col) = img.shape[0:2]
    for x in range(row):
        for y in range(col):
            img[x,y] = sum(img[x, y]) * constant #this constant better be 1/3
    return img

def manualGrayScaleConverterMe(img):
    (row, col) = img.shape[0:2]
    for  x in range(row):
        image [x] = image [x] * 0.333
    for  y in range(col):
        image [x] = image [x] * 0.333
    return img


cv2.imshow('BANRRRR', manualGrayScaleConverterMe(image))
cv2.waitKey(0)

'''cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', grayImage)
cv2.imshow('Grayscale Image Manual', manualGrayScaleConverter(image, 0.33))
cv2.waitKey(0)'''