#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class yumi_group(object):

    def __init__(self):
        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('yumin_group_python', anonymous=True)

        ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
        ## to a planning group (group of joints).
        temp="right_arm"
        group_name = "panda_arm"
        move_group = moveit_commander.MoveGroupCommander(group_name)

        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
        ## trajectories in Rviz:
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

        ## Getting Basic Information
        # We can get the name of the reference frame for this robot:
        planning_frame = move_group.get_planning_frame()
        print "============ Planning frame: %s" % planning_frame

        # # We can also print the name of the end-effector link for this group:
        # eef_link = move_group.get_end_effector_link()
        # print "============ End effector link: %s" % eef_link
        # # We can get a list of all the groups in the robot:
        # group_names = robot.get_group_names()
        # print "============ Available Planning Groups:", robot.get_group_names()

        # Sometimes for debugging it is useful to print the entire state of the
        # robot:
        print "============ Printing robot state"
        print robot.get_current_state()
        print ""
        #Misc variables
        self.box_name = ''
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        #home = move_group.get_current_joint_values()
        self.display_trajectory_publisher = display_trajectory_publisher
        #self.planning_frame = planning_frame
        #self.eef_link = eef_link
        #self.group_names = group_names

    def go_to_home(self):
        #home position!!!
        move_group = self.move_group
        ## The Panda's zero configuration is at a `singularity'so the first
        ## thing we want to do is move it to a slightly better configuration.
        # We can get the joint values from the group and adjust some of the values:
        home = move_group.get_current_joint_values()
        home[0] = 0
        home[1] = -pi/4
        home[2] = 0
        home[3] = -pi/2
        home[4] = 0
        home[5] = pi/3
        home[6] = 0

        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        move_group.go(home, wait=True)

    def go_to_joint_state(self):
        '''Planning to a Joint Goal'''
        move_group = self.move_group

        joint_goal=move_group.get_random_joint_values()



        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        move_group.go(joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()


    def go_to_pose_goal(self):
        ''' Planning to a Pose Goal'''
        move_group = self.move_group

        ## We can plan a motion for this group to a desired pose for the
        ## end-effector:
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = 1.0
        pose_goal.position.x = 0.4
        pose_goal.position.y = 0.1
        pose_goal.position.z = 0.4

        move_group.set_pose_target(pose_goal)

        ## Now, we call the planner to compute the plan and execute it.
        plan = move_group.go(wait=True)
        # Calling `stop()` ensures that there is no residual movement
        move_group.stop()
        # It is always good to clear your targets after planning with poses.
        # Note: there is no equivalent function for clear_joint_value_targets()
        move_group.clear_pose_targets()

    def plan_cartesian_path(self, scale=1):
        move_group = self.move_group

        ## Cartesian Paths
        ## You can plan a Cartesian path directly by specifying a list of waypoints
        ## for the end-effector to go through.

        waypoints = []

        wpose = move_group.get_current_pose().pose
        wpose.position.z -= scale * 0.1  # First move up (z)
        wpose.position.y += scale * 0.2  # and sideways (y)
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.y -= scale * 0.1  # Third move sideways (y)
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = move_group.compute_cartesian_path(
                                           waypoints,   # waypoints to follow
                                           0.01,        # eef_step
                                           0.0)         # jump_threshold

        move_group.execute(plan, wait=True)

def main():
    #print "============ Press `Enter` to start (press ctrl-d to exit) ......"
    raw_input()
    yumiR=yumi_group()
    counter=0
    yumiR.go_to_home()
    import time
    time.sleep(0.5)
    while(True):
        print "\n============ Press `Enter` to execute a movement using a joint state goal ..."
        raw_input()
        yumiR.go_to_joint_state()
        #yumiR.plan_cartesian_path()
        counter+=1
        rospy.loginfo("counter: %s",counter)

        #yumiR.go_to_home()
        #time.sleep(0.5)
if __name__=='__main__':
    main()
