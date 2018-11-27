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
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty

from math import radians
import tf
import math
import time


from sensor_msgs.msg import LaserScan


pub = None
goal_position = Point()
goal_position.x = 5
goal_position.y = 9
goal_position.z= 0

goal_angle=math.atan2(goal_position.y,goal_position.x)



current_position = Point(0.0,0.0,0.0)
delta_xy=Point(0.0,0.0,0.0)
theta=0.0



def odometry_callback(msg):
    #print('====================')
    global current_position
    current_position.x=msg.pose.pose.position.x
    current_position.y=msg.pose.pose.position.y
    orientation_q=msg.pose.pose.orientation
    quaternion=[orientation_q.x,orientation_q.y,orientation_q.z,orientation_q.w]
    roll,pitch,yaw=tf.transformations.euler_from_quaternion(quaternion)
    global theta
    theta=yaw
    #print("(x={0}, y={1})".format(current_position.x,current_position.y))
    #print('theta: ',math.degrees(theta))



def main():

    rospy.init_node('TurtleBot', anonymous=True)

    #This declares that your node subscribes to the /odom topic which is of type Odometry.
    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    #sub = rospy.Subscriber('/robot1/odom', Odometry, odometry_callback)
    sub = rospy.Subscriber('/robot0/odom', Odometry, odometry_callback)

    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    #pub = rospy.Publisher('/robot1/cmd_vel', Twist, queue_size=10)
    pub = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size=10)

    # # set up the odometry reset publisher
    # reset_odom = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    #
    # # reset odometry (these messages take a few iterations to get through)
    # timer = time.time()
    # while time.time() - timer < 0.25:
    #     reset_odom.publish(Empty())


    rate = rospy.Rate(10) # 5hz

    velo_cmd = Twist()

    global theta
    global goal_position
    global current_position

    from math import pow,atan2,sqrt
    delta_xy.x=goal_position.x-current_position.x
    delta_xy.y=goal_position.y-current_position.y
    distance=sqrt(pow((delta_xy.x),2)+pow((delta_xy.y),2))

    pGain=0.025
    pGain_x=0.5

    goal_angle=math.atan2(goal_position.y,goal_position.x)
    process_angle=math.atan2(delta_xy.y,delta_xy.x)

    while (distance>=0.10):

        delta_xy.x=goal_position.x-current_position.x
        delta_xy.y=goal_position.y-current_position.y
        goal_angle_steer=math.atan2(delta_xy.y,delta_xy.x)

        distance=sqrt(pow((delta_xy.x),2)+pow((delta_xy.y),2))

        errorP_x=goal_position.x-current_position.x
        control_variable_x=pGain_x*errorP_x



        errorP=math.degrees(goal_angle_steer)-math.degrees(theta)
        control_variable=pGain*errorP

        #Limit the angular velocity
        if (control_variable>0.3):
            control_variable=0.3
        elif (control_variable<-0.3):
            control_variable=-0.3

        #Limit the linear velocity
        if (control_variable_x>0.3):
            control_variable_x=0.3

        #Linear velocity
        velo_cmd.linear.x = control_variable_x

        #Angular velocity
        velo_cmd.angular.z = control_variable


        print('goal_angle: ',math.degrees(goal_angle))
        print('goal_angle_steer',goal_angle_steer)
        print('theta: ',math.degrees(theta))
        print('errorP',errorP)
        print('control_variable',control_variable)

        # print(current_position.x)
        # print(current_position.y)
        # print(goal_position.x)
        # print(goal_position.y)




        pub.publish(velo_cmd)
        rate.sleep()
        #rospy.loginfo("Moving into goal pose!!!")
    print('Goal reached out!!!')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
