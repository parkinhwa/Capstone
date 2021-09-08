import open3d as o3d
import numpy as np

pc = o3d.read_point_cloud("noise_remove.pcd")
o3d.visualization.draw_geometries([pc])
