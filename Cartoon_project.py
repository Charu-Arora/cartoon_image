import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("/Users/charuarora/Desktop/Projects/Orginal_image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
color=cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)
plt.imshow(cartoon)
cv2.imshow("Image",img)
cv2.imshow("Edges",edges)
cv2.imshow("CArtoon",cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()