#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
#!/usr/bin/env python
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
from geometry_msgs.msg import TransformStamped
from tf.transformations import euler_from_quaternion



def handle_turtle_pose(msg, turtlename):

    broadcasterOBJECT = tf2_ros.TransformBroadcaster()
    transformOBJECT = TransformStamped()

    transformOBJECT.header.stamp = rospy.Time.now()
    transformOBJECT.header.frame_id = "world"
    transformOBJECT.child_frame_id = turtlename

    transformOBJECT.transform.translation.x = msg.x
    transformOBJECT.transform.translation.y = msg.y
    transformOBJECT.transform.translation.z = 0.0

    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    transformOBJECT.transform.rotation.x = q[0]
    transformOBJECT.transform.rotation.y = q[1]
    transformOBJECT.transform.rotation.z = q[2]
    transformOBJECT.transform.rotation.w = q[3]

    broadcasterOBJECT.sendTransform(transformOBJECT)

def main():

    rospy.init_node('tf2_turtle_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,turtlesim.msg.Pose,handle_turtle_pose,turtlename)
    rospy.spin()

if __name__ == '__main__':
    main()
