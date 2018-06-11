import cv2
import numpy as np

def area_of_contour(contour):
    return cv2.minAreaRect(c)
def distance_from_camera(knownWidth,focalLength, areaOfContour):
    return (knownWidth*focalLength)/areaOfContour[1][0]
def calc_focal_length(knownDistance,knownWidth,areaOfContour):
    return (areaOfContour[1][0]*knownDistance)/knownWidth

'''

Storing constants

'''
KNOWN_DISTANCE_1 = 1
KNOWN_DISTANCE_2 = 1
KNOWN_WIDTH_1 = 1
KNOWN_WIDTH_2 = 1
focal_length_1 = 1
focal_length_2 = 1