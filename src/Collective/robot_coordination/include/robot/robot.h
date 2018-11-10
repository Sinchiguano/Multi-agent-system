#include "nav_msgs/Odometry.h"
#include "ros/ros.h"
#include "robot/waypoint.h"


class Robot {
  public:

    Robot();
    /** Callback function to process odometry messages.
     *  This function is called every time the nav_msgs/Odometry message is received on odom topic.
     *  */
    void odometryCallback (const nav_msgs::Odometry::ConstPtr& msg);

    /** Set the path to follow by the robot.
     *  This command rewrite the actual planned path of the robot with the Path class.
     *  */
    void setPath (std::list<Waypoint> path);

    /** The robot starts to move along the planned path.
     * The robot moves along the set of way-points using the "follow-the-carrot" control law. 
     * */
    void startExecutePath();
    /** Stop the plan execution.
     * */
    void stopExecutePath();

    /** Set the publisher created outside of the class*/
    void setCommandPublisher(ros::Publisher* pub);

    /** Create the publisher inside of the class*/
    void createCommandPublisher(ros::NodeHandle &nh);



  private:
    /** Implementation of the follow-the-carrot control law.
     * This function is to be called in the odometry callback function.
     *
     * @return true when robot finishes the plan, false otherwise.
     * */
    bool followTheCarrot ();

    ros::Publisher* command_publisher;

    ros::Time execute_start_time;

    std::list<Waypoint> plan;

    geometry_msgs::Pose robot_pose;

    double treshold;

    bool execute;

};
