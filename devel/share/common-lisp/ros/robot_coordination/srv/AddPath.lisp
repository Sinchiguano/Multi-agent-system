; Auto-generated. Do not edit!


(cl:in-package robot_coordination-srv)


;//! \htmlinclude AddPath-request.msg.html

(cl:defclass <AddPath-request> (roslisp-msg-protocol:ros-message)
  ((waypoints
    :reader waypoints
    :initarg :waypoints
    :type (cl:vector robot_coordination-msg:Waypoint)
   :initform (cl:make-array 0 :element-type 'robot_coordination-msg:Waypoint :initial-element (cl:make-instance 'robot_coordination-msg:Waypoint))))
)

(cl:defclass AddPath-request (<AddPath-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddPath-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddPath-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_coordination-srv:<AddPath-request> is deprecated: use robot_coordination-srv:AddPath-request instead.")))

(cl:ensure-generic-function 'waypoints-val :lambda-list '(m))
(cl:defmethod waypoints-val ((m <AddPath-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_coordination-srv:waypoints-val is deprecated.  Use robot_coordination-srv:waypoints instead.")
  (waypoints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddPath-request>) ostream)
  "Serializes a message object of type '<AddPath-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'waypoints))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'waypoints))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddPath-request>) istream)
  "Deserializes a message object of type '<AddPath-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'waypoints) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'waypoints)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'robot_coordination-msg:Waypoint))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddPath-request>)))
  "Returns string type for a service object of type '<AddPath-request>"
  "robot_coordination/AddPathRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddPath-request)))
  "Returns string type for a service object of type 'AddPath-request"
  "robot_coordination/AddPathRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddPath-request>)))
  "Returns md5sum for a message object of type '<AddPath-request>"
  "131b0547a79043bf206c558dae4c0162")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddPath-request)))
  "Returns md5sum for a message object of type 'AddPath-request"
  "131b0547a79043bf206c558dae4c0162")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddPath-request>)))
  "Returns full string definition for message of type '<AddPath-request>"
  (cl:format cl:nil "Waypoint[] waypoints~%~%================================================================================~%MSG: robot_coordination/Waypoint~%geometry_msgs/Pose pose~%duration timepoint~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddPath-request)))
  "Returns full string definition for message of type 'AddPath-request"
  (cl:format cl:nil "Waypoint[] waypoints~%~%================================================================================~%MSG: robot_coordination/Waypoint~%geometry_msgs/Pose pose~%duration timepoint~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddPath-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'waypoints) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddPath-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AddPath-request
    (cl:cons ':waypoints (waypoints msg))
))
;//! \htmlinclude AddPath-response.msg.html

(cl:defclass <AddPath-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AddPath-response (<AddPath-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddPath-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddPath-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_coordination-srv:<AddPath-response> is deprecated: use robot_coordination-srv:AddPath-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <AddPath-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_coordination-srv:result-val is deprecated.  Use robot_coordination-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddPath-response>) ostream)
  "Serializes a message object of type '<AddPath-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddPath-response>) istream)
  "Deserializes a message object of type '<AddPath-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddPath-response>)))
  "Returns string type for a service object of type '<AddPath-response>"
  "robot_coordination/AddPathResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddPath-response)))
  "Returns string type for a service object of type 'AddPath-response"
  "robot_coordination/AddPathResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddPath-response>)))
  "Returns md5sum for a message object of type '<AddPath-response>"
  "131b0547a79043bf206c558dae4c0162")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddPath-response)))
  "Returns md5sum for a message object of type 'AddPath-response"
  "131b0547a79043bf206c558dae4c0162")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddPath-response>)))
  "Returns full string definition for message of type '<AddPath-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddPath-response)))
  "Returns full string definition for message of type 'AddPath-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddPath-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddPath-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AddPath-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AddPath)))
  'AddPath-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AddPath)))
  'AddPath-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddPath)))
  "Returns string type for a service object of type '<AddPath>"
  "robot_coordination/AddPath")