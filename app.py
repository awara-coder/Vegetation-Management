from maskGenerator import mask_generate, mask_generate_taskbar
from maskProcess import depth_finder
from time import sleep
import pickle
import cv2
import numpy as np

LOWER_BLACK = np.array([73, 9, 2])
UPPER_BLACK = np.array([138, 83, 95])
LOWER_GREEN = np.array([33, 60, 36])
UPPER_GREEN = np.array([74, 150, 113])

file = open('real_record.pkl', 'rb')
frames = pickle.load(file)
file.close()

relDeapth = []
frame_counter = 0
for frame in frames:
    frame_counter += 1
    frame_counter %= 5
    if(frame_counter != 0):
        continue
    color_frame = frame['color_image']
    depth_frame = frame['depth_image']
    # cv2.imshow('as', color_frame)
    wireMask = mask_generate(color_frame, LOWER_BLACK, UPPER_BLACK)
    vegetationMask = mask_generate(color_frame, LOWER_GREEN, UPPER_GREEN)
    wire_depth, floor_depth1 = depth_finder(wireMask, depth_frame, max)
    vegetation_depth, floor_depth2 = depth_finder(vegetationMask, depth_frame,
                                                 max, True, False)
    if floor_depth1 == wire_depth:
        wire_depth = 0
    relDeapth.append({'depth': wire_depth - vegetation_depth, 'color-image': color_frame})
    print(wire_depth - vegetation_depth)
    
    cv2.imshow('color-image', color_frame)
    cv2.imshow('wire', wireMask)
    cv2.imshow('vegetation', vegetationMask)
    cv2.waitKey(1)
    # sleep(0.0001)
    # sleep(0.03)

cv2.destroyAllWindows()

# Exporting the relative height to a csv file
out = open('real_output.pkl', 'wb')
pickle.dump(relDeapth, out)