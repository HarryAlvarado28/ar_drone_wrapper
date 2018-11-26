#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyleft (c) 2018 CITIC.
## This module export all the topics needed for the drone work
# /ardrone/cmd_vel
# /ardrone/odom
# /ardrone/front_camera/raw_image
# /ardrone/front_camera/raw_image_compressed
# /ardrone/altitude
# /ardrone/battery
# /ardrone/tf
# /ardrone/nav_data
# /ardrone/takeoff
# /ardrone/land
# /ardrone/reset
# /ardrone/mag
# Tag detection, I will work on it in the next version

# Authors:
#   * Ariel Vernaza (DSAPANDORA)
#     avernaza@citicup.org
import sys
from std_msgs.msg import String
from std_msgs.msg import Empty
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2
from libardrone import ardrone


def cmd_vel(move_data):
    # TODO

def front_camera_image():
    # TODO

def odom():
    # TODO

def altitude():
    # TODO

def battery():
    # TODO

def tf():
    # TODO

def nav_data():
    # TODO

def takeoff(data):
    # TODO

def land(data):
    # TODO

def reset(data):
    # TODO

def mag():
    # TODO
