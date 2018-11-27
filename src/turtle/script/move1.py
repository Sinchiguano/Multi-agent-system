#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import radians


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    #rospy.on_shutdown(self.shutdown)
    cmd_vel1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=10)
    cmd_vel2 = rospy.Publisher('/robot2/mobile_base/commands/velocity', Twist, queue_size=10)

	# create two different Twist() variables(objects).
    # One for moving forward and the other one for turning 45 degrees.

    # Go forward at 0.2 m/s
    #======================
    move_cmd1 = Twist()
    move_cmd1.linear.x = 0.1

    move_cmd2 = Twist()
    move_cmd2.linear.x = 0.1

    # Turn at 45 deg/s
    #=======================

    rate = rospy.Rate(5) # 5hz
    #while (not rospy.is_shutdown()):
    # Go forward 0.4 m (2 seconds * 0.2 m / seconds)
    rospy.loginfo("Going Forward")

    for x in range(0,50):
        print('hi')
        cmd_vel1.publish(move_cmd1)
        cmd_vel2.publish(move_cmd2)
        rate.sleep()


    # Go backward at 0.2 m/s
    #======================

    move_cmd1.linear.x = -0.1
    move_cmd2.linear.x = -0.1

    # Turn at 45 deg/s
    #=======================

    rate = rospy.Rate(5) # 5hz
    #while (not rospy.is_shutdown()):
    # Go forward 0.4 m (2 seconds * 0.2 m / seconds)
    rospy.loginfo("Going backward")

    for x in range(0,50):
        print('hi')
        cmd_vel1.publish(move_cmd1)
        cmd_vel2.publish(move_cmd2)
        rate.sleep()







    rate.sleep()
    print('thank!!!')



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
