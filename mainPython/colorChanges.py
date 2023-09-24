import cv2
import os
import numpy

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\macaVermelha.jpg"
outputPath = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\"


image = cv2.imread(path)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

width = 4
height = 2
testImage = numpy.zeros((height,width,3), numpy.uint8)
testImage[:,0:width//2] = (255,0,0)      # (B, G, R)
testImage[:,width//2:width] = (0,255,0)

def manualGrayScaleConverterG2G(img, constant):
    (row, col) = img.shape[0:2]
    for x in range(row):
        for y in range(col):
            img[x,y] = sum(img[x, y]) * constant #this constant better be 1/3
    return img

b = 0.5
g = 1
r = 1

matrix  = [b, g, r]
def manualGrayScaleConverterMe(img, cons):
    (row, col) = img.shape[0:2]
    for x in range(row):
        for y in range(col):
            img[x, y] = img [x, y] * cons
            print(img[x, y])
            print(str(x)+str(y))
    return img

def generateFrame(leImg):
    #for x in range(0, 100, 1):
    leImg = manualGrayScaleConverterMe(leImg, [1, 1, 1])
    return leImg

imageFade = manualGrayScaleConverterMe(testImage, matrix)
cv2.imwrite(outputPath+str(0)+".png", imageFade)

imageBanr = manualGrayScaleConverterMe(image, matrix)
cv2.imwrite(outputPath+str(1)+".png", imageBanr)

'''for x in range(1, 2, 1):
    cv2.imshow('bozo', manualGrayScaleConverterMe(image, [1,0.3,1]))
    cv2.waitKey(0)
    print("done", x)'''


'''cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', grayImage)
cv2.imshow('Grayscale Image Manual', manualGrayScaleConverter(image, 0.33))
cv2.waitKey(0)'''