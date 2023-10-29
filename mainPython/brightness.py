import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\input\\teste.png"
outputPath = "C:\\Users\\Rodrigo\\Documents\\GitHub\\computerVision\\images\\output\\"

image = cv2.imread(path)
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

threshold_value = 100

_, segmentedImage = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

'''cv2.imshow('Imagem Segmentada', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

plt.imshow(segmentedImage)

plt.show()