def getArea(con): # Gets the area of the contour
    return cv2.contourArea(con)

def getYcoord(con): # Gets the Y coordinate of the contour center
    M = cv2.moments(con)
    cy = int(M['m01']/M['m00'])
    return cy

def getXcoord(con): # Gets the X coordinate of the contour center
    M = cv2.moments(con)
    cy = int(M['m10']/M['m00'])
    return cy

def sortByArea(conts) : # Returns an array sorted by area from smallest to largest
    contourNum = len(conts) # Gets number of contours
    sortedBy = sorted(conts, key=getArea) # sortedBy now has all the contours sorted by area
    return sortedBy
def findBiggestContour(cnt):
    max = cv2.contourArea(cnt[0])
    maxContour = cnt[0]
    for i in cnt:
        if cv2.contourArea(i) > max:
            maxContour = i
            max = cv2.contourArea(i)
    return maxContour
