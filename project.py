import cv2
import numpy

img1 = cv2.imread('./1.jpg')
img2 = cv2.imread('./2.jpg')
img3 = cv2.imread('./3.jpg')

canny1 = cv2.Canny(img1, 125, 175)
cv2.imshow("edge1", canny1)
canny2 = cv2.Canny(img2, 125, 175)
cv2.imshow("edge2", canny2)
canny3 = cv2.Canny(img3, 125, 175)
cv2.imshow("edge3", canny3)
cv2.waitKey()
