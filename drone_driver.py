#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyleft (c) 2018 CITIC.
## This module export all the topics needed for the drone work
# /ardrone/cmd_vel
# /ardrone/nav_data
# /ardrone/takeoff
# /ardrone/land
# /ardrone/reset
# /ardrone/odom
# /ardrone/front_camera/raw_image
# /ardrone/front_camera/raw_image_compressed
# /ardrone/altitude
# /ardrone/battery
# /ardrone/tf
# /ardrone/mag
# Tag detection, I will work on it in the next version

# Authors:
#   * Ariel Vernaza (DSAPANDORA)
#     avernaza@citicup.org
import sys
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2
from libardrone import ardrone
from multiprocessing import Process

drone = None

def images():
    while(True):
        print 'Images'

def nav_data():
    while(True):
        print "nav_data"


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
    # Use two threads to complete the drone data
    nav_data_thread = Process(target=nav_data)
    images_thread = Process(target=images)
    try:
        nav_data_thread.start()
        nav_data_thread.join()
        images_thread.start()
        images_thread.join()
        rospy.spin()
    except KeyboardInterrupt:
        drone.halt()
        print "Shutting down ROS ARDRONE DRIVER module"

if __name__ == '__main__':
    main(sys.argv)
