import cv2
import numpy as np

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

par = cv2.aruco.DetectorParameters_create()
par.adaptiveThreshConstant = 7.0
par.adaptiveThreshWinSizeMax = 23
par.adaptiveThreshWinSizeMin = 3
par.adaptiveThreshWinSizeStep = 10
par.cornerRefinementMaxIterations = 30
par.cornerRefinementMinAccuracy = 0.1
par.cornerRefinementWinSize = 5
# par.doCornerRefinement = False
par.errorCorrectionRate = 0.6
par.markerBorderBits = 1
par.maxErroneousBitsInBorderRate = 0.35
par.maxMarkerPerimeterRate = 4.0
par.minCornerDistanceRate = 0.05
par.minDistanceToBorder = 3
par.minMarkerDistanceRate = 0.05
par.minMarkerPerimeterRate = 0.03
par.minOtsuStdDev = 5.0
par.perspectiveRemoveIgnoredMarginPerCell = 0.13
par.perspectiveRemovePixelPerCell = 4
par.polygonalApproxAccuracyRate = 0.03


def detect_markers(image):
    detections, ids, falsepos = cv2.aruco.detectMarkers(image, dictionary)

    if ids is None:
        return []

    dets = []
    for d, i in zip(detections, ids):
        dets.append((d[0],i[0]))

    return dets


def draw_markers(image, detections):
    if len(detections) > 0:
        ids = np.array([d[1] for d in detections])
        dets = [np.array([d[0]]) for d in detections]
        cv2.aruco.drawDetectedMarkers(image, dets, ids)
    return image
