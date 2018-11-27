#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

#!/usr/bin/env python
# Python libs
import sys, time

# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy
from cv_bridge import CvBridge, CvBridgeError
# Ros Messages
from sensor_msgs.msg import Image, CameraInfo, PointCloud2
import sensor_msgs.point_cloud2 as pc2


# Constants:
topic_rgb_image = '/camera/color/image_raw'
topic_depth_image = '/camera/depth/image_rect_raw'
topic_point_cloud = '/camera/depth_registered/points'


# initialize cv bridge
bridge = CvBridge()

cv_image1=None
cv_image2=None
pts=None

def callback_rgb(data):
    global cv_image1
    #### direct conversion to CV2 ####
    try:
      cv_image1 = bridge.imgmsg_to_cv2(data, "bgr8")
      #print(type(cv_image1))
    except CvBridgeError as e:
      print(e)

    #(rows,cols,channels) = cv_image1.shape
    #print('hi',rows,cols,channels)

    # convert color input image to grayscale
    #gray = cv2.cvtColor(cv_image1, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Image window", gray)

def callback_depth(data):
    global cv_image2
    try:
        cv_image2 = bridge.imgmsg_to_cv2(data, "passthrough")
        print(type(cv_image2))
    except CvBridgeError as e:
        print(e)
        #return None
    #return cv_image
    # cv2.imshow("Depth image. By: Casch!!!", cv_image2)
    # cv2.waitKey(3)
def callback_pointCloud(data):
    global pts
    pts = list(pc2.read_points(data, skip_nans=False, field_names=("x", "y", "z")))
    # print(len(pts))
    # print('Cesar Sinchiguano')
    # print(type(pts))
    # print(pts[0:1])
    if len(pts) == 307200:
        pts= np.array(list(pts)).reshape((480,640,3))
        #print(type(pts))
    # elif len(pts) == 172800:
    #     pc = np.array(list(pts)).reshape((360,480,3))
    print(pts.shape)

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
def main():
    # In ROS, nodes are uniquely named.
    rospy.init_node('listener', anonymous=True)


    #Subscriber to the rgb, rgbd and point cloud data...
    rospy.Subscriber(topic_rgb_image, Image, callback_rgb)
    rospy.Subscriber(topic_depth_image, Image, callback_depth)
    rospy.Subscriber(topic_point_cloud, PointCloud2, callback_pointCloud)

    while(True):
       # get rgb image
        img = get_image()

        #get point PointCloud2
        pc=get_point_cloud()

        #get depth image
        dpth=get_depth()


        # wait for image or point cloud to be ready
        if img is None:
            continue
        elif pc is None:
            continue
        elif dpth is None:
            continue
        numpy_horizontal = np.hstack((img, pc))

        print('good!!!')
        img = get_image()
        cv2.imshow('image',pc)
        cv2.waitKey(3)

    # close any open windows
    cv2.destroyAllWindows()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()
