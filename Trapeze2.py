from __future__ import division

import cv
import cv2
import math

import trouverPointIntersection


class Trapeze:
	# Attributes
	point_hg = [0, 1]
	point_hd = [1, 1]
	point_bg = [0, 0]
	point_bd = [1, 0]

   	# Constructor
    	def __init__(self, point_hg, point_hd, point_bg, point_bd):
        	self.point_hg = point_hg
        	self.point_hd = point_hd
        	self.point_bg = point_bg
        	self.point_bd = point_bd

	# Method
	# For a point (x,y), return the cooordinates min_x on the trapeze left straight
	# line for the coordinates y
	def minEqLeft(self,x, y):
		#if trapeze straight line is vertical
		if (self.point_bg[0] == self.point_hg[0]) :
	 		min_x = self.point_bg[0]
		# we calculate the slope of the trapeze straight line
		else :
	    		a = math.trunc((self.point_bg[1] - self.point_hg[1]) / (self.point_bg[0] - self.point_hg[0]))
	   		b = self.point_bg[1] - a * self.point_bg[0]
	    		min_x = math.trunc((y - b) / a)
	    	return min_x

	# For a point (x,y), return the cooordinates min_x on the trapeze right straight line for the coordinates y
	def minEqRight(self,x, y):
		#if trapeze straight line is vertical
		if (self.point_bd[0] == self.point_hd[0]) :
	    		min_x = self.point_bd[0]
		# we calculate the slope of the trapeze straight line
		else :
	   		a = math.trunc((self.point_bd[1] - self.point_hd[1]) / (self.point_bd[0] - self.point_hd[0]))
	    		b = self.point_bd[1] - a * self.point_bd[0]
	   		min_x = math.trunc((y - b) / a)
		return min_x

    	# return True if the point (x,y) is inside the trapeze
	def isPointIn(self, x, y):
		if y <= self.point_hg[1]:
			return False
		else:
			minx_g = self.minEqLeft(x,y)
			minx_d = self.minEqRight(x,y)

		    	if (x > minx_g and x < minx_d):
				return True
		    	else:
				return False

    	# return True if there is an intersection with the straight lines of the trapeze
	def isIntersection(self, line):
		left = [[self.point_hg[0], self.point_hg[1]], [self.point_bg[0], self.point_bg[1]]]
		right = [[self.point_hd[0], self.point_hd[1]], [self.point_bd[0], self.point_bd[1]]]

		inter_left = trouverPointIntersection.trouverIntersection([[line[0], line[1]], [line[2], line[3]]], left)
		inter_right = trouverPointIntersection.trouverIntersection([[line[0], line[1]], [line[2], line[3]]], right)
		
		return (inter_left or inter_right)
    
    	# return True if there is point or line crossing the trapeze
	def isObstacle(self,contours):
       		# no contour
		if contours == None:
			return False	

		for c in contours:
			i=0
           		# for each point in contours, we take two consecutives point
            		# and we create a line with this point
			while i < len(c)-1:
				pt = c[i]
				pt_plus1 = c[i+1]
				x1 = pt[0][0]
				y1 = pt[0][1]
				x2 = pt_plus1[0][0]
				y2 = pt_plus1[0][1]
			
				line = [x1,y1,x2,y2]
               			# check that point are or not in the Trapeze
                		if (self.isPointIn(x1, y1) or self.isPointIn(x2, y2)):
					print "Point in the trapeze : (", x1, ",", y1,") | (", x2,",",y2,")"
					return True
                		else:
		    			#check if there is any intersection with the straight line of trapeze
					if (self.isIntersection(line)):
						print "Cross Line : ", line
						return True
                		i+=1
		return False

	# draw the trapeze
	def drawTrapeze(self, image, color):
		pt1 = (self.point_hg[0], self.point_hg[1])
		pt2 = (self.point_hd[0], self.point_hd[1])
		pt3 = (self.point_bg[0], self.point_bg[1])
		pt4 = (self.point_bd[0], self.point_bd[1])

		cv2.line(image, pt1, pt3, color, 2)
		cv2.line(image, pt1, pt2, color, 2)
		cv2.line(image, pt2, pt4, color, 2)
