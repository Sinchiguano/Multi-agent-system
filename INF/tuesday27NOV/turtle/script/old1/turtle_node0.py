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
from math import radians
import tf
import math
import time


goal_position = Point()
goal_position.x = 0.3
goal_position.y = 0.4
goal_position.z= 0

goal_angle=math.atan2(goal_position.y,goal_position.x)



current_position = Point(0.0,0.0,0.0)
error_position=Point(0.0,0.0,0.0)
theta=0.0




class PID:
    """
    Discrete PID control
    """

    def __init__(self, P=2.0, I=0.0, D=1.0):

        self.pGain=P
        self.iGain=I
        self.dGain=D

        self.previousError=0.0
        self.currentError=0.0

        self.set_point=0.0

        self.p_error=0.0
        self.d_error=0.0
        self.I_error=0.0

        self.I_max=500
        self.I_min=500

    def update_pid(self,current_value):
        """
        Calculate PID output value for given reference input and feedback
        """
        self.currentError = self.set_point - current_value
        #Proportional part
        self.p_error=self.currentError
        self.P_term = self.pGain * self.p_error
        #Derivativa part
        self.d_error=self.currentError - self.previousError
        self.D_term = self.dGain *self.d_error
        self.previousError = self.currentError
        #Integral part
        self.I_error += self.error
        if self.I_error > self.I_max:
        	self.I_error = self.I_max
        elif self.I_error < self.I_min:
        	self.I_error = self.I_min
        self.I_term = self.iGain*self.I_error
        #PID controller
        PID = self.P_term + self.I_term + self.D_term

        return PID


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
    sub = rospy.Subscriber('/odom', Odometry, odometry_callback)

    #Declares that your node is publishing to the cmd/input/navi topic using the message type Twist.
    pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

    rate = rospy.Rate(10) # 5hz
    velo_cmd = Twist()

    global theta
    global goal_position
    while (not rospy.is_shutdown()):

        error_position.x=goal_position.x-current_position.x
        error_position.y=goal_position.y-current_position.y
        goal_angle=math.atan2(goal_position.y,goal_position.x)

        if abs(goal_angle-theta)>math.radians(5):
            velo_cmd.linear.x = 0
            velo_cmd.angular.z = 0.2
            pub.publish(velo_cmd)
            rospy.loginfo("Moving around!!!")
        else:
            velo_cmd.linear.x = 0.2
            velo_cmd.angular.z = 0
            pub.publish(velo_cmd)
            rospy.loginfo("Moving into goal pose!!!")
            if error_position.x<0.1 and error_position.y<0.1:
                print('Goal done!!!')
                break
        rate.sleep()
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
