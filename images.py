import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load a color image
img = cv.imread('imyourfather.png')
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
# Load a color image in grayscale
img = cv.imread('imyourfather.png',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
# Load a  BIG image
img = cv.imread('imyourfather.jpg')
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
# Exit or save and exit
img = cv.imread('imyourfather.png')
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit or any other key!
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' or 'S' key to save and exit
    cv.imwrite('gray.png',img)
    cv.destroyAllWindows()




