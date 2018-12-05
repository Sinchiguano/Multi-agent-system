#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

import sys, time

# numpy and scipy
import numpy as np
from scipy.ndimage import filters
from geometry_msgs.msg import Twist
from math import radians
# OpenCV
import cv2

# Ros libraries
import roslib
import rospy
from cv_bridge import CvBridge, CvBridgeError
# Ros Messages
from sensor_msgs.msg import Image, CameraInfo, PointCloud2
import sensor_msgs.point_cloud2 as pc2


# initialize cv bridge
bridge = CvBridge()

cv_image1=None
cv_image2=None
pts=None
pc=None

def callback_rgb(data):
    global cv_image1
    #### direct conversion to CV2 ####
    try:
      cv_image1 = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print()

def callback_depth(data):
    global cv_image2
    try:
        cv_image2 = bridge.imgmsg_to_cv2(data, "passthrough")
        #print(type(cv_image2))
    except CvBridgeError as e:
        print()
def callback_pointCloud(data):
    global pts
    global pc
    # print(len(pts))
    # print(type(pts))
    # print(pts[0:1])
    if data is not None:
        print('there is something at least!!!')
        pts = list(pc2.read_points(data, skip_nans=False, field_names=("x", "y", "z")))
        temp=pc2.read_points(data, skip_nans=False, field_names=("x", "y", "z"))
        print('i am here:',type(temp))
        if len(pts) == 307200:
            pc = np.array(list(pts)).reshape((480,640,3))
        elif len(pts) == 172800:
            pc = np.array(list(pts)).reshape((360,480,3))
    else:
        rospy.logerr("No point cloud image, did you initialize Turtlebot(pc=True)")
    print(type(pc))

def infoDepthCallback(msg):
    #print('received info from depth camera!!!',msg)
    print()
def infoColorCallback(msg):
    rospy.loginfo("received info from color camera!!!%s",msg)

def get_image():
    global cv_image1
    return cv_image1
def get_depth():
    global cv_image2
    return cv_image2
def get_point_cloud():
    global pts
    return pts

x_range = (-0.3, 0.3)
z_range = (0.3, 3.0)

MOVE = 1
ROTATE = 2

running = True
active = True

def main():
    # In ROS, nodes are uniquely named.
    rospy.init_node('listener', anonymous=True)
    #Subscriber to the rgb, rgbd, point cloud data and informations of the first two of them...
    # rospy.Subscriber('/camera/rgb/image_raw', Image, callback_rgb)
    # rospy.Subscriber('/camera/depth/image_raw', Image, callback_depth)
    rospy.Subscriber('robot1/camera/depth/points', PointCloud2, callback_pointCloud)

    # rospy.Subscriber('/camera/depth/camera_info', CameraInfo,infoDepthCallback)
    # rospy.Subscriber('/camera/rgb/camera_info', CameraInfo,infoColorCallback)

    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    #pub1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=10)
    pub = rospy.Publisher('robot1/mobile_base/commands/velocity', Twist, queue_size=10)
    rate = rospy.Rate(10)

    velo_cmd = Twist()



    direction = None
    while(True):
        #print('working!!!')
        #get rgb image
        #img = get_image()

        #get point PointCloud2
        pc=get_point_cloud()

        #get depth image
        #dpth=get_depth()

        # wait for image or point cloud to be ready
        if pc is None:
            continue
        # elif pc is None:
        #     continue
        # elif dpth is None:
        #     continue

        # mask out floor points in y coordinates!!!
        mask = pc[:,:,1] < 0.2
        #print(pc[:2,:2,:])
        #exit(0)

        # mask point too far in z coordinates!!!
        mask = np.logical_and(mask, pc[:,:,2] < 3.0)

        if np.count_nonzero(mask) <= 0:
            continue

        # empty image
        image = np.zeros(mask.shape)
        print('filter of my pc',mask.shape)

        # assign depth i.e. distance to image
        image[mask] = np.int8(pc[:,:,2][mask] / 3.0 * 255)
        im_color = cv2.applyColorMap(255 - image.astype(np.uint8), cv2.COLORMAP_JET)

        # show image
        #cv2.imshow('Obstacles', im_color)
        #cv2.waitKey(1)

        # check obstacle
        mask = np.logical_and(mask, pc[:,:,1] > -0.2)
        data = np.sort(pc[:,:,2][mask])


        state = MOVE
        if data.size > 50:
            dist = np.percentile(data, 10)
            print(dist)
            if dist < 0.6:
                state = ROTATE

        # command velocity
        if active and state == MOVE:
            velo_cmd.linear.x = 0.2
            velo_cmd.angular.z = 0.0
            pub.publish(velo_cmd)
            direction = None

        elif active and state == ROTATE:
            if direction is None:
                direction = np.sign(np.random.rand() - 0.5)
            velo_cmd.linear.x = 0.0
            velo_cmd.angular.z = 0.2*direction
            pub.publish(velo_cmd)
        rate.sleep()

    #close any open windows
    cv2.destroyAllWindows()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()
