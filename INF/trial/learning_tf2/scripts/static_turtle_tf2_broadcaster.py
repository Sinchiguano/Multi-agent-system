#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

import rospy
# to get commandline arguments
import sys
#Because of transformations
import tf
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import TransformStamped
from tf.transformations import euler_from_quaternion
from tf2_ros import StaticTransformBroadcaster


def main():

    if len(sys.argv) < 8 :
        rospy.logerr('Invalid number of parameters!!!')
        sys.exit(0)
    else:
        if sys.argv[1] == 'world':
            rospy.logerr('Your static turtle name cannot be "world"')
            sys.exit(0)
        #-----------------------------------------------
        rospy.init_node('my_static_tf2_broadcaster')
        broadcaster = StaticTransformBroadcaster()
        #Here we create a TransformStamped object which will be the message we will send over once populated
        tf_object = TransformStamped()

        #Before stuffing the actual transform values we need to give it the appropriate metadata.
        tf_object.header.stamp = rospy.Time.now()
        #parent frame
        tf_object.header.frame_id = "world"
        #child frame
        #sys.argv is automatically a list of strings
        tf_object.child_frame_id = sys.argv[1]

        tf_object.transform.translation.x = float(sys.argv[2])
        tf_object.transform.translation.y = float(sys.argv[3])
        tf_object.transform.translation.z = float(sys.argv[4])

        quat = tf.transformations.quaternion_from_euler(float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
        tf_object.transform.rotation.x = quat[0]
        tf_object.transform.rotation.y = quat[1]
        tf_object.transform.rotation.z = quat[2]
        tf_object.transform.rotation.w = quat[3]

        broadcaster.sendTransform(tf_object)
        rospy.spin()
if __name__=='__main__':
    main()
