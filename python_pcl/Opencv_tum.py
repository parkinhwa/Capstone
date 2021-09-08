import open3d as o3d
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Read TUM dataset")
    color_raw = o3d.io.read_image(
        "000000_rgb.png")
    depth_raw = o3d.io.read_image(
        "000000_depth.png")
    rgbd_image = o3d.geometry.create_rgbd_image_from_tum_format(
        color_raw, depth_raw, convert_rgb_to_intensity=False)
    print(rgbd_image)
    #plt.subplot(1, 2, 1)
    #plt.title('TUM grayscale image')
    #plt.imshow(rgbd_image.color)
    #plt.subplot(1, 2, 2)
    #plt.title('TUM depth image')
    #plt.imshow(rgbd_image.depth)
    #plt.show()
    pcd = o3d.geometry.create_point_cloud_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
           o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.write_point_cloud("./000000.pcd", pcd)
    o3d.visualization.draw_geometries([pcd])



