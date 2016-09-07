import time
import tk1car as car
import cv2

class Car:
	# attributs
	camera = None
	historique = []
	image = None
	trapeze = None

	# constants
	_FORWARD = "_FORWARD"
	_BACKWARD = "_BACKWARD"
	# _STOP = "_STOP"
	_TURN_R = "_TURN_RIGHT"
	_TURN_L = "_TURN_LEFT"
	_TURN_BACK_R_L = "_TURN_BACK_RIGHT_AND_LEFT"

	_TIMEForward = 1
	

	# METHODS
	#Initialize the Car object
	def __init__(self, trapeze):
		self.trapeze = trapeze

	def loadImage(self, image):
		self.image = image

	def getImage(self):
        	return self.image

	def loadCamera(self, camera):
		self.camera = camera

	#Add mouvement to the history
	def addToHistorique(self, mouvement):
		self.historique.append(mouvement)
	
	#Save the history of the movement in a txt file
	def saveHistorique(self, nameFile):
		fileH = open(nameFile, 'w')
		for i in range(len(self.historique)):
		    	fileH.write(str(i + 1) + "| ")
		    	fileH.write(self.historique[i])
		    	fileH.write("\n")
		fileH.close()

	#Method to choose the better direction for the car
	#param : contours, contains all the contour of an image 
	def decision(self, contours):
		# The 3 trapeze area
		t_back = self.trapeze[0]
		t_left = self.trapeze[1]
		t_right = self.trapeze[2]

		# If obstacle in the backward area
		if (t_back.isObstacle(contours)):
			return self._BACKWARD
		else :
			# If obstacle in the left and right area, we go back right and left
			if (t_left.isObstacle(contours) and t_right.isObstacle(contours)):
				return self._TURN_BACK_R_L
			else :
				# If obstacle in left area, turn left
				if (t_left.isObstacle(contours)):
					return self._TURN_L
				#If obstacle in the right area, turn right
				elif (t_right.isObstacle(contours)):
					return self._TURN_R
				# If no obstacle in the 3 trapeze area, go forward
				else :
					return self._FORWARD
				



	# Method which run the car with the decision taken by the car	
	def run(self,contours):
        # Analyse
		decision = self.decision(contours)

		# Decision and mouvement
		#For each decision taken, we add the decision in the history, we print the decision 
		# and we run the car with the decision

		if decision == self._FORWARD:
			self.addToHistorique(self._FORWARD)
			print self._FORWARD
			car.init_mouvement()
			car.forward(self._TIMEForward)
			car.close_mouvement()

		elif decision == self._BACKWARD:
			self.addToHistorique(self._BACKWARD)
			print self._BACKWARD
			car.init_mouvement()
			car.backward(self._TIMEForward)
			car.close_mouvement()

		elif decision == self._TURN_L:
			self.addToHistorique(self._TURN_L)
			print self._TURN_L
			car.init_mouvement()
			car.turn45(car.LEFT,self._TIMEForward)
			car.close_mouvement()

		elif decision == self._TURN_R:
			self.addToHistorique(self._TURN_R)
			print self._TURN_R
			car.init_mouvement()
			car.turn45(car.RIGHT,self._TIMEForward)
			car.close_mouvement()

		elif decision == self._TURN_BACK_R_L:
			self.addToHistorique(self._TURN_BACK_R_L)
			print self._TURN_BACK_R_L
			car.init_mouvement()
			car.turnBack45(car.RIGHT,self._TIMEForward)
			car.turnBack45(car.LEFT,self._TIMEForward)
			car.forward(self._TIMEForward)
			car.close_mouvement()

		else:
			print "NO DECISION"
	
	#Method to show the image of the cam, the contours and the 3 trapeze area
	def showCamera(self, image, contours, drawTrap, drawCont):
		if drawTrap:
	    		self.trapeze[0].drawTrapeze(image, (0,0,255))
			self.trapeze[1].drawTrapeze(image, (0,255,0))
			self.trapeze[2].drawTrapeze(image, (255,0,0))
		if drawCont:
	    		cv2.drawContours(image, contours, -1 , (0,255,255))

		cv2.imshow("Video feed", image)



