# import the necessary packages
import numpy as np
import imutils
import cv2
import pyocr
import pyocr.builders
from PIL import Image

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
lower = (0, 0, 0)
upper = (255, 255, 50)

frame = cv2.imread("signs1.png")
# keep looping

# resize the frame, blur it, and convert it to the HSV
# color space
frame = imutils.resize(frame, width=600)
#blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# construct a mask for the color "green", then perform
# a series of dilations and erosions to remove any small
# blobs left in the mask
mask = cv2.inRange(hsv, lower, upper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

tool = pyocr.get_available_tools()[0]
# Digits - Only Tesseract (not 'libtesseract' yet !)
img = Image.fromarray(mask)
#img.show()
digits = tool.image_to_string(
    img,
    builder=pyocr.tesseract.DigitBuilder()
)

#lab = int(digits)
print("Number = " + digits)

x = frame.shape[0]/2
y = frame.shape[1]/10
cv2.putText(frame,digits,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),3)

cv2.imshow("frame",frame)
cv2.imshow("mask",mask)
cv2.waitKey(0)