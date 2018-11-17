;; Auto-generated. Do not edit!


(when (boundp 'robot_coordination::AddPath)
  (if (not (find-package "ROBOT_COORDINATION"))
    (make-package "ROBOT_COORDINATION"))
  (shadow 'AddPath (find-package "ROBOT_COORDINATION")))
(unless (find-package "ROBOT_COORDINATION::ADDPATH")
  (make-package "ROBOT_COORDINATION::ADDPATH"))
(unless (find-package "ROBOT_COORDINATION::ADDPATHREQUEST")
  (make-package "ROBOT_COORDINATION::ADDPATHREQUEST"))
(unless (find-package "ROBOT_COORDINATION::ADDPATHRESPONSE")
  (make-package "ROBOT_COORDINATION::ADDPATHRESPONSE"))

(in-package "ROS")





(defclass robot_coordination::AddPathRequest
  :super ros::object
  :slots (_waypoints ))

(defmethod robot_coordination::AddPathRequest
  (:init
   (&key
    ((:waypoints __waypoints) (let (r) (dotimes (i 0) (push (instance robot_coordination::Waypoint :init) r)) r))
    )
   (send-super :init)
   (setq _waypoints __waypoints)
   self)
  (:waypoints
   (&rest __waypoints)
   (if (keywordp (car __waypoints))
       (send* _waypoints __waypoints)
     (progn
       (if __waypoints (setq _waypoints (car __waypoints)))
       _waypoints)))
  (:serialization-length
   ()
   (+
    ;; robot_coordination/Waypoint[] _waypoints
    (apply #'+ (send-all _waypoints :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robot_coordination/Waypoint[] _waypoints
     (write-long (length _waypoints) s)
     (dolist (elem _waypoints)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robot_coordination/Waypoint[] _waypoints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _waypoints (let (r) (dotimes (i n) (push (instance robot_coordination::Waypoint :init) r)) r))
     (dolist (elem- _waypoints)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass robot_coordination::AddPathResponse
  :super ros::object
  :slots (_result ))

(defmethod robot_coordination::AddPathResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass robot_coordination::AddPath
  :super ros::object
  :slots ())

(setf (get robot_coordination::AddPath :md5sum-) "131b0547a79043bf206c558dae4c0162")
(setf (get robot_coordination::AddPath :datatype-) "robot_coordination/AddPath")
(setf (get robot_coordination::AddPath :request) robot_coordination::AddPathRequest)
(setf (get robot_coordination::AddPath :response) robot_coordination::AddPathResponse)

(defmethod robot_coordination::AddPathRequest
  (:response () (instance robot_coordination::AddPathResponse :init)))

(setf (get robot_coordination::AddPathRequest :md5sum-) "131b0547a79043bf206c558dae4c0162")
(setf (get robot_coordination::AddPathRequest :datatype-) "robot_coordination/AddPathRequest")
(setf (get robot_coordination::AddPathRequest :definition-)
      "Waypoint[] waypoints

================================================================================
MSG: robot_coordination/Waypoint
geometry_msgs/Pose pose
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
---
bool result

")

(setf (get robot_coordination::AddPathResponse :md5sum-) "131b0547a79043bf206c558dae4c0162")
(setf (get robot_coordination::AddPathResponse :datatype-) "robot_coordination/AddPathResponse")
(setf (get robot_coordination::AddPathResponse :definition-)
      "Waypoint[] waypoints

================================================================================
MSG: robot_coordination/Waypoint
geometry_msgs/Pose pose
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
---
bool result

")



(provide :robot_coordination/AddPath "131b0547a79043bf206c558dae4c0162")


