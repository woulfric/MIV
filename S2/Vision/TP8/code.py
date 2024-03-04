import cv2
import os
import numpy as np

images_path = "images/"

images = os.listdir(images_path)

sift = cv2.SIFT_create()

bf = cv2.BFMatcher()

img_width = 1024
img_height=800

draw_params = dict(matchColor=(255, 0, 0), singlePointColor=None, flags=2)

images_reshaped = []
keypoints = []
centroids = []

for i in range(len(images)-1):
    
    img1 = cv2.imread(os.path.join(images_path, images[i]))
    img1_S = cv2.resize(img1, (img_height, img_width))
    gray1 = cv2.cvtColor(img1_S, cv2.COLOR_BGR2GRAY)   
    

    img2 = cv2.imread(os.path.join(images_path, images[i+1]))
    img2_S = cv2.resize(img2, (img_height, img_width))
    images_reshaped.append(img2_S)
    gray2 = cv2.cvtColor(img2_S, cv2.COLOR_BGR2GRAY)
    
    keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2, None) 
    keypoints.append(keypoints1)
    keypoints.append(keypoints2)

    
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)       
    good_matches = []    
    
    for m,n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    Img_match = cv2.drawMatches(img1_S, keypoints1, img2_S, keypoints2, good_matches, None, **draw_params)
    cv2.imshow("Image "+str(i)+str(i+1), Img_match)
    cv2.waitKey(0)


for i in range(len(images_reshaped)):

    kp = keypoints[i]
    x = [k.pt[0] for k in kp]
    y = [k.pt[1] for k in kp]
    centroid = (int(np.mean(x)), int(np.mean(y)))
    centroids.append(centroid)

    cv2.circle(images_reshaped[i], centroid, 2, (0, 0, 255), 2)
    cv2.putText(images_reshaped[i], "Centroid", centroid, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Image', images_reshaped[i])
    cv2.waitKey(0)

for i in range(len(images_reshaped)):
    shifted_keypoints = []

    for keypoint in keypoints[i]:
        shifted_keypoints.append(cv2.KeyPoint(keypoint.pt[0] - centroid[0], keypoint.pt[1] - centroid[1], keypoint.size, keypoint.angle, keypoint.response, keypoint.octave, keypoint.class_id))
   
    shifted_keypoints = np.array([keypoint.pt for keypoint in shifted_keypoints], dtype=np.float32)
    
    cov_mat = np.cov(shifted_keypoints, rowvar=False)
    _, eigvecs = np.linalg.eig(cov_mat)
    
    W = np.column_stack((eigvecs[:, 0], eigvecs[:, 1]))

print(W)

U, s, V = np.linalg.svd(W)