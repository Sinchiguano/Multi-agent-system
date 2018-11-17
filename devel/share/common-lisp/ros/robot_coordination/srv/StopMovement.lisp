; Auto-generated. Do not edit!


(cl:in-package robot_coordination-srv)


;//! \htmlinclude StopMovement-request.msg.html

(cl:defclass <StopMovement-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass StopMovement-request (<StopMovement-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StopMovement-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StopMovement-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_coordination-srv:<StopMovement-request> is deprecated: use robot_coordination-srv:StopMovement-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StopMovement-request>) ostream)
  "Serializes a message object of type '<StopMovement-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StopMovement-request>) istream)
  "Deserializes a message object of type '<StopMovement-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StopMovement-request>)))
  "Returns string type for a service object of type '<StopMovement-request>"
  "robot_coordination/StopMovementRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StopMovement-request)))
  "Returns string type for a service object of type 'StopMovement-request"
  "robot_coordination/StopMovementRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StopMovement-request>)))
  "Returns md5sum for a message object of type '<StopMovement-request>"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StopMovement-request)))
  "Returns md5sum for a message object of type 'StopMovement-request"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StopMovement-request>)))
  "Returns full string definition for message of type '<StopMovement-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StopMovement-request)))
  "Returns full string definition for message of type 'StopMovement-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StopMovement-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StopMovement-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StopMovement-request
))
;//! \htmlinclude StopMovement-response.msg.html

(cl:defclass <StopMovement-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass StopMovement-response (<StopMovement-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StopMovement-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StopMovement-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_coordination-srv:<StopMovement-response> is deprecated: use robot_coordination-srv:StopMovement-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <StopMovement-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_coordination-srv:ack-val is deprecated.  Use robot_coordination-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StopMovement-response>) ostream)
  "Serializes a message object of type '<StopMovement-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ack) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StopMovement-response>) istream)
  "Deserializes a message object of type '<StopMovement-response>"
    (cl:setf (cl:slot-value msg 'ack) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StopMovement-response>)))
  "Returns string type for a service object of type '<StopMovement-response>"
  "robot_coordination/StopMovementResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StopMovement-response)))
  "Returns string type for a service object of type 'StopMovement-response"
  "robot_coordination/StopMovementResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StopMovement-response>)))
  "Returns md5sum for a message object of type '<StopMovement-response>"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StopMovement-response)))
  "Returns md5sum for a message object of type 'StopMovement-response"
  "8f5729177853f34b146e2e57766d4dc2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StopMovement-response>)))
  "Returns full string definition for message of type '<StopMovement-response>"
  (cl:format cl:nil "bool ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StopMovement-response)))
  "Returns full string definition for message of type 'StopMovement-response"
  (cl:format cl:nil "bool ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StopMovement-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StopMovement-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StopMovement-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StopMovement)))
  'StopMovement-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StopMovement)))
  'StopMovement-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StopMovement)))
  "Returns string type for a service object of type '<StopMovement>"
  "robot_coordination/StopMovement")