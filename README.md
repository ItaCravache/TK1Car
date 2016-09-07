# Project TK1 Car - Summer 2016 - Maxime DROY - Nicolas VENDITTI - MAM4

#CAR DECISIONS
We had several features to implement in order to improve the previous learning car projects

- First off we changed their code in order for it to work on the Jetson TK1.
The fews differences were about the camera capture and activating the directions of the car.

- There are a few GPIO pins on the Jetson, each one controls a direction and is linked to a wire of the remote control.

- You can activate a GPIO by using http://elinux.org/Jetson/Tutorials/GPIO , but the easier python command are in tk1car.py

- If you interupt a program in the middle of it, the GPIO will stay activated and you won't be able to do anything, when this happens just do "sudo su" in terminal and execute disableGPIO.sh in this folder to close all the GPIOs, then "exit" to exit the superuser mode.

- To the previous project we changed the way the car moves by improving the decisions, the car no longer tries to find vanishing points, but moves forward and tries to avoid obstacles.

#FACE RECOGNITION
We added a face recognition CNN in the main program, it is only trained with our faces for now, so everyone is recognized as Nico or Max.

If you want to add new faces you need to do the following:
- Go in config/faceRecog.cfg
- There is the definition of the possible labels ('m' and 'n' corresponding to Max and Nico), you can add labels for training new faces, and set the train boolean on true.
- For each news face you need to add at least 100 pictures for training in Train_new_CNN/train , the name of the pictures need to be starting with the same letter that you added in the possible labels.
You can use Train_new_CNN/snap.py to take snapshots with you webcam, do it in several rooms with different luminosity like we did.
You can also add test images in the test folder.
- Then do "sudo python Train_new_CNN/CNN.py config/faceRecog.cfg" (you should do it with a lot of calculation power like NEF by using GPUs, it's still really long to train).
Once it's done you will have a model file named "faceRecog", you can test it by changing the boolean to false in the cfg file and run CNN.py again.
- When you have a good new model you can replace the one in the config file of this folder.
- Once a recognition is done, you will have an array prediction like [ 0.1 , 0.3 , 0.6 ], each of the positions of the array corresponds to a face and the one that has the highest probability is the actual predicted face. Check faceRecog.py to understand how the face name is displayed.


#TRAFFIC SIGNS RECOGNITION
We wanted to be able to recognize a traffic sign and analyze it with deep learning algorithms but we were lacking time, and our CNN for recognition wasn't working in the end.
We still have the detection of circle shaped signs though, the code is in the "traffic_signs" folder but isn't implemented in the main script.

#PEDESTRIAN DETECTION
We also wanted to detect a pedestrian and calculate his distance to the camera, so we used an openCV detection at first (code in "pedestrian_detect" folder, also not implemented in main) but it's a clutchy detection which isn't working really well with the low angle of our camera.
Using a deep learning algorithm would also be key here. 

#OBJECT RECOGNITION
Finally we planned on using googlenet training model for imagenet, we were able to implement it on python but the main program is already taking too much time by itself, the code is in the "googlenet" folder.

#STARTING THE MAIN PROGRAM
Connect to the car by SSH (you need to be on the same network of course, a phone is good, don't use the university wifi):
ssh ubuntu@tegra-ubuntu
(password: ubuntu)
To start the main program: sudo python start.py
When started it needs to be interupted with Ctrl-C .
Each run is saved in a folder into the image folder (images taken and decision historic)

#HOW TO CONTINUE OUR PROJECT
- Implement traffic signs recog with deep learning
- Use a rotative camera instead of the classic camera to improve decisions
- Improve pedestrian detection to make it usable

## Readme of the previous project

******************
**** README ******
******************

Date : From 6 to 24 January 2014.

Project : make an autonomous car with a raspberry and picar. Make establishment of hardware and software. Use image processing with a pi-camera.

Group :	Students of 4th years at Polytech Nice Sophia in department of Modeling and Applied Mathematics
	 |
	 | CONTAL Rebecca		MESTRE Coralie		RICHTER Cannelle	SAMOUN Lirone

Sumary :
	A] Hardware you need
	B] Software and files to run
	C] How to start the car
	D] What you have to know

	JUST ENJOY.



A] Hardware you need
====================

