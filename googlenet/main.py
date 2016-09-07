from __future__ import division

import sys
import cv
import cv2
import numpy as np
sys.path.append('/home/ubuntu/caffe/python/')
import caffe
import time

#Read the names of the possible classes (or labels) and return it
# By default, the file with the classes is "synset_words.txt"
def readClassNames(filename="synset_words.txt"):
	classNames=[]	
	with open(filename, "r") as ins:
    		for line in ins:
			classNames.append(line[10:-1])
		return classNames

def main():
	#Path to the model files
	modelTxt = "bvlc_googlenet.prototxt"
	modelBin = "bvlc_googlenet.caffemodel"
	#Path to the image to predict
	imageFile = "watch.png" #"space_shuttle.jpg"
	
	#We set the GPU mode (faster with the Jetson TK1)
	caffe.set_mode_gpu()

	#we create the clasifier
	net = caffe.Classifier(modelTxt, modelBin,
	       mean=np.load('./ilsvrc_2012_mean.npy').mean(1).mean(1),
               raw_scale=255,
               image_dims=(244, 244)) #channel_swap=(2,1,0) ?
	
	#Get the current time and the time at the end of the prediction
	#in order to have a idea of the prediction speed 
	start=time.time()
	#We load the image and resize it
	img=caffe.io.load_image(imageFile)
	img = cv2.resize(img, (244,244))
	
	#Predict on the image with the classifier created earlier
	prediction = net.predict([img])
	print(prediction[0][prediction[0].argmax()])
	classes=readClassNames()
	bestpreds=prediction[0].argsort()[-5:][::-1] # top-5 predictions
	#We print the TOP 5 predictions about the image
	print("--- TOP 5 PREDICTIONS ON "+imageFile+" ---")
	j=1
	for i in bestpreds:
		print str(j)+" - "+str(readClassNames()[i])
		j+=1
	#Current time, at the end of the prediction
	stop=time.time()
	#Print the time of prediction
	print("Execution time: "+str(stop-start)+" secs")

main()
