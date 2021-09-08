import PIL.Image
import trimesh
import numpy as np
import cv2

def pointcloud(detpth, fov):
    fy = fx = 0.5 / np.tan(fov * 0.5) # assume aspectRatio is one.

    height = depth.shape[0]

    width = depth.shape[1]

    mask = np.where(depth > 0)

    x = mask[1]

    y = mask[0]

    normalized_x = (x.astype(np.float32) - width * 0.5) / width

    normalized_y = (y.astype(np.float32) - height * 0.5) / height

    world_x = normalized_x * depth[y, x] / fx

    world_y = normalized_y * depth[y, x] / fy

    world_z = depth[y, x]

    ones = np.ones(world_z.shape[0], dtype=np.float32)

    return np.vstack((world_x, world_y, world_z)).T

if __name__ == "__main__":
   # test on a simple mesh
   mesh = trimesh.load('../models/featuretype.STL')

   # scene will have automatically generated camera and lights
   scene = mesh.scene()

   # any of the automatically generated values can be overridden
   # set resolution, in pixels
   scene.camera.resolution = [480, 480]
   # set field of view, in degrees
   # make it relative to resolution so pixels per degree is same
   scene.camera.fov = 60 * (scene.camera.resolution /
                         scene.camera.resolution.max())

   # convert the camera to rays with one ray per pixel
   origin, vectors = scene.camera_rays()

   # intersects_location requires origins to be the same shape as vectors
   origins = np.tile(np.expand_dims(origin, 0), (len(vectors), 1))

   # do the actual ray- mesh queries 
   points, index_ray, index_tri = mesh.ray.intersects_location(
   origins, vectors, multiple_hits=False)
   #points, index_ray, index_tri = mesh.ray.intersects_id(
   #    origins, vectors, multiple_hits=True, return_locations=True)

   print(points[0])
   print(index_ray.shape)
   print(index_tri.shape)
   # for each hit, find the distance along its vector
   # you could also do this against the single camera Z vector
   depth = trimesh.util.diagonal_dot(points - origin,
                                  vectors[index_ray])
   # find the angular resolution, in pixels per radian
   ppr = scene.camera.resolution / np.radians(scene.camera.fov)
   # convert rays to pixel locations
   angles = scene.camera.angles()
   print('angles ',ppr)
   pixel = (angles * ppr).round().astype(np.int64)
   # make sure we are in the first quadrant
   pixel -= pixel.min(axis=0)
   # find pixel locations of actual hits
   pixel_ray = pixel[index_ray]

   # create a numpy array we can turn into an image
   # doing it with uint8 creates an `L` mode greyscale image
   a = np.zeros(scene.camera.resolution, dtype=np.uint8)

   # scale depth against range (0.0 - 1.0)
   depth_float = ((depth - depth.min()) / depth.ptp())
   print('Depth shape ', depth_float.shape)

   # convert depth into 0 - 255 uint8
   depth_int = (depth_float * 255).astype(np.uint8)
   # assign depth to correct pixel locations
   a[pixel_ray[:, 0], pixel_ray[:, 1]] = depth_int

   # create a PIL image from the depth queries
   img = PIL.Image.fromarray(a)

   img.show()
   img.save("000000.png")

   depth_img = cv2.imread('000000.png',0)
   pcl = pointcloud(depth_img, 60)
   np.savetxt('recon.xyz', pcl)
