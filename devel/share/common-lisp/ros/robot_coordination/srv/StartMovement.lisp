; Auto-generated. Do not edit!


(cl:in-package robot_coordination-srv)


;//! \htmlinclude StartMovement-request.msg.html

(cl:defclass <StartMovement-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass StartMovement-request (<StartMovement-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartMovement-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartMovement-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_coordination-srv:<StartMovement-request> is deprecated: use robot_coordination-srv:StartMovement-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartMovement-request>) ostream)
  "Serializes a message object of type '<StartMovement-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartMovement-request>) istream)
  "Deserializes a message object of type '<StartMovement-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartMovement-request>)))
  "Returns string type for a service object of type '<StartMovement-request>"
  "robot_coordination/StartMovementRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartMovement-request)))
  "Returns string type for a service object of type 'StartMovement-request"
  "robot_coordination/StartMovementRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartMovement-request>)))
  "Returns md5sum for a message object of type '<StartMovement-request>"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartMovement-request)))
  "Returns md5sum for a message object of type 'StartMovement-request"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartMovement-request>)))
  "Returns full string definition for message of type '<StartMovement-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartMovement-request)))
  "Returns full string definition for message of type 'StartMovement-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartMovement-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartMovement-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StartMovement-request
))
;//! \htmlinclude StartMovement-response.msg.html

(cl:defclass <StartMovement-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass StartMovement-response (<StartMovement-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartMovement-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartMovement-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_coordination-srv:<StartMovement-response> is deprecated: use robot_coordination-srv:StartMovement-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <StartMovement-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_coordination-srv:ack-val is deprecated.  Use robot_coordination-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartMovement-response>) ostream)
  "Serializes a message object of type '<StartMovement-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartMovement-response>) istream)
  "Deserializes a message object of type '<StartMovement-response>"
    (cl:setf (cl:slot-value msg 'ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartMovement-response>)))
  "Returns string type for a service object of type '<StartMovement-response>"
  "robot_coordination/StartMovementResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartMovement-response)))
  "Returns string type for a service object of type 'StartMovement-response"
  "robot_coordination/StartMovementResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartMovement-response>)))
  "Returns md5sum for a message object of type '<StartMovement-response>"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartMovement-response)))
  "Returns md5sum for a message object of type 'StartMovement-response"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartMovement-response>)))
  "Returns full string definition for message of type '<StartMovement-response>"
  (cl:format cl:nil "bool ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartMovement-response)))
  "Returns full string definition for message of type 'StartMovement-response"
  (cl:format cl:nil "bool ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartMovement-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartMovement-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StartMovement-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StartMovement)))
  'StartMovement-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StartMovement)))
  'StartMovement-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartMovement)))
  "Returns string type for a service object of type '<StartMovement>"
  "robot_coordination/StartMovement")