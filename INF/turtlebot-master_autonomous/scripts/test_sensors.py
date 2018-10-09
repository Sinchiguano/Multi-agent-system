
from turtlebot import Turtlebot

turtle = Turtlebot()
turtle.wait_for_odometry()
print "Odometry: ", turtle.get_odometry()


turtle = Turtlebot(rgb=True)
turtle.wait_for_rgb_image()
rgb = turtle.get_rgb_image()
print "RGB shape: ", str(rgb.shape)
print "RGB at 20,20: ", rgb[20,20,:]


turtle = Turtlebot(depth=True)
turtle.wait_for_depth_image()
depth =  turtle.get_depth_image()
print "Depth shape: ", str(depth.shape)
print "Depth at 20,20:", depth[20,20]


turtle = Turtlebot(pc=True)
turtle.wait_for_point_cloud()
pc = turtle.get_point_cloud()
print "PointCloud shape: ", str(pc.shape)
print "Point at 20,20: ", pc[20,20,:]
