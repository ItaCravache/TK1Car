
import numpy
import random
import string
import cv2
from PIL import Image
from PIL import ImageOps
numpy.seterr(all='ignore')


def sigmoid(x):
    return 1. / (1 + numpy.exp(-x))


def dsigmoid(x):
    return x * (1. - x)

def tanh(x):
    return numpy.tanh(x)

def dtanh(x):
    return 1. - x * x

def softmax(x):
    e = numpy.exp(x - numpy.max(x))  # prevent overflow
    if e.ndim == 1:
        return e / numpy.sum(e, axis=0)
    else:  
        return e / numpy.array([numpy.sum(e, axis=1)]).T  # ndim = 2


def ReLU(x):
    return x * (x > 0)

def dReLU(x):
    return 1. * (x > 0)


# # probability density for the Gaussian dist
# def gaussian(x, mean=0.0, scale=1.0):
#     s = 2 * numpy.power(scale, 2)
#     e = numpy.exp( - numpy.power((x - mean), 2) / s )

#     return e / numpy.square(numpy.pi * s)

# for CNN
def create_demo_data(N_each, channel, n_in, n_out, rng, p=0.9):
    if rng is None:
        rng = numpy.random.RandomState(1234)

    data = numpy.zeros( (N_each * n_out, channel, n_in, n_in) )
    label = numpy.zeros( (N_each * n_out, n_out) )

    K = n_in / n_out

    index = 0
    for k in xrange(n_out):  # for each class        
        for num in xrange(N_each):  # for each sub data
            for c in xrange(channel):
                for i in xrange(n_in):
                    for j in xrange(n_in):                

                        if i < (k+1) * K and i >= k * K:
                            # a = int(128 * rng.rand() + 128) * rng.binomial(size=1, n=1, p=p) / 256.0
                            a = 128.0 * rng.binomial(size=1, n=1, p=p) / 256.0

                        else:
                            a = 128.0 * rng.binomial(size=1, n=1, p=1-p) / 256.0


                        data[index][c][i][j] = a

            for i in xrange(n_out):
                if i == k:
                    label[index][i] = 1.0
                else:
                    label[index][i] = 0.0

            index += 1

    return data, label
def prepare_image_cv2(img,size, equalizeHist, channel):
    if channel == 1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,size)

    if equalizeHist :
        img = cv2.equalizeHist(img,size)
    np_img = numpy.array(img)
    img_final = numpy.reshape(np_img,(1,channel,size[0],size[1]))/numpy.float32(255)

    return img_final

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

def get_ID(filename, dic_lab):
    part = string.split(filename, '/')

    return dic_lab[part[-1][0]]

def create_dic(poss_lab):
    dic = {}

    for idx, lab in enumerate(poss_lab) :
        dic[lab] = idx
    return dic

def load_data(f,dic_lab,size,equalizeHist,channel):
    random.shuffle(f)
    targets = numpy.zeros((len(f), len(dic_lab)))
    labels=[]
    features=[]
    for im in f:
        features.append(prepare_image(im,size,equalizeHist,channel))
        labels.append(get_ID(im,dic_lab))
    #labels=numpy.array(labels)
    for count, target in enumerate(labels):
            targets[count][target]= 1  
    new_data = {}
    new_data['input'] = numpy.reshape(features, (len(f),channel,size[0],size[1]))
    new_data['output'] = targets
    
    return new_data

