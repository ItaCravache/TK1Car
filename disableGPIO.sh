#!/bin/bash

#Set the 4 GPIO at low (0)
sudo echo 0 > /sys/class/gpio/gpio57/value
sudo echo 0 > /sys/class/gpio/gpio81/value
sudo echo 0 > /sys/class/gpio/gpio160/value
sudo echo 0 > /sys/class/gpio/gpio161/value
sudo echo 0 > /sys/class/gpio/gpio162/value
sudo echo 0 > /sys/class/gpio/gpio163/value
sudo echo 0 > /sys/class/gpio/gpio164/value
sudo echo 0 > /sys/class/gpio/gpio165/value
sudo echo 0 > /sys/class/gpio/gpio166/value
sudo echo 0 > /sys/class/gpio/gpio225/value
sudo echo 0 > /sys/class/gpio/gpio226/value


#Remove the GPIO form the list
sudo echo 57 > /sys/class/gpio/unexport
sudo echo 81 > /sys/class/gpio/unexport
sudo echo 160 > /sys/class/gpio/unexport
sudo echo 161 > /sys/class/gpio/unexport
sudo echo 162 > /sys/class/gpio/unexport
sudo echo 163 > /sys/class/gpio/unexport
sudo echo 164 > /sys/class/gpio/unexport
sudo echo 165 > /sys/class/gpio/unexport
sudo echo 166 > /sys/class/gpio/unexport
sudo echo 225 > /sys/class/gpio/unexport
sudo echo 226 > /sys/class/gpio/unexport


#GPIO list
sudo cat /sys/kernel/debug/gpio

