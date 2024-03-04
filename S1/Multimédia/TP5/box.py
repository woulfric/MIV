import cv2
import numpy as np
import math


box_coordinates = []

# mouse callback function
def draw_rect(event, x, y, flags, param):
    global box_coordinates 
    global box_coordinates2 
    if event == cv2.EVENT_LBUTTONDOWN:
        box_coordinates=[(x, y)]
        box_coordinates2 = [(x-100, y-100)] 
      
    elif event == cv2.EVENT_LBUTTONUP:
        box_coordinates.append((x, y)) 
        box_coordinates2.append((x+100, y+100)) 
        # box1
        cv2.rectangle(img, (box_coordinates[0][0], box_coordinates[0][1]), 
        (box_coordinates[1][0], box_coordinates[1][1]), (0, 0, 255), 2)
        # cv2.imshow("image", img) 
        # box2
        cv2.rectangle(img, (box_coordinates2[0][0], box_coordinates2[0][1]), 
        (box_coordinates2[1][0], box_coordinates2[1][1]), (255, 0, 0), 2)
        cv2.imshow("image", img) 
         
def slide():
    global box_coordinates 

    
    list_box1 = list(box_coordinates[0])
    list_box2 = list(box_coordinates[1])


    list_box1[0] = box_coordinates[0][0]-100
    list_box1[1] = box_coordinates[0][1]-100
    list_box2[0] = box_coordinates[0][0]-100
    list_box2[1] = box_coordinates[0][1]-100

    box_coordinates= [list_box1,list_box2]
    cv2.rectangle(grayImg2, (box_coordinates[0][0], box_coordinates[0][1]), 
             (box_coordinates[1][0], box_coordinates[1][1]), (255, 0, 0), 2)
    cv2.imshow("cropped", grayImg2)
	
img = cv2.imread("image072.png")
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)

while(True):
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
print(box_coordinates)
print(box_coordinates2)
cv2.destroyAllWindows()

img1 = cv2.imread('image072.png')
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# Cropping an image
bloc1 = grayImg1[box_coordinates[0][1]:box_coordinates[1][1], box_coordinates[0][0]:box_coordinates[1][0]] 
# Display cropped image
cv2.imshow("cropped", bloc1)
cv2.waitKey(0)

img2 = cv2.imread('image092.png')
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.rectangle(grayImg2, (box_coordinates2[0][0], box_coordinates2[0][1]), 
             (box_coordinates2[1][0], box_coordinates2[1][1]), (255, 0, 0), 2)
# cv2.imshow("cropped", grayImg2)
# slide()
cv2.waitKey(0)
bloc2 = grayImg2[box_coordinates2[0][1]:box_coordinates2[1][1], box_coordinates2[0][0]:box_coordinates2[1][0]] 


def MSE(M, N, Bloc, image):
    dif = (Bloc - image)**2
    sum = np.sum(dif)
    return 1/(M*N)*sum




bloc3=grayImg2[box_coordinates[0][1]-200:box_coordinates[1][1]+200, box_coordinates[0][0]-200:box_coordinates[1][0]+200] 

x = -(box_coordinates[0][1] - box_coordinates[1][1])
y = -(box_coordinates[0][0] - box_coordinates[1][0])

minn=math.inf 
for i in range(int(bloc3.shape[0]/x)):
    for j in range (int(bloc3.shape[1]/y)):
        if minn>MSE(x,y,bloc1,bloc3[x*i:x*(i+1),y*j:y*(j+1)]):
            minn=MSE(x,y,bloc1,bloc3[x*i:x*(i+1),y*j:y*(j+1)])
            print(minn)
            img_max=bloc3[x*i:x*(i+1),y*j:y*(j+1)]

# Display cropped image
cv2.imshow("cropped22",img_max)
cv2.waitKey(0)

    