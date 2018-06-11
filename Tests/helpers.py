import cv2
import numpy as np
def area_of_contour(contour):
    return cv2.minAreaRect(c)
def distance_from_camera(knownWidth,focalLength, perWidth):
    return (knownWidth*focalLength)/perWidth
def calc_focal_length(knownDistance,knownWidth,areaOfContour):
    return (areaOfContour[1][0]*knownDistance)/knownWidth

