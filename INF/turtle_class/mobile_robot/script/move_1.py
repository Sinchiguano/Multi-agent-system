#!/usr/bin/env python

import sys
from turtle.turtle_class import Turtlebot
import numpy as np

def main():
    while (robot.get_odometry() is None):
        print("Waiting")
    robot.reset_odometry()
    
    while (not robot.is_shutting_down()):
        

if __name__ == "__main__":
    robot=Turtlebot()
    main()
