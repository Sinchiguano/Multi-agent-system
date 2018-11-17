;; Auto-generated. Do not edit!


(when (boundp 'robot_coordination::StopMovement)
  (if (not (find-package "ROBOT_COORDINATION"))
    (make-package "ROBOT_COORDINATION"))
  (shadow 'StopMovement (find-package "ROBOT_COORDINATION")))
(unless (find-package "ROBOT_COORDINATION::STOPMOVEMENT")
  (make-package "ROBOT_COORDINATION::STOPMOVEMENT"))
(unless (find-package "ROBOT_COORDINATION::STOPMOVEMENTREQUEST")
  (make-package "ROBOT_COORDINATION::STOPMOVEMENTREQUEST"))
(unless (find-package "ROBOT_COORDINATION::STOPMOVEMENTRESPONSE")
  (make-package "ROBOT_COORDINATION::STOPMOVEMENTRESPONSE"))

(in-package "ROS")





(defclass robot_coordination::StopMovementRequest
  :super ros::object
  :slots ())

(defmethod robot_coordination::StopMovementRequest
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

(defclass robot_coordination::StopMovementResponse
  :super ros::object
  :slots (_ack ))

(defmethod robot_coordination::StopMovementResponse
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

(defclass robot_coordination::StopMovement
  :super ros::object
  :slots ())

(setf (get robot_coordination::StopMovement :md5sum-) "8f5729177853f34b146e2e57766d4dc2")
(setf (get robot_coordination::StopMovement :datatype-) "robot_coordination/StopMovement")
(setf (get robot_coordination::StopMovement :request) robot_coordination::StopMovementRequest)
(setf (get robot_coordination::StopMovement :response) robot_coordination::StopMovementResponse)

(defmethod robot_coordination::StopMovementRequest
  (:response () (instance robot_coordination::StopMovementResponse :init)))

(setf (get robot_coordination::StopMovementRequest :md5sum-) "8f5729177853f34b146e2e57766d4dc2")
(setf (get robot_coordination::StopMovementRequest :datatype-) "robot_coordination/StopMovementRequest")
(setf (get robot_coordination::StopMovementRequest :definition-)
      "---
bool ack

")

(setf (get robot_coordination::StopMovementResponse :md5sum-) "8f5729177853f34b146e2e57766d4dc2")
(setf (get robot_coordination::StopMovementResponse :datatype-) "robot_coordination/StopMovementResponse")
(setf (get robot_coordination::StopMovementResponse :definition-)
      "---
bool ack

")



(provide :robot_coordination/StopMovement "8f5729177853f34b146e2e57766d4dc2")


