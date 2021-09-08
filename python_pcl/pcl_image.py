import numpy as np
from PIL import Image
import cv2
import pcl
import open3d

#img = cv2.imread('/home/inhwa/PCL/000000.jpg')
img_px = ('000000_rgb.jpg')
im = Image.open(img_px)
arr = []
pix = np.array(im, dtype=np.float32)
#print(im.size)
#print(pix[479][639])
h, w = im.size
print(h, w)

for i in range(w):
   for j in range(h):
       arr.append([i, j, 0])

# print(arr)
pc = pcl.PointCloud(arr)
print(pc)

pcl.save(pc, 'pc2pcd.pcd')
    
