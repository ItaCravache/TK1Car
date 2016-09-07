import cv2

#Method which detect contours in a frame
def detectObjects(img):
	#Convert RGB image to gray, blur it and apply a threshold
	img_gray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
	img_filt = cv2.medianBlur(img_gray,21)
	img_th = cv2.adaptiveThreshold(img_filt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,3)
	
	#Find contours on this image
	contours, hierarchy = cv2.findContours(img_th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	
	#To not have the contour around the whole image
	contours = contours[1:len(contours)-1]

	return contours
