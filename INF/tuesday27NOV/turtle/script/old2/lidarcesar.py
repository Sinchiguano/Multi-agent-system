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

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty

from math import radians
import tf
import math
import time

regions0=dict()
regions1=dict()

pub = None
goal_position = Point()
goal_position.x = 5
goal_position.y = 9
goal_position.z= 0

goal_angle=math.atan2(goal_position.y,goal_position.x)





current_position1 = Point(0.0,0.0,0.0)
old_position1=Point(0.0,0.0,0.0)
delta_xy1=Point(0.0,0.0,0.0)
theta1=0.0
temp1=False

current_position0 = Point(0.0,0.0,0.0)
old_position0=Point(0.0,0.0,0.0)
delta_xy0=Point(0.0,0.0,0.0)
theta0=0.0
temp0=False


def odometry_callback1(msg):
    global current_position1
    global old_position1
    global temp1
    current_position1.x=msg.pose.pose.position.x
    current_position1.y=msg.pose.pose.position.y
    orientation_q=msg.pose.pose.orientation
    quaternion=[orientation_q.x,orientation_q.y,orientation_q.z,orientation_q.w]
    roll,pitch,yaw=tf.transformations.euler_from_quaternion(quaternion)
    global theta1
    theta1=yaw
    print("(x={0}, y={1})".format(current_position1.x,current_position1.y))
    print('theta: ',math.degrees(theta1))
    if old_position1.x!=current_position1.x and  old_position1.y!=current_position1.y:
        temp1=True
        old_position1=current_position1
    else:
        temp1=False
    print(temp1)

def odometry_callback0(msg):
    global current_position0
    global old_position0
    global temp0
    current_position0.x=msg.pose.pose.position.x
    current_position0.y=msg.pose.pose.position.y
    orientation_q=msg.pose.pose.orientation
    quaternion=[orientation_q.x,orientation_q.y,orientation_q.z,orientation_q.w]
    roll,pitch,yaw=tf.transformations.euler_from_quaternion(quaternion)
    global theta0
    theta0=yaw
    print("(x={0}, y={1})".format(current_position0.x,current_position0.y))
    print('theta: ',math.degrees(theta0))

    if old_position1.x!=current_position0.x and  old_position1.y!=current_position0.y:
        temp0=True
        old_position0=current_position0
    else:
        temp0=False
    print(temp0)



def clbk_laser0(msg):
    global regions0
    regions0 = {
        'right':  min(min(msg.ranges[0:128]), 10),
        'fright': min(min(msg.ranges[129:256]), 10),
        'front':  min(min(msg.ranges[257:384]), 10),
        'fleft':  min(min(msg.ranges[385:512]), 10),
        'left':   min(min(msg.ranges[513:640]), 10),
    }
    #print(regions0)

def clbk_laser1(msg):
    global regions1
    regions1 = {
        'right':  min(min(msg.ranges[0:128]), 10),
        'fright': min(min(msg.ranges[129:256]), 10),
        'front':  min(min(msg.ranges[257:384]), 10),
        'fleft':  min(min(msg.ranges[385:512]), 10),
        'left':   min(min(msg.ranges[513:640]), 10),
    }
    #print(regions1)


def take_action(temp,flag,change):

    regions=flag
    pub=temp
    msg = Twist()
    linear_x = 0
    angular_z = 0

    state_description = ''

    if regions['front'] > 1.5 and regions['fleft'] > 1.5 and regions['fright'] > 1.5:
        state_description = 'case 1.5 - nothing'
        linear_x = 0.6
        angular_z = 0
    elif regions['front'] < 1.5 and regions['fleft'] > 1.5 and regions['fright'] > 1.5:
        state_description = 'case 2 - front'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1.5 and regions['fleft'] > 1.5 and regions['fright'] < 1.5:
        state_description = 'case 3 - fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1.5 and regions['fleft'] < 1.5 and regions['fright'] > 1.5:
        state_description = 'case 4 - fleft'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1.5 and regions['fleft'] > 1.5 and regions['fright'] < 1.5:
        state_description = 'case 5 - front and fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] < 1.5 and regions['fleft'] < 1.5 and regions['fright'] > 1.5:
        state_description = 'case 6 - front and fleft'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1.5 and regions['fleft'] < 1.5 and regions['fright'] < 1.5:
        state_description = 'case 7 - front and fleft and fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1.5 and regions['fleft'] < 1.5 and regions['fright'] < 1.5:
        state_description = 'case 8 - fleft and fright'
        linear_x = 0.3
        angular_z = 0
    # if not change:
    #     state_description = 'case 8 - no changes'
    #     linear_x = 0.6
    #     angular_z = 0.3
    else:
        linear_x = 0
        angular_z = 0.6
        state_description = 'unknown case'
        rospy.loginfo(regions)

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)

def main():
    global temp1
    global temp0
    global regions0
    global regions1
    rospy.init_node('reading_laser')
    sub1 = rospy.Subscriber('/robot1/odom', Odometry, odometry_callback1)
    sub0 = rospy.Subscriber('/robot0/odom', Odometry, odometry_callback0)

    pub0 = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size=1)

    sub0 = rospy.Subscriber('/robot0/laser_0', LaserScan, clbk_laser0)

    pub1 = rospy.Publisher('/robot1/cmd_vel', Twist, queue_size=1)

    sub1 = rospy.Subscriber('/robot1/laser_0', LaserScan, clbk_laser1)

    import time

    while(True):

        if not (regions0 and regions1):
            continue
        print('robot0:', regions0)
        take_action(pub0,regions0,temp0)
        print(regions0)
        time.sleep(0.300)
        take_action(pub1,regions1,temp1)
        print('robot1:',regions1)
        time.sleep(0.300)
        rospy.loginfo("Moving around!!!")

if __name__ == '__main__':
    main()
