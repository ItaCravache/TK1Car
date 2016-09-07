"""Detect speed limits from webcam feed"""
import re
import os
import sys
import cv2
import threading
import argparse
import numpy as np

#Path to the images to analyse
IMG_PATH="images/signalisation13.jpg"


def run():
    """Run TSR and ISA"""
    lastdetect = "00"
    downscale = 1
    possiblematch = "00"
    try:
        #Read the image
        frame=cv2.imread(IMG_PATH)
	i=0
        while i==0:
	    i+=1
            origframe = frame
            #Convert RGB image to gray
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            scaledsize = (frame.shape[1]/downscale, frame.shape[0]/downscale)
            scaledframe = cv2.resize(frame, scaledsize)

            # Detect signs in downscaled frame
            signs = CLASSIFIER.detectMultiScale(
                scaledframe,
                1.1,
                5,
                0,
                (10, 10),
                (200, 200))
            count = 1
            #For each sign detected
            for sign in signs:
                xpos, ypos, width, height = [ i*downscale for i in sign ]

                #Get the crop image with xpos, ypos, width and height of the sign
                crop_img = frame[ypos:ypos+height, xpos:xpos+width]
                sized = cv2.resize(crop_img, (128, 128))
                
                x = xpos+width/2
                y = ypos+height/2
                r = int((width+height)*1.05/4)

                blank_image = 255*np.ones(origframe.shape, np.uint8)
                
                #Save the signs on the frame in a file
                cv2.circle(blank_image, (x,y), r, (0, 0, 0), -1)
                img_circle = cv2.bitwise_or(origframe, blank_image)
                img_circle = img_circle[y-r:y+r,x-r:x+r]
                
                cv2.imwrite("signs" + str(count) + ".png",img_circle)
                # Draw a circle around the sign
                cv2.circle(origframe, (x,y), r, (0,255,0), thickness=2)
                count+=1
            
            cv2.imshow("preview", origframe)
            _ = cv2.waitKey(0)

    except (KeyboardInterrupt, Exception), exept:
        print exept
        return True


if __name__ == "__main__":

    #Load the classifier in order to detect signs
    CLASSIFIER = cv2.CascadeClassifier("lbpCascade.xml")
    run()
