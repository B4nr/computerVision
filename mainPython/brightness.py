import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\\tarefaComprimidos\\cart_012.jpg"
outputPath = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\"

onlyFans = cv2.imread(path)
image = cv2.imread(path)

threshold_value = 40
_, segmentedImage = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

'''cv2.imshow('Imagem Segmentada', segmentedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

total = [0, 0, 0]
inverseTotal = ~segmentedImage

(row, col) = segmentedImage.shape[0:2]
for x in range(row):
    for y in range(col):
        total = total + inverseTotal[x,y]

moreTotal = 0
for x in total:
    moreTotal = moreTotal+x

trueValue = moreTotal/407581.071429

#print(trueValue)

#plt.imshow(segmentedImage)
plt.text(1, 35, str("Quantidade de Remedios: "+str(trueValue)))
plt.imshow(onlyFans)
plt.show()