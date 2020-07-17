import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('imyourfather.png',0)    # Loat image
img2 = img.copy()                        # Make a true copy
template = cv.imread('template.png',0)   # Load template
w, h = template.shape[::-1]              # get Template width and height (58,71 pix)

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:            # For each method
    img = img2.copy()           # Copy the original image
    method = eval(meth)         # Load methods in list as Python code

    # Apply template Matching, res is the original array, but now are all shades of gray
    res = cv.matchTemplate(img,template,method)   #  Apply matching and get image result
    # get min and max values of an image; min loc, and max loc are location tuples
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        # Define top left matching square coordinates
        top_left = min_loc   # 327, 181
    else:
        top_left = max_loc   # 327, 181
    # Define bottom right coordinates
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # Draw rectangle
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    # Show subplots
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
