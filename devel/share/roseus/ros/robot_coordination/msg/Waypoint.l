;; Auto-generated. Do not edit!


(when (boundp 'robot_coordination::Waypoint)
  (if (not (find-package "ROBOT_COORDINATION"))
    (make-package "ROBOT_COORDINATION"))
  (shadow 'Waypoint (find-package "ROBOT_COORDINATION")))
(unless (find-package "ROBOT_COORDINATION::WAYPOINT")
  (make-package "ROBOT_COORDINATION::WAYPOINT"))

(in-package "ROS")
;;//! \htmlinclude Waypoint.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass robot_coordination::Waypoint
  :super ros::object
  :slots (_pose _timepoint ))

(defmethod robot_coordination::Waypoint
  (:init
   (&key
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    ((:timepoint __timepoint) (instance ros::time :init))
    )
   (send-super :init)
   (setq _pose __pose)
   (setq _timepoint __timepoint)
   self)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:timepoint
   (&optional __timepoint)
   (if __timepoint (setq _timepoint __timepoint)) _timepoint)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ;; duration _timepoint
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;; duration _timepoint
       (write-long (send _timepoint :sec) s) (write-long (send _timepoint :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;; duration _timepoint
     (send _timepoint :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _timepoint :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get robot_coordination::Waypoint :md5sum-) "82b1fd005964132ed04c925157225818")
(setf (get robot_coordination::Waypoint :datatype-) "robot_coordination/Waypoint")
(setf (get robot_coordination::Waypoint :definition-)
      "geometry_msgs/Pose pose
duration timepoint


================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :robot_coordination/Waypoint "82b1fd005964132ed04c925157225818")


