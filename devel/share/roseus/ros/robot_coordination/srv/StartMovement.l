;; Auto-generated. Do not edit!


(when (boundp 'robot_coordination::StartMovement)
  (if (not (find-package "ROBOT_COORDINATION"))
    (make-package "ROBOT_COORDINATION"))
  (shadow 'StartMovement (find-package "ROBOT_COORDINATION")))
(unless (find-package "ROBOT_COORDINATION::STARTMOVEMENT")
  (make-package "ROBOT_COORDINATION::STARTMOVEMENT"))
(unless (find-package "ROBOT_COORDINATION::STARTMOVEMENTREQUEST")
  (make-package "ROBOT_COORDINATION::STARTMOVEMENTREQUEST"))
(unless (find-package "ROBOT_COORDINATION::STARTMOVEMENTRESPONSE")
  (make-package "ROBOT_COORDINATION::STARTMOVEMENTRESPONSE"))

(in-package "ROS")





(defclass robot_coordination::StartMovementRequest
  :super ros::object
  :slots ())

(defmethod robot_coordination::StartMovementRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass robot_coordination::StartMovementResponse
  :super ros::object
  :slots (_ack ))

(defmethod robot_coordination::StartMovementResponse
  (:init
   (&key
    ((:ack __ack) nil)
    )
   (send-super :init)
   (setq _ack __ack)
   self)
  (:ack
   (&optional __ack)
   (if __ack (setq _ack __ack)) _ack)
  (:serialization-length
   ()
   (+
    ;; bool _ack
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _ack
       (if _ack (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _ack
     (setq _ack (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass robot_coordination::StartMovement
  :super ros::object
  :slots ())

(setf (get robot_coordination::StartMovement :md5sum-) "8f5729177853f34b146e2e57766d4dc2")
(setf (get robot_coordination::StartMovement :datatype-) "robot_coordination/StartMovement")
(setf (get robot_coordination::StartMovement :request) robot_coordination::StartMovementRequest)
(setf (get robot_coordination::StartMovement :response) robot_coordination::StartMovementResponse)

(defmethod robot_coordination::StartMovementRequest
  (:response () (instance robot_coordination::StartMovementResponse :init)))

(setf (get robot_coordination::StartMovementRequest :md5sum-) "8f5729177853f34b146e2e57766d4dc2")
(setf (get robot_coordination::StartMovementRequest :datatype-) "robot_coordination/StartMovementRequest")
(setf (get robot_coordination::StartMovementRequest :definition-)
      "---
bool ack

")

(setf (get robot_coordination::StartMovementResponse :md5sum-) "8f5729177853f34b146e2e57766d4dc2")
(setf (get robot_coordination::StartMovementResponse :datatype-) "robot_coordination/StartMovementResponse")
(setf (get robot_coordination::StartMovementResponse :definition-)
      "---
bool ack

")



(provide :robot_coordination/StartMovement "8f5729177853f34b146e2e57766d4dc2")


