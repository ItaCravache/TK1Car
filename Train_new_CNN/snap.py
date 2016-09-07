import cv2

# import webcam
from imutils.video import WebcamVideoStream
import imutils
import argparse

#Start the cam
vs = WebcamVideoStream(src=0).start()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#Path to the folder of the images to save
ap.add_argument("-p", "--path", required=True,
	help="path to the folder of the images")
#Global name of the saved image
ap.add_argument("-n", "--name", type=str, default="image",
	help="name of the images")
#Beginnig of the iteration
ap.add_argument("-i", "--iter", type=int, default=1,
	help="beginning of the iteration")

args = vars(ap.parse_args())

#Get the args 
path = args["path"]
name = args["name"]
ite = args["iter"]

print "Folder path = " , path
print "Image name = ", name
print "Iteration = ", ite

while True:
	#Resize the frame frome the cam
	frame = imutils.resize(vs.read(), width=1000)

	#Show the frame
	cv2.imshow('Video', frame)
	key=cv2.waitKey(10)

	#If tap on "q", we quit the program and close the cam
	if key & 0xFF == ord('q') :
		break

	#If tap on "p", we save the current frame as an jpg image, in the folder
	if key & 0xFF == ord('p') :
		cv2.imwrite(path + name + str(ite)+".jpg",frame)
		print("Image " + name + str(ite) + ".jpg saved !")
		ite+=1
