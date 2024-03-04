import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# imgL = cv.imread('scene1.png',0)
# imgR = cv.imread('scene2.png',0)
imgL = cv.imread('1.JPG',0)
imgR = cv.imread('2.JPG',0)

# for i in range(16, 33, 16):
stereo = cv.StereoBM_create(numDisparities=16, blockSize=25)
disparity = stereo.compute(imgL,imgR)
# print(i)
plt.imshow(disparity)
plt.show()

#Parameters
#numDisparities  the disparity search range. 
#For each pixel algorithm will find the best disparity from 0 (default minimum 
#disparity) to numDisparities. The search range can then be shifted by changing 
#the minimum disparity.
#blockSize   the linear size of the blocks compared by the algorithm. 
#The size should be odd (as the block is centered at the current pixel). 
#Larger block size implies smoother, though less accurate disparity map. 
#Smaller block size gives more detailed disparity map, but there is higher chance 
#for algorithm to find a wrong correspondence.


# 16 13
# 32 9