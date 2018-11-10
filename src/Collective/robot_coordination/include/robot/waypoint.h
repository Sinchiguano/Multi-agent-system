#include "geometry_msgs/Pose.h"
#include "ros/ros.h"
class Waypoint {
  public:
  geometry_msgs::Pose pose;
  ros::Duration  timepoint;
  double distanceTo(geometry_msgs::Pose);
  double angleTo(geometry_msgs::Pose);
  
};
