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
from math import pow,atan2,sqrt,radians
import tf
import time
import math




current_position = Point(0.0,0.0,0.0)
steer_position=Point(0.0,0.0,0.0)
goal_position = Point()
goal_position.x = 4
goal_position.y = 4
goal_position.z= 0


current_theta=0.0
steer_theta=0.0


pGain=0.025
iGain=0.0
dGain=0.0

I_max=500
I_min=500





def odometry_callback(msg):

    global current_position
    global current_theta
    current_position.x=msg.pose.pose.position.x
    current_position.y=msg.pose.pose.position.y
    orientation_data=msg.pose.pose.orientation
    quaternion=[orientation_data.x,orientation_data.y,orientation_data.z,orientation_data.w]
    roll,pitch,yaw=tf.transformations.euler_from_quaternion(quaternion)
    current_theta=yaw
    #print("(x={0}, y={1})".format(current_position.x,current_position.y))
    #print('theta: ',math.degrees(theta))

def euclidean_distance():

    global goal_position
    global current_position
    global steer_position
    steer_position.x=goal_position.x-current_position.x
    steer_position.y=goal_position.y-current_position.y

    return sqrt(pow((steer_position.x),2)+pow((steer_position.y),2))

def main():

    rospy.init_node('TurtleBot', anonymous=True)

    #This declares that your node subscribes to the /odom topic which is of type Odometry.
    #When new messages are received, odometry_callback is invoked with the message as the first argument.
    sub_1 = rospy.Subscriber('/odom', Odometry, odometry_callback)

    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    pub_1 = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

    # set up the odometry reset publisher
    pub_2 = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)



    # reset odometry (these messages take a few iterations to get through)
    startingTime = time.time()
    while ((time.time() - startingTime)< 0.25):
        pub_2.publish(Empty())

    rate = rospy.Rate(10)

    velo_cmd = Twist()

    global current_theta
    global steer_theta

    global goal_position
    global current_position
    global steer_position

    global I_min
    global I_max

    tmp_dist=euclidean_distance()


    global pGain
    global dGain
    global iGain

    current_error=0.0
    previous_error=0.0
    control_variable=0.0
    I_error=0.0

    while (tmp_dist>=0.01):

        steer_position.x=goal_position.x-current_position.x
        steer_position.y=goal_position.y-current_position.y

        steer_theta=math.atan2(steer_position.y,steer_position.x)


        current_error=math.degrees(steer_theta)-math.degrees(current_theta)

        #Proportional part
        p_error=current_error
        P_term = pGain * p_error

        # #Derivativa part
        # d_error=current_error - previous_error
        # D_term = dGain *d_error
        # previous_error = current_error
        #
        # #Integral part
        # I_error += current_error
        # if I_error > I_max:
        # 	I_error = I_max
        # elif I_error < I_min:
        # 	I_error = I_min
        # I_term = iGain*I_error
        #
        # #PID controller
        # PID = P_term + I_term + D_term

        control_variable=P_term


        #Limit the angular velocity
        if (control_variable>0.3):
            control_variable=0.3
        elif (control_variable<-0.3):
            control_variable=-0.3


        tmp_dist=euclidean_distance()
        #Limit the linear velocity
        if (tmp_dist>0.2):
            tmp_dist=0.2

        #Linear velocity
        velo_cmd.linear.x = 1.5*tmp_dist

        #Angular velocity
        velo_cmd.angular.z = control_variable

        pub_1.publish(velo_cmd)

        rate.sleep()
        rospy.loginfo("Moving into goal pose!!!")
    print('Goal reached out!!!')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
