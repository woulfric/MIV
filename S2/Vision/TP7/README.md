# Stereo 3D Reconstruction

The README is divided into two parts,
1. Structure from Motion (For camera parameters and sparse reconstruction): Here, incremental structure from motion is implemented.
2. Multiview Stereo (For dense reconstruction): Will be done later.

## Structure from Motion (SfM)

### Steps to Execute

1. Clone the repository as ```git clone https://github.com/FlagArihant2000/sfm-mvs```
2. ```cd sfm-mvs```. The directory for the image directory (Line 30), along with the camera parameters (Line 16) can be updated accordingly.
3. Run ```python3 sfm.py```.
4. If executed successfully, open ```sparse.ply``` to analyse the sparse reconstruction using meshlab.

### Dataset

The dataset used is a statue of Gustav II Adolf ([Link](http://www.maths.lth.se/matematiklth/personal/calle/dataset/dataset.html)). All the images have been used for obtaining the sparse point cloud.

A sample image:
<img src="image.jpg" alt="Image" style="zoom:25%;" />



### Output

<img src="Result/result.png" alt="Image" style="zoom:50%;" />



### Team Members

1. Arihant Gaur
2. Saurabh Kemekar

IMPORTANT: Due to the lack of time, it wasn't possible to extend this project. Maybe in the near future, we would be able to optimize bundle adjustment, increase data association size, and incorporate Multiview Stereo. This is purely a project to learn and understand 3D Reconstruction of large scale data, and implement in an understandable manner, using python. Do NOT use it for research purposes. Use other incremental SfM pipelines like COLMAP.
