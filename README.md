# Project TK1 Car - Summer 2016 - Maxime DROY - Nicolas VENDITTI - MAM4

# CAR DECISIONS
We had several features to implement in order to improve the previous learning car projects

- First off we changed their code in order for it to work on the Jetson TK1.
The fews differences were about the camera capture and activating the directions of the car.

- There are a few GPIO pins on the Jetson, each one controls a direction and is linked to a wire of the remote control.

- You can activate a GPIO by using http://elinux.org/Jetson/Tutorials/GPIO , but the easier python command are in tk1car.py

- If you interupt a program in the middle of it, the GPIO will stay activated and you won't be able to do anything, when this happens just do "sudo su" in terminal and execute disableGPIO.sh in this folder to close all the GPIOs, then "exit" to exit the superuser mode.

- To the previous project we changed the way the car moves by improving the decisions, the car no longer tries to find vanishing points, but moves forward and tries to avoid obstacles.

# FACE RECOGNITION
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


# TRAFFIC SIGNS RECOGNITION
We wanted to be able to recognize a traffic sign and analyze it with deep learning algorithms but we were lacking time, and our CNN for recognition wasn't working in the end.
We still have the detection of circle shaped signs though, the code is in the "traffic_signs" folder but isn't implemented in the main script.

# PEDESTRIAN DETECTION
We also wanted to detect a pedestrian and calculate his distance to the camera, so we used an openCV detection at first (code in "pedestrian_detect" folder, also not implemented in main) but it's a clutchy detection which isn't working really well with the low angle of our camera.
Using a deep learning algorithm would also be key here. 

# OBJECT RECOGNITION
Finally we planned on using googlenet training model for imagenet, we were able to implement it on python but the main program is already taking too much time by itself, the code is in the "googlenet" folder.

# STARTING THE MAIN PROGRAM
Connect to the car by SSH (you need to be on the same network of course, a phone is good, don't use the university wifi):
ssh ubuntu@tegra-ubuntu
(password: ubuntu)
To start the main program: sudo python start.py
When started it needs to be interupted with Ctrl-C .
Each run is saved in a folder into the image folder (images taken and decision historic)

# HOW TO CONTINUE OUR PROJECT
- Implement traffic signs recog with deep learning
- Use a rotative camera instead of the classic camera to improve decisions
- Improve pedestrian detection to make it usable
