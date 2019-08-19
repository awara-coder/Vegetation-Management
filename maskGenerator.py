import cv2 
import numpy as np
import matplotlib as mp



ilowH = 33
ihighH = 74
ilowS = 60
ihighS = 150
ilowV = 36
ihighV = 113


LOWER_BLACK = np.array([73, 9, 2])
UPPER_BLACK = np.array([138, 83, 95])

def mask_generate(frame, LOWER_BLACK, UPPER_BLACK):
    X = len(frame)
    Y = len(frame[0])
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvFrame, LOWER_BLACK, UPPER_BLACK)
    
    # Eroding  and dilating mask
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations = 1)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    return mask

def callback(a):
    pass
'''
cv2.namedWindow('image')


# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,180,callback)
cv2.createTrackbar('highH','image',ihighH,180,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)

'''
def mask_generate_taskbar(frame):
    X = len(frame)
    Y = len(frame[0])
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    LOWER_BLACK = np.array([ilowH, ilowS, ilowV])
    UPPER_BLACK = np.array([ihighH, ihighS, ihighV])
    mask = mask_generate(frame, LOWER_BLACK, UPPER_BLACK)
    return mask