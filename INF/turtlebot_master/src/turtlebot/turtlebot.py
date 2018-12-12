import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rospy.numpy_msg import numpy_msg
from kobuki_msgs.msg import ButtonEvent, BumperEvent, CliffEvent, WheelDropEvent, Sound
from sensor_msgs.msg import Imu, Image, CameraInfo, PointCloud2
from cv_bridge import CvBridge, CvBridgeError
import sensor_msgs.point_cloud2 as pc2
import tf
from std_msgs.msg import Empty
import numpy as np

# Constants
topic_odom = '/odom'
topic_cmd_vel = '/cmd_vel_mux/random_walker'
topic_button_event = '/mobile_base/events/button'
topic_bumper_event = '/mobile_base/events/bumper'
topic_imu = '/mobile_base/sensors/imu_data'
topic_rgb_image = '/camera/rgb/image_raw'
topic_depth_image = '/camera/depth_registered/sw_registered/image_rect'
topic_rgb_camera_info = '/camera/rgb/camera_info'
topic_depth_camera_info = '/camera/depth/camera_info'
topic_point_cloud = '/camera/depth_registered/points'
topic_sound = '/mobile_base/commands/sound'
topic_reset_odometry = '/mobile_base/commands/reset_odometry'

max_vel_linear = 0.5
max_vel_angular = 0.5

timeout = 5.0 # 5s
node_name = 'turtlenode'

class Turtlebot(object):

    def __init__(self,
                 rgb=False,
                 depth=False,
                 pc=False):
        # init node
        rospy.init_node(node_name)

        # subscribe topics
        self.sub_odom = rospy.Subscriber(topic_odom, Odometry, self.odom_cb)
        self.sub_imu = rospy.Subscriber(topic_imu, Imu, self.imu_cb)

        # initialize sensor
        if rgb:
            self.sub_rgb = rospy.Subscriber(topic_rgb_image, Image, self.rgb_image_cb)
        if depth:
            self.sub_depth = rospy.Subscriber(topic_depth_image, Image, self.depth_image_cb)
        if pc:
            self.sub_pc = rospy.Subscriber(topic_point_cloud, PointCloud2, self.point_cloud_cb)

        # publish topics
        self.pub_cmd_vel = rospy.Publisher(topic_cmd_vel, Twist, queue_size=1)
        self.pub_reset_odometry = rospy.Publisher(topic_reset_odometry, Empty, queue_size=1)
        self.pub_sound = rospy.Publisher(topic_sound, Sound, queue_size=1)

        # get camera info
        try:
            self.rgb_camera_info = rospy.wait_for_message(topic_rgb_camera_info, CameraInfo, timeout)
        except rospy.ROSException as e:
            rospy.logerr("Unable to get RGB camera info: " + str(e))
            self.rgb_camera_info = None

        # get camera info
        try:
            self.depth_camera_info = rospy.wait_for_message(topic_depth_camera_info, CameraInfo, timeout)
        except rospy.ROSException as e:
            rospy.logerr("Unable to get depth camera info: " + str(e))
            self.depth_camera_info = None

        # initialize cv bridge
        self.bridge = CvBridge()

        # initiliaze vars
        self.odom = None
        self.imu = None
        self.rgb_msg = None
        self.depth_msg = None
        self.pc_msg = None

    def reset_odometry(self):
        t_start = rospy.get_time()
        while self.pub_reset_odometry.get_num_connections() <= 0:
            if rospy.get_time() - t_start > timeout:
                rospy.logerr("No subscriber for reset odometry, check the robot driver.")
                break

        self.pub_reset_odometry.publish(Empty())

    def odom_cb(self, msg):
        self.odom = msg

    def imu_cb(self, msg):
        self.imu = msg

    def rgb_image_cb(self, msg):
        self.rgb_msg = msg

    def depth_image_cb(self, msg):
        self.depth_msg = msg

    def point_cloud_cb(self, msg):
        self.pc_msg = msg

    def cmd_velocity(self, linear=0, angular=0):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.pub_cmd_vel.publish(msg)

    def play_sound(self, sound_id=0):
        msg = Sound()
        msg.value = max(0, min(sound_id, 6))
        self.pub_sound.publish(msg)

    def get_rgb_K(self):
        return np.array(self.rgb_camera_info.K).reshape((3,3))

    def get_depth_K(self):
        return np.array(self.depth_camera_info.K).reshape((3,3))

    def has_odometry(self):
        return self.odom is not None

    def wait_for_odometry(self):
        self.odom = None
        while not (self.has_odometry() or rospy.is_shutdown()):
            rospy.sleep(0.5)

    def get_odometry(self):
        if self.odom:
            odom = np.zeros((3))
            odom[0] = self.odom.pose.pose.position.x
            odom[1] = self.odom.pose.pose.position.y

            r, p, y = tf.transformations.euler_from_quaternion([
                self.odom.pose.pose.orientation.x,
                self.odom.pose.pose.orientation.y,
                self.odom.pose.pose.orientation.z,
                self.odom.pose.pose.orientation.w])

            odom[2] = y
            return odom
        else:
            return None

    def has_rgb_image(self):
        return self.rgb_msg is not None

    def wait_for_rgb_image(self):
        self.rgb_msg = None
        while not (self.has_rgb_image() or rospy.is_shutdown()):
            rospy.sleep(0.5)

    def get_rgb_image(self):
        if self.rgb_msg:
            try:
                cv_image = self.bridge.imgmsg_to_cv2(self.rgb_msg, "bgr8")
            except CvBridgeError as e:
                print(e)
                return None
            return cv_image
        else:
            rospy.logerr("No rgb image, did you initialize Turtlebot(rgb=True)")
            return None

    def has_depth_image(self):
        return self.depth_msg is not None

    def wait_for_depth_image(self):
        self.depth_msg = None
        while not (self.has_depth_image() or rospy.is_shutdown()):
            rospy.sleep(0.5)

    def get_depth_image(self):
        if self.depth_msg:
            try:
                cv_image = self.bridge.imgmsg_to_cv2(self.depth_msg, "passthrough")
            except CvBridgeError as e:
                print(e)
                return None
            return cv_image
        else:
            rospy.logerr("No depth image, did you initialize Turtlebot(depth=True)")
            return None

    def has_point_cloud(self):
        return self.pc_msg is not None

    def wait_for_point_cloud(self):
        self.pc_msg = None
        while not (self.has_point_cloud() or rospy.is_shutdown()):
            rospy.sleep(0.5)

    def get_point_cloud(self):
        if self.pc_msg:
            pts = list(pc2.read_points(self.pc_msg, skip_nans=False, field_names=("x", "y", "z")))

            if len(pts) == 307200:
                pc = np.array(list(pts)).reshape((480,640,3))
            elif len(pts) == 172800:
                pc = np.array(list(pts)).reshape((360,480,3))
            return pc
        else:
            rospy.logerr("No point cloud image, did you initialize Turtlebot(pc=True)")
            return None

    def register_button_event_cb(self, cb):
        self.sub_button_event = rospy.Subscriber(topic_button_event, ButtonEvent, cb)

    def register_bumper_event_cb(self, cb):
        self.sub_bumper_event = rospy.Subscriber(topic_bumper_event, BumperEvent, cb)

    def is_shutting_down(self):
        return rospy.is_shutdown()
