import glob
import cv2
import numpy as np

files = glob.glob("data/*.jpg")
file = files[2]

img = cv2.imread(file)
cv2.imshow("result", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("result", gray)
cv2.waitKey(0)

ret,bin = cv2.threshold(gray,245,255,cv2.THRESH_BINARY)
cv2.imshow("result", bin)
cv2.waitKey(0)

# closing
kernel = np.ones((3,3),  np.uint8)
closing = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)
cv2.imshow("result", closing)
cv2.waitKey(0)

# invert black/white
inv = cv2.bitwise_not(closing)

cv2.imshow("result", inv)
cv2.waitKey(0)