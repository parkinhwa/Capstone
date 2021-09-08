import pcl
import numpy as np
import random

pc_array = np.array([[1, 2, 3], [3, 4, 5]], dtype=np.float32)
print(pc_array)

#방법 1
pc = pcl.PointCloud(pc_array)
#print(pc)

#방법 2
#pc = pcl.PointCloud()
#pc.from_array(pc_array)
#print(pc)


#방법 3 
RAND_MAX = 1.0
searchPoint = pcl.PointCloud()
searchPoints = np.zeros((1, 3), dtype=np.float32) #np.zeros((1, 4) for RGBD
searchPoints[0][0] = 1024 * random.random() / (RAND_MAX + 10.0)
searchPoints[0][1] = 1024 * random.random() / (RAND_MAX + 10.0)
searchPoints[0][2] = 1024 * random.random() / (RAND_MAX + 10.0)


#방법 4 
#p = pcl.PointCloud(10)  # "empty" point cloud
#a = np.asarray(p)       # NumPy view on the cloud
#a[:] = 0                # fill with zeros
#print(p[3])             # prints (0.0, 0.0, 0.0)
#a[:, 0] = 1             # set x coordinates to 1
#print(p[3])             # prints (1.0, 0.0, 0.0)


#방법 5 for ROS
#new_cloud = pcl.PointCloud()
#new_cloud.from_array(new_data)
#new_cloud = pcl_helper.XYZ_to_XYZRGB(new_cloud,[255,255,255])

pcl.save(pc, 'pc2pcd.pcd')
