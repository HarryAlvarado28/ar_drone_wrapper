#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
#check world debug
import sys
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
import pygame
from pygame.locals import *
import cv2
import os

video_size = 700, 500
velocity_publisher = rospy.Publisher('/ardrone/cmd_vel', Twist, queue_size=10)

def key_action():
    vel_msg = Twist()
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        vel_msg.linear.x = 1
    if keys[K_UP]:
        vel_msg.linear.y = 1
    if keys[K_RIGHT]:
        vel_msg.linear.x = -1
    if keys[K_DOWN]:
        vel_msg.linear.y = -1
    if keys[K_SPACE]:
        vel_msg.linear.z = 1
    if keys[K_BACKSPACE]:
        vel_msg.linear.z = -1
    return vel_msg

def main(args):
    '''Initializes and cleanup ros node'''
    rospy.init_node('world_observation_client', anonymous=True)
    try:
        screen = pygame.display.set_mode(video_size)
        while True:
            surf = pygame.image.load(os.path.join('data', 'image.jpg'))
            screen.blit(surf, (0, 0))
            pygame.display.update()
            vel_msg = key_action()
            velocity_publisher.publish(vel_msg)
            pygame.event.pump()
    except KeyboardInterrupt:
        print("Shutting down ROS Gym Image Viewer module")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
