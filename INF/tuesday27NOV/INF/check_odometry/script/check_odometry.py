#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print('--------------------')
    # print(msg.pose.pose)
    # print('====================')
    print(type(msg.pose.pose))
    print('x: ',msg.pose.pose.position.x)
    print('y: ',msg.pose.pose.position.y)
    print('W: ',msg.pose.pose.orientation.w)
def main():

    rospy.init_node('odometry_node')
    #Subscribe to the following topic /odom
    rospy.Subscriber('/odom', Odometry, callback)
    print('nothing happens  ')
    rospy.spin()


if __name__=='__main__':
    main()