- rasberry
- pi-camera connected to the raspberry
- breadboard connecting raspberry to joystick of the car
- 64G SD Card on the raspberry
- wifi USB connected on the raspberry
- external battery on the car
- servo-motor assembled with camera and plug on the raspberry
- make the car more heavy (the plug for charging the car for exemple)

B] Software and files to run
=============================

The OS Rasbian is installed on both black and red 64G cards.
Python, OpenCV and all tools to work are already installed.

The module to control the servo-motor is ONLY installed in the black card (image OS package given by OpenElectron).

You have just to copy-paste and extract the good zip on the good card (on the folder /home/pi/Desktop/ for example.
- picamera-1.0_blackcard
- picamera-1.0_redcard

The folders
-------------
- picamera : a module to control the rasberry' camera
- pi-pan : a module to control the servo-motor
- snapshot : some examples of shop taken by camera while running

The files
-----------
- start.py to start the program to run the car
- ServerConnection.py to copy on the computer which will receive the video stream from the car
- ClientConnection.py : to transfer the video stream
- compareHisto.py : a method to compare two image by their histograms (not use in your project)
- pan_try.py : some method to control the servo-motor (not use)
- picar.py : some method to command how the car is moving
- pointFuite.py : some method to find the vanishing point
- Trapeze.py : class of Trapeze to define it and methods to find an obstacle into the Trapeze
- trouverPointIntersection.py : method to find the intersection point of lines
- Vector.py : class Vector.py used to find distance between two points...
- Voiture.py : base class that study the image, calculate the best solution, give a result and move the car. the class can also access to the camera to take another picture

- historique.txt : we record the path follow by the car while running

NOTE : read the file "Recapitulatif des éléments effectués.doc" to have all the details concerning installation.


C] How to start the car
===========================

1. Make sure that all hardware and sofware is correctly installed on the car

2. Connect your computer (and another computer or another terminal.. ? if you want the video stream) at same network (if possible without password) that the raspberry.
Unice network doesn't work correctly.
You can use your phone as a modem to have a simply good connection.

3. Copy the file : ServerConnection.py on the computer which will receive video stream

4. In the file : ClientConnection.py change "your adress ip" by wich is matched with video streamer computer.

5. a) IF YOU HAVE THE IP OF THE RASBERRY (192.168.43.29 normaly or check on your phone if we use like a modem):
	You can access to the terminal of raspberry with SSH connection :
		ssh pi@"ip_raspberry"
	and enter the password : raspberry

	b) IF YOU DON'T
	You have to connect the raspberry on a screen and a keyboard (HDMI&USB) and start the raspberry by connecting the battery.
	LOGIN : pi
	PASSWORD : raspberry
	To start the UI of the Rasbian, the command is : startx
	Then, open the WIFI interface, scan, and add your network. The ip of the raspberry is showing on the screen. Check with a "ifconfig" on the terminal and a "ping".
	Then connect you with ssh.

6. Execute the script ServerConnection.py on your video streamer computer.

7. Execute the script start.py by the computer using SSH.

Now the car is starting !!!!!

!!!!!!!!! WARNING : !!!!!
To stop the program, stop by Ctrl-C on the SSH computer AND ONLY WHEN THE CAR HAS STOPED TO MOVE.
!!!!!!!!!!


D] What you have to know
============================

1. The car takes a picture, analyses, moves, THEN take another picture...
2. The connection for sharing video stream is during ongly 5 min (300sec) you can change that in the class ClientConnection (duration)
3. The car moves forward and brakes then to stop directly the car, otherwise the camera takes blur pictures cause by speed.
The car need to be more heavy to do not skip, so add some materials.
4. When STARTING the script, we save all pictures taken by the camera in the folder : /home/pi/Desktop/picamera-1.0/
AND save an historique of car movements.
You can change that in the script start.py, removing "cv2.imwrite(image_name,image)"
5. DON'T TOUCH or CHANGE the position of the servo-motor because it is in the neutral position. If it is stop straight ahead before starting or after stopping the car, it will replace automatically when starting the script.
6. The camera placed on the servo-motor is upside down, so we flipped the image before analyse it.




---
THANKS to Mr.Precioso
THANKS to the group
It was a great job ! :)
---
