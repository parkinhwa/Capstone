#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>

//Filtering a PointCloud using a PassThrough filter
//http://pointclouds.org/documentation/tutorials/passthrough.php#passthrough

int
 main (int argc, char** argv)
{
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZRGB>);

  // *.PCD 파일 읽기 (https://raw.githubusercontent.com/adioshun/gitBook_Tutorial_PCL/master/Beginner/sample/tabletop.pcd)
  pcl::io::loadPCDFile<pcl::PointXYZRGB> ("noise_remove.pcd", *cloud);

  // 포인트수 출력
  std::cout << "Loaded :" << cloud->width * cloud->height  << std::endl;

  // 오브젝트 생성 
  pcl::PassThrough<pcl::PointXYZRGB> pass;
  pass.setInputCloud (cloud);                //입력 
  pass.setFilterFieldName ("z");             //적용할 좌표 축 (eg. Z축)
  pass.setFilterLimits (-10.0, 8.0);          //적용할 값 (최소, 최대 값)
  //pass.setFilterLimitsNegative (true);     //적용할 값 외 
  pass.filter (*cloud_filtered);             //필터 적용 

  // 포인트수 출력
  std::cout << "Filtered :" << cloud_filtered->width * cloud_filtered->height  << std::endl;  

  // 저장 
  pcl::io::savePCDFile<pcl::PointXYZRGB>("tabletop_passthrough.pcd", *cloud_filtered); //Default binary mode save

  return (0);
}
