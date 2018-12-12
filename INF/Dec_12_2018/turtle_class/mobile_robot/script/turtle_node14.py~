#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.



import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from math import pow,atan2,sqrt,radians
import tf
import time
import math
from tf.transformations import euler_from_quaternion


current_position = Point(0.0,0.0,0.0)
goal_position = Point()
goal_position.x =-3
goal_position.y =1
goal_position.z= 0



def odometry1_callback(msg):

    global current_position
    current_position.x=msg.pose.pose.position.x
    current_position.y=msg.pose.pose.position.y
    orientation_data=msg.pose.pose.orientation
    quaternion=[orientation_data.x,orientation_data.y,orientation_data.z,orientation_data.w]
    roll,pitch,yaw=tf.transformations.euler_from_quaternion(quaternion)
    current_position.z=yaw

def euclidean_distance():

    global goal_position
    global current_position

    tmp1=goal_position.x-current_position.x
    tmp2=goal_position.y-current_position.y

    return sqrt(pow((tmp1),2)+pow((tmp2),2))
def main():

    rospy.init_node('TurtleBot', anonymous=True)

    #This declares that your node subscribes to the /odom topic which is of type Odometry.
    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    sub1_1 = rospy.Subscriber('/robot1/odom', Odometry, odometry1_callback)
    sub1_1 = rospy.Subscriber('/odom', Odometry, odometry1_callback)

    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    #sub2_1 = rospy.Subscriber('/robot2/odom', Odometry, odometry2_callback)
    #-----------------------------------------------------------
    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    pub1_1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=10)
    pub1_1 = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

    # set up the odometry reset publisher
    pub1_2 = rospy.Publisher('/robot1/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    pub1_2 = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)

    #-----------------------------------------------------------
    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    # pub2_1 = rospy.Publisher('/robot2/mobile_base/commands/velocity', Twist, queue_size=10)
    # # set up the odometry reset publisher
    # pub2_2 = rospy.Publisher('/robot2/mobile_base/commands/reset_odometry', Empty, queue_size=10)

    # reset odometry (these messages take a few iterations to get through)
    startingTime = time.time()
    while ((time.time() - startingTime)< 0.35):
        pub1_2.publish(Empty())
    rate = rospy.Rate(10)

    velo_cmd_1 = Twist()

    l_radio=0.10
    alpha=0.055
    dis=euclidean_distance()

    while (dis>0.1):
        #My any positive function according to the paper
        dis=euclidean_distance()
        print('dist:',dis)
        print('goal x and y:',goal_position.x, goal_position.y)
        print('current x and y:',current_position.x,current_position.y)
        #Control the linear velocity
        tmp=goal_position.x*math.cos(current_position.z)+goal_position.y*math.sin(current_position.z)+l_radio
        u1=0.075*tmp*dis
        if (u1>0.2):
            u1=0.2
        elif(u1<-0.2):
            u1=-0.2
        #Control the angular velocity
        u2=(-1*alpha/l_radio)*(goal_position.x*math.sin(current_position.z)-goal_position.y*math.cos(current_position.z))

        #Linear velocity
        velo_cmd_1.linear.x =1.5*u1
        print('velocity:',u1)

        #Angular velocity
        velo_cmd_1.angular.z = u2
        #print('angular:',u2,math.degrees(u2))

        pub1_1.publish(velo_cmd_1)


        rate.sleep()
        rospy.loginfo("Moving into goal pose!!!")
    print('Goal reached out!!!')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
