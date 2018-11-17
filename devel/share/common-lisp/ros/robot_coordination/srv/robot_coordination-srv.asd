
(cl:in-package :asdf)

(defsystem "robot_coordination-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :robot_coordination-msg
)
  :components ((:file "_package")
    (:file "AddPath" :depends-on ("_package_AddPath"))
    (:file "_package_AddPath" :depends-on ("_package"))
    (:file "StartMovement" :depends-on ("_package_StartMovement"))
    (:file "_package_StartMovement" :depends-on ("_package"))
    (:file "StopMovement" :depends-on ("_package_StopMovement"))
    (:file "_package_StopMovement" :depends-on ("_package"))
  ))