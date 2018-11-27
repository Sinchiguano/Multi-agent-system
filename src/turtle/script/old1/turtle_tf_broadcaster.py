#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
import roslib
#roslib.load_manifest('learning_tf')
import rospy
import tf
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry


def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    ori=msg.pose.pose.orientation
    quaternion=[ori.x,ori.y,ori.z,ori.w]
    br.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, 0),quaternion,
                     rospy.Time.now(),
                     "world",
                     turtlename)
def main():
    rospy.init_node("turtle_tf_broadcaster")
    #turtlename = rospy.get_param('/robot1/tf_prefix')
    name_turtles=list()
    #wrong one
    name_turtles2=['robot1_tf','robot2_tf']

    #right one
    name_turtles1=['robot1','robot2']
    for turtle in name_turtles1:
        print(turtle)
        rospy.Subscriber('/%s/odom' % turtle,Odometry,handle_turtle_pose,turtle)
    rospy.spin()

if __name__ == '__main__':

    main()
