
import numpy
import random
import string
import cv2
from PIL import Image
from PIL import ImageOps
numpy.seterr(all='ignore')

#def of the sigmoid
def sigmoid(x):
    return 1. / (1 + numpy.exp(-x))

#def of the derivative sigmoid
def dsigmoid(x):
    return x * (1. - x)

#def of the hyperbolic tan
def tanh(x):
    return numpy.tanh(x)

#def of the derivative hyperbolic tan
def dtanh(x):
    return 1. - x * x

#def of the softmax
def softmax(x):
    e = numpy.exp(x - numpy.max(x))  # prevent overflow
    if e.ndim == 1:
        return e / numpy.sum(e, axis=0)
    else:  
        return e / numpy.array([numpy.sum(e, axis=1)]).T  # ndim = 2


#def of the rectified linear unit
def ReLU(x):
    return x * (x > 0)

#def of the derivative rectified linear unit
def dReLU(x):
    return 1. * (x > 0)

#prepare image for the CNN train and prediction by using openCV
def prepare_image_cv2(img,size, equalizeHist, channel):
    if channel == 1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,size)

    if equalizeHist :
        img = cv2.equalizeHist(img,size)
    np_img = numpy.array(img)
    img_final = numpy.reshape(np_img,(1,channel,size[0],size[1]))/numpy.float32(255)

    return img_final

#prepare image for the CNN train and prediction by using PIL
def prepare_image(filename,size,equalizeHist,channel):    
    #if (type(filename) == 'str'):   
    img = Image.open(filename)
        
    if channel == 1 :
        img = img.convert("L")

    img = img.resize(size)

    if equalizeHist :
        img = ImageOps.equalize(img) 

    np_img = numpy.array(img.getdata())
    img_final = numpy.reshape(np_img,(1,channel,size[0],size[1]))/numpy.float32(255)

    return img_final

#get the id of a label
def get_ID(filename, dic_lab):
    part = string.split(filename, '/')

    return dic_lab[part[-1][0]]

#Create a dictionnary with all the possible label for the CNN
def create_dic(poss_lab):
    dic = {}

    for idx, lab in enumerate(poss_lab) :
        dic[lab] = idx
    return dic

#Load the data from a folder f
def load_data(f,dic_lab,size,equalizeHist,channel):
	#Randomize the examples of the data
    random.shuffle(f)
    #Init the targets and features of the data
    targets = numpy.zeros((len(f), len(dic_lab)))
    labels=[]
    features=[]
    
    #For each examples im in the folder f
    for im in f:
    	#Append the image in the feature after preparing the image in the right shape 
        features.append(prepare_image(im,size,equalizeHist,channel))
        #Append the labels by getting the ID of it
        labels.append(get_ID(im,dic_lab))
    #for each labels, we define the targets    
    for count, target in enumerate(labels):
            targets[count][target]= 1  
    
    new_data = {}
    #Features
    new_data['input'] = numpy.reshape(features, (len(f),channel,size[0],size[1]))
    #Output or targets
    new_data['output'] = targets
    
    return new_data

