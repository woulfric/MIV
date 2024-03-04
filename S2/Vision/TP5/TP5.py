import cv2
import matplotlib.pyplot as plt 
import numpy as np

fx = np.load("mtx.npy")[0][0]
fy = np.load("mtx.npy")[1][1]

ox = np.load("mtx.npy")[0][2]
oy = np.load("mtx.npy")[1][2]

b = 3

img1= cv2.imread("img3.jpg")
img1=  cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img1 = cv2.resize(img1,(1240,800))

img2 = cv2.imread("img4.jpg")
img2=  cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img2 = cv2.resize(img2,(1240,800))


sift = cv2.SIFT_create()

# fidnding keypoints 

kp_img1, des_img1 = sift.detectAndCompute(img1,None)
kp_img2, des_img2 = sift.detectAndCompute(img2,None)

cv2.imshow("image 1", cv2.drawKeypoints(img1, kp_img1, None))
cv2.waitKey()

cv2.imshow("image 2", cv2.drawKeypoints(img2, kp_img2, None))
cv2.waitKey()
cv2.destroyAllWindows()


match = cv2.BFMatcher()
matches = match.knnMatch(des_img1,des_img2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.5*n.distance:
        good.append(m)

draw_params = dict(matchColor=(0,255,0),
                       singlePointColor=None,
                       flags=2)

img3 = cv2.drawMatches(img1,kp_img1,img2,kp_img2,good,None,**draw_params)
plt.imshow(img3), plt.show()

Coordinates = []
x = []
y = []
z = []

liste_kps1 = []
liste_kps2 = []

for point in range(len(good)) :
# for point in range(5) :
    liste_kps1.append(good[point].queryIdx)
    liste_kps2.append(good[point].trainIdx)


for i in range(len(liste_kps1)):
    ul, vl = kp_img1[liste_kps1[i]].pt[0], kp_img1[liste_kps1[i]].pt[1]
    ur, vr = kp_img2[liste_kps2[i]].pt[0], kp_img2[liste_kps2[i]].pt[1]

    d = abs(ul-ur)
    # Coordinates.append(((b*(ul-ox))/d, ((b*fx) - (ul-oy)) / (fy * d), b*fx/d))
    x.append((b* (ul-ox))/d)
    y.append(((b*fx) * (vl-oy)) / (fy * d))
    z.append(b*fx/d)
    

# print(Coordinates)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x, z, y)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')
ax.set_title('3D Scatter Plot')
plt.show()