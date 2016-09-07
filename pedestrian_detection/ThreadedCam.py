from __future__ import print_function
import imutils
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse

import time
import cv2
from imutils.video import WebcamVideoStream
import imutils


# Load camera stream in threads
vs = WebcamVideoStream(src=0).start()

########## Start video stream
try:
    while True:
	F=450.0
	W=0.5
	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
	
	image = vs.read()
	image = imutils.resize(image, width=min(400, image.shape[1]))
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),   
		padding=(8, 8), scale=1.05)
		#(4,4) & (8,8) & 1.05
		# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x+w/4, y, x + 3*w/4, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
		print()
		cv2.putText(image, "D = "+str(F*W/(xB-xA)),
		(20, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		1.0, (0, 255, 0), 3)
	# show the output image
	cv2.imshow("After NMS", image)
	
	k = cv2.waitKey(10)
	
        if k == ord('q'):
            break
finally:
    print("finished, cleanup now")
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
	
    #F = (P x  D) / W
    #F = (248px x 24in) / 11in = 543.45

