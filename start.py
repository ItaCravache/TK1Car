import time

import cv2
from CNN import CNN
from utils import *
#Import for camera
from imutils.video import WebcamVideoStream
import imutils

import os

#Tools for detection (obsatcle, faces,...)
import Trapeze2 as Trap
import testDetection as detect
import face_recog

from Car import Car
import tk1car

print("Initialisation...")
time.sleep(5)

w=800
vs = WebcamVideoStream(src=0).start()
frame = imutils.resize(vs.read(), width=w)

########### CONFIG FACE RECOG #########
cascPath = "config/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
cfg_file = "config/faceRecog.cfg"

########### TRAPEZE ###########
h_video = frame.shape[0]
w_video = frame.shape[1]

# Trapeze for the backward area
point_hg1 = [w_video/10, 3*h_video/4]
point_hd1 = [9*w_video/10, 3*h_video/4]
point_bg1 = [0, h_video]
point_bd1 = [w_video, h_video]

t_back = Trap.Trapeze(point_hg1, point_hd1, point_bg1, point_bd1)

# Trapeze for the TURN_RIGHT area
point_hg2 = [2*w_video/10, h_video/2]
point_hd2= [w_video/2,h_video/2]
point_bg2 = point_hg1
point_bd2 = [w_video/2,3*h_video/4]

t_right = Trap.Trapeze(point_hg2, point_hd2, point_bg2, point_bd2)

# Trapeze for the TURN_LEFT area
point_hg3 = point_hd2
point_hd3= [8*w_video/10, h_video/2]
point_bg3 = point_bd2
point_bd3 = point_hd1

t_left = Trap.Trapeze(point_hg3, point_hd3, point_bg3, point_bd3)

trap = [t_back,t_left,t_right]

#Initialisation of the car
car = Car(trap)

#Loading of the classifier (for face recog)
classifier = CNN(1,[], 20, 2, [1,1], 1, [10,20],[[3,3],[2,2]], [[2,2],[2,2]])
classifier = face_recog.loadCNN(cfg_file)
########### MAIN ###########

currentTime = time.strftime("%dd-%mm-%Yy-%Hh-%Mm-%Ss")
print("Execution " + currentTime)

#Folder to record images (and history)
imagesPath = "images/" + currentTime
if not os.path.exists(imagesPath):
	os.makedirs(imagesPath)

try:
	count=1
	# main loop
	while True:
		frame = imutils.resize(vs.read(), width=w)
		#Detection of objects
		cont = detect.detectObjects(frame)
	
		print("Iteration " + str(count))
		# load the frame in the car
		car.loadImage(frame)
		#face detection and recognition 
		face_recog.predictFace(cfg_file,classifier,faceCascade,frame)

		#To show the frame
		#car.showCamera(frame,cont,True,True)
		# we run the car with the data
		car.run(cont)
		
		#we record every picture
		image_name = imagesPath + "/image_"+str(count)+".jpg"
		cv2.imwrite(image_name,frame)
		
		count+=1

		# waitkey to quit
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

except KeyboardInterrupt:
	print "History record !"
	tk1car.close_mouvement()
	#History record
	car.saveHistorique(str(imagesPath)+"/history.txt")
	cv2.destroyAllWindows()


