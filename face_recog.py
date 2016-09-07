import pickle
import ConfigParser
import os
import cv2
import time
from CNN import CNN
from utils import *

# Method which search face in a frame
def processPicture(frame,faceCascade):
    # Convert image RGB to Gray and equalize the histogram
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Search face with the faceCascade
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Return faces
    return faces
    
# Method which load a CNN model
# param : cfg_file, configuration file which contains all the param of the CNN model
def loadCNN(cfg_file) :
	# Creation of a ConfigParser object in order to get the param
    cfg = ConfigParser.ConfigParser()
    # Reading the file
    cfg.read(cfg_file)

    # Get the params of the CNN model
    sec = 'CNN_Parameters'

    namefile = cfg.get(sec,'namefile')

    poss_lab = eval(cfg.get(sec,'poss_lab'),{},{})
    train = cfg.getboolean(sec,'train')

    epochs = cfg.getint(sec,'epochs')
    learning_rate = cfg.getfloat(sec,'learning_rate')
    
    img_resize = eval(cfg.get(sec,'img_resize'),{},{})
    equalizeHist = cfg.getboolean(sec,'equalizeHist')
    channel = cfg.getint(sec,'channel')
    
    n_kernels = eval(cfg.get(sec,'n_kernels'),{},{})
    kernel_sizes = eval(cfg.get(sec,'kernel_sizes'),{},{})
    pool_sizes = eval(cfg.get(sec,'pool_sizes'),{},{})
    n_hidden  = cfg.getint(sec,'n_hidden')

    # Initialize a CNN model before opening it
    classifier = CNN(1, [], n_hidden, 2, [1,1], channel, n_kernels, kernel_sizes, pool_sizes)

    with open(namefile, 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        classifier = mon_depickler.load()
    
    return classifier

#Method which predict the face in a frame, thanks to the CNN model
def predictFace(cfg_file,classifier,faceCascade,frame):
	# Creation of a ConfigParser object in order to get the param
	cfg = ConfigParser.ConfigParser()
    # Reading the file
	cfg.read(cfg_file)
	sec = 'CNN_Parameters'
	
	#Get the parameters of the CNN we need
	img_resize = eval(cfg.get(sec,'img_resize'),{},{})
	equalizeHist = cfg.getboolean(sec,'equalizeHist')
	channel = cfg.getint(sec,'channel')

	#Get faces of the frame
	faces = processPicture(frame,faceCascade)
        
    #Loop over faces
	for (x, y, w, h) in faces:
		img_faces = frame[y:y+h,x:x+w]
        
        #prepare image for the CNN prediction
		Y = prepare_image_cv2(img_faces,img_resize,equalizeHist,channel)
		Y = numpy.reshape(Y, (len(Y),channel,img_resize[0],img_resize[1])) 
		#Prediction of the CNN
		pred = classifier.predict(Y)
		if pred[0][0] > 0.5 :
			text="Nico"
		else:
			text="Max"
		# Draw a rectangle around faces and write the name of the predicted face
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(frame,text,(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
