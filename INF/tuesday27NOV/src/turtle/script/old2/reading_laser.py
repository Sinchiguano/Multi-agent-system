#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser0(msg):
    # 720 / 5 = 144
    regions0 = [
        min(min(msg.ranges[0:143]), 10),
        min(min(msg.ranges[144:287]), 10),
        min(min(msg.ranges[288:431]), 10),
        min(min(msg.ranges[432:575]), 10),
        min(min(msg.ranges[576:713]), 10),
    ]
    print('regions0',regions0)


def clbk_laser1(msg):
    # 720 / 5 = 144
    regions1 = [
        min(min(msg.ranges[0:143]), 10),
        min(min(msg.ranges[144:287]), 10),
        min(min(msg.ranges[288:431]), 10),
        min(min(msg.ranges[432:575]), 10),
        min(min(msg.ranges[576:713]), 10),
    ]
    print('regions1',regions1)

def main():
    rospy.init_node('reading_laser')

    sub0= rospy.Subscriber('/robot0/laser_0', LaserScan, clbk_laser0)

    sub1= rospy.Subscriber('/robot1/laser_0', LaserScan, clbk_laser1)
    rospy.spin()

if __name__ == '__main__':
    main()
