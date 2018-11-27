#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.
"""
proportional control!!!
"""
import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from math import pow,atan2,sqrt,radians
import tf
import time
import math


current_position_r1 = Point(0.0,0.0,0.0)#x,y,theta
steer_position_r1=Point(0.0,0.0,0.0)
goal_position_r1 = Point(3,0,0.0)
pGain=0.025


current_position_r2 = Point(0.0,0.0,0.0)#x,y,theta
steer_position_r2=Point(0.0,0.0,0.0)
#goal_position_r2 = Point(2,2,0.0)

def odometry_r1_callback(msg):

    global current_position_r1

    orientation_r1=msg.pose.pose.orientation
    quaternion_r1=[orientation_r1.x,orientation_r1.y,orientation_r1.z,orientation_r1.w]
    roll_r1,pitch_r1,yaw_r1=tf.transformations.euler_from_quaternion(quaternion_r1)

    current_position_r1.x=msg.pose.pose.position.x
    current_position_r1.y=msg.pose.pose.position.y
    current_position_r1.z=yaw_r1


def odometry_r2_callback(msg):

    global current_position_r2

    orientation_r2=msg.pose.pose.orientation
    quaternion_r2=[orientation_r2.x,orientation_r2.y,orientation_r2.z,orientation_r2.w]
    roll_r2,pitch_r2,yaw_r2=tf.transformations.euler_from_quaternion(quaternion_r2)

    current_position_r2.x=msg.pose.pose.position.x
    current_position_r2.y=msg.pose.pose.position.y
    current_position_r2.z=yaw_r2

def euclidean_distance():

    global goal_position_r1
    global current_position_r1
    global steer_position_r1
    steer_position_r1.x=goal_position_r1.x-current_position_r1.x
    steer_position_r1.y=goal_position_r1.y-current_position_r1.y

    return sqrt(pow((steer_position_r1.x),2)+pow((steer_position_r1.y),2))

def main():

    rospy.init_node('TurtleBot', anonymous=True)

    #robot1
    #-----------------------------
    #This declares that your node subscribes to the /odom topic which is of type Odometry.
    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    #rospy.Subscriber('/odom', Odometry, odometry_callback)
    sub_Odom_r1 = rospy.Subscriber('/robot1/odom', Odometry, odometry_r1_callback)

    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    #rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    pub_Vel_r1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=10)

    # set up the odometry reset publisher
    #rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    pub_ResOdom_r1 = rospy.Publisher('/robot1/mobile_base/commands/reset_odometry', Empty, queue_size=10)



    #robot2
    #-----------------------------
    #This declares that your node subscribes to the /odom topic which is of type Odometry.
    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    #rospy.Subscriber('/odom', Odometry, odometry_callback)
    sub_Odom_r2 = rospy.Subscriber('/robot2/odom', Odometry, odometry_r2_callback)

    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    #rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    pub_Vel_r2 = rospy.Publisher('/robot2/mobile_base/commands/velocity', Twist, queue_size=10)

    # set up the odometry reset publisher
    #rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    pub_ResOdom_r2 = rospy.Publisher('/robot2/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    #
    listener_r2 = tf.TransformListener()



    # reset odometry (these messages take a few iterations to get through)
    startingTime = time.time()
    while ((time.time() - startingTime)< 0.25):
        pub_ResOdom_r1.publish(Empty())

    while ((time.time() - startingTime)< 0.25):
        pub_ResOdom_r2.publish(Empty())

    rate = rospy.Rate(10)

    velR1 = Twist()
    velR2 = Twist()

    global current_position
    global goal_position
    global steer_position
    global pGain

    tmp_dist=euclidean_distance()


    current_error=0.0
    control_variable=0.0

    min_dist2=0.5
    min_dist3=2

    while (True):

        try:
            #listener_r2.waitForTransform('/robot2/base_footprint','/robot1/base_footprint', rospy.Time(0), rospy.Duration(5))
            trans,rot= listener_r2.lookupTransform('/robot2_tf/base_footprint','/robot1_tf/base_footprint',  rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue


        #turtle2
        #===========
        angular = 2* math.atan2(trans[1], trans[0])
        linear = 0.2* math.sqrt(trans[0] ** 2 + trans[1] ** 2)

        #distance from the leader
        dist_from_leader2= math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        print(dist_from_leader2)
        #Limit the angular velocity
        if (angular>0.3):
            angular=0.3
        elif (angular<-0.3):
            angular=-0.3

        if (linear>0.2):
            linear=0.2

        velR2.linear.x=2*linear
        velR2.angular.z =1.5* angular
        pub_Vel_r2.publish(velR2)
        # if dist_from_leader2>2:
        #     velR2.linear.x=2*linear
        #     velR2.angular.z =1.5* angular
        #     pub_Vel_r2.publish(velR2)
        # else:
        #     velR2.linear.x=0
        #     velR2.angular.z =0
        #     pub_Vel_r2.publish(velR2)



        rate.sleep()
        rospy.loginfo("Moving into goal pose!!!")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
