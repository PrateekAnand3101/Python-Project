# Paint the image a certain colour
# import cv2 as cv
# import numpy as np
# blank = np.zeros((500,500,3), dtype = 'uint8')
# cv.imshow('blank', blank)
# blank[:] = 0,255, 0 
# cv.imshow('Green',blank)
# cv.waitKey(0)

# Draw a Rectangle


import cv2 as cv
from matplotlib.pyplot import gray
import numpy as np
# blank = np.zeros((500,500,3), dtype = 'uint8')
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2)
# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

# Converting an image to grayscale
img = cv.imread('c:\\Users\\PRATEEK ANAND\\Pictures\\Saved Pictures\\POSTER.png')
cv.imshow('large',img)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur an image
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur) 

# Create and Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)