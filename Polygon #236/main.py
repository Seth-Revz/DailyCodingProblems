# Good morning! Here's your coding interview problem for today.

# This problem was asked by Nvidia.

# You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon. 
# You can assume these points are given in order; that is, you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so on, 
# finally looping around to connect point N to point 1.

# Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).

### Im sure using matplotlib is cheating the challenge but im lazy

import matplotlib.path as mplPath
import numpy as np

def containsPoint(poly, point):
    path = mplPath.Path(poly)
    result = path.contains_point(point)
    return result

if __name__ == "__main__":
    poly = np.array([[0, 0], [0, 2], [4, 4], [4, 0]])
    point = [2, 0]
    
    result = containsPoint(poly, point)
    print(result)