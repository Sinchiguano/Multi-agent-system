#include "ros/ros.h"
#include "tf/tf.h"
#include "robot/robot.h"
#include "geometry_msgs/Twist.h"


Robot::Robot() {
  treshold = 0.1;
  execute = false;
}

void Robot::odometryCallback (const nav_msgs::Odometry::ConstPtr& msg) {
  ROS_INFO("get odometry " );
  robot_pose = msg->pose.pose;
  if (execute) {
    followTheCarrot();
  }
}


void Robot::startExecutePath() {
  execute_start_time=ros::Time::now();
  execute = true;
}

void Robot::stopExecutePath() {
  execute = false;
}

void Robot::setPath(std::list<Waypoint> path) {
  plan = path;  
}

void Robot::setCommandPublisher( ros::Publisher * cmdpub) {
  command_publisher = cmdpub;
}

bool Robot::followTheCarrot() {
  while (!plan.empty() && plan.front().distanceTo(robot_pose) < treshold) {
      plan.pop_front();
  }
  if (plan.empty()) {
    geometry_msgs::Twist command;
    command.angular.z = 0;
    command.linear.x = 0;
    command_publisher->publish(command);
    return true;
  } else { 
    Waypoint actual_goal = plan.front();
    double dist = actual_goal.distanceTo(robot_pose);
    double angle = actual_goal.angleTo(robot_pose);
    tf::Quaternion q(
        robot_pose.orientation.x,
        robot_pose.orientation.y,
        robot_pose.orientation.z,
        robot_pose.orientation.w);
    tf::Matrix3x3 m(q);
    double roll, pitch, yaw;
    m.getRPY(roll, pitch, yaw);
    ROS_INFO("distance %f and angle %f to goal", dist,angle);
    ROS_INFO("robot roll %f , pitch %f yaw %f", roll, pitch, yaw);
    geometry_msgs::Twist command;
    double delta = angle - yaw;
    if (delta > M_PI ) {
      delta = delta - 2*M_PI;
    }
    if (delta < -M_PI ) {
      delta = delta + 2*M_PI;      
    }
    ROS_INFO_STREAM(ros::Time::now() << " " << actual_goal.timepoint);
    double time_to_goal = ((execute_start_time + actual_goal.timepoint) - ros::Time::now()).toSec() ;
    
    ROS_INFO("time to goal %f " ,time_to_goal );
    double speed;
    if (time_to_goal > 0 ) { 
      speed = dist/time_to_goal ;
    } else {
     speed = 1;
    } 
    command.angular.z = 2*(sin(delta) - 0.333*sin(3*delta));
    command.angular.z = delta;
    command.linear.x = speed*(cos(delta) + 0.333*cos(3*delta));
    if (command.linear.x <0 ) {
      command.linear.x = 0;
    }
    command_publisher->publish(command);

    return false;
  }
}
