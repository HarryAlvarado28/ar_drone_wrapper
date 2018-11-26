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

drone = None

def cmd_vel(move_data):
    global drone
    if move_data.linear.x == -1:
        drone.move_right()
    if move_data.linear.y == 1:
        drone.move_forward()
    if move_data.linear.z == 1:
        drone.move_up()
    if move_data.linear.x == 1:
        drone.move_left()
    if move_data.linear.y == -1:
        drone.move_backward()
    if move_data.linear.z == -1:
        drone.move_down()


def takeoff(_data):
    global drone
    drone.takeoff()

def land(_data):
    global drone
    drone.land()

def reset(_data):
    global drone
    drone.reset()

def main(args):
    rospy.init_node('drone_driver', anonymous=True)
    drone = ardrone.ARDrone(True)
    drone.reset()
    cmd_vel_sub = rospy.Subscriber("/ardrone/cmd_vel", Twist, cmd_vel,  queue_size = 1)
    takeoff_sub = rospy.Subscriber("/ardrone/takeoff", Empty, takeoff,  queue_size = 1)
    land_sub = rospy.Subscriber("/ardrone/land", Empty, land,  queue_size = 1)
    reset_sub = rospy.Subscriber("/ardrone/reset", Empty, reset,  queue_size = 1)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        drone.halt()
        print "Shutting down ROS ARDRONE DRIVER module"

if __name__ == '__main__':
    main(sys.argv)
