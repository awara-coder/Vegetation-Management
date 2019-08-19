import numpy as np


def depth_finder(mask, depth, func, band = False, median = True):
    depths = np.array(list())
    minDepth = 0.0
    Y = len(mask)
    X_start = 0
    X = len(mask[0])
    if band == True:
        X_start = 320 - 64
        X = 320 + 64
    for i in range(Y):
        for j in range(X_start, X):
            minDepth = max(minDepth, depth[i][j])

            # Check whether the current cell is white
            if mask[i][j] > 0 :
                np.append(depths, depth[i][j])
    if len(depths) == 0:
        return minDepth, minDepth
    depths.sort()
    if median:
        return np.median(depths), minDepth
        wireDepth = np.median(depths)
    return max(depths), minDepth