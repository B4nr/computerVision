import cv2
import os
import numpy

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"

image = cv2.imread(path)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def manualGrayScaleConverterG2G(img, constant):
    (row, col) = img.shape[0:2]
    for x in range(row):
        for y in range(col):
            img[x,y] = sum(img[x, y]) * constant #this constant better be 1/3
    return img

b = 3
g = 0
r = 0

matrix  = [b, g, r]
def manualGrayScaleConverterMe(img, cons):
    (row, col) = img.shape[0:2]
    for x in range(row):
        #numpy.savetxt('r1.txt', img[x])
        img[x] = img [x] * cons
        #numpy.savetxt('r2.txt', img[x])
    return img

def generateFrame(leImg, m):
    #for x in range(0, 100, 1):
    leImg = manualGrayScaleConverterMe(leImg, [1, x/100, 1])
    cv2.imwrite(str(m)+".png", leImg)

for x in range(100, 0, -1):
    generateFrame(image, x)



generateFrame(image, 1)
'''for x in range(1, 2, 1):
    cv2.imshow('bozo', manualGrayScaleConverterMe(image, [1,0.3,1]))
    cv2.waitKey(0)
    print("done", x)'''


'''cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', grayImage)
cv2.imshow('Grayscale Image Manual', manualGrayScaleConverter(image, 0.33))
cv2.waitKey(0)'''