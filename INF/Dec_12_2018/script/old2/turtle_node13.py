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
goal_position.y =3
goal_position.z= 0



def odometry1_callback(msg):

    global current_position
    current_position.x=msg.pose.pose.position.x
    current_position.y=msg.pose.pose.position.y
    orientation_data=msg.pose.pose.orientation
    quaternion=[orientation_data.x,orientation_data.y,orientation_data.z,orientation_data.w]
    roll,pitch,yaw=tf.transformations.euler_from_quaternion(quaternion)
    current_position.z=yaw

def euclidean_distance(X,Y):

    return sqrt(pow((X),2)+pow((Y),2))
def main():

    rospy.init_node('TurtleBot', anonymous=True)

    #This declares that your node subscribes to the /odom topic which is of type Odometry.
    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    sub1_1 = rospy.Subscriber('/robot1/odom', Odometry, odometry1_callback)

    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    #sub2_1 = rospy.Subscriber('/robot2/odom', Odometry, odometry2_callback)
    #-----------------------------------------------------------
    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    pub1_1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=10)

    # set up the odometry reset publisher
    pub1_2 = rospy.Publisher('/robot1/mobile_base/commands/reset_odometry', Empty, queue_size=10)

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
    k1=0.35
    k2=10.5

    while (True):



        #Limit the linear velocity
        tmp=goal_position.x*math.cos(current_position.z)+goal_position.y*math.sin(current_position.z)
        print(tmp)
        term_sqr=sqrt(current_position.x**2+current_position.y**2+2*abs(tmp)*l_radio+pow(l_radio,2))

        alpha=k1/(k2+term_sqr)
        u1=alpha*(tmp+l_radio)

        #Limit the angular velocity
        u2=(-1*alpha/l_radio)*(goal_position.x*math.sin(current_position.z)-goal_position.y*math.cos(current_position.z))

        #Linear velocity
        velo_cmd_1.linear.x =1.5*u1
        print('linear velocity:',u1)

        #Angular velocity
        velo_cmd_1.angular.z = u2
        #print('angular velocity:',u2)


        pub1_1.publish(velo_cmd_1)


        rate.sleep()
        #rospy.loginfo("Moving into goal pose!!!")
    print('Goal reached out!!!')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
