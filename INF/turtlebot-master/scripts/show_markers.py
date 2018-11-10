#!/usr/bin/env python

from turtlebot import Turtlebot, detector
import numpy as np
import cv2

WINDOW = 'markers'

def main():

    turtle = Turtlebot(rgb=True)
    cv2.namedWindow(WINDOW)

    while not turtle.is_shutting_down():
        # get point cloud
        image = turtle.get_rgb_image()

        # wait for image to be ready
        if image is None:
            continue

        # detect markers in the image
        markers = detector.detect_markers(image)

        # draw markers in the image
        detector.draw_markers(image, markers)

        # show image
        cv2.imshow(WINDOW, image)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()

