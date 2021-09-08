#include <pcl/io/pcd_io.h>  //文件输入输出
#include <pcl/point_types.h>  //点类型相关定义
#include <pcl/visualization/cloud_viewer.h>  //点云可视化相关定义
#include <pcl/filters/statistical_outlier_removal.h>  //滤波相关
#include <pcl/common/common.h>  

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	//1.读取点云
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZRGB>);
	pcl::PCDReader r;
	r.read<pcl::PointXYZRGB>("test_save_hallway_6f.pcd", *cloud);
	cout << "there are " << cloud->points.size() << " points before filtering." << endl;

	//2.统计滤波
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filter(new pcl::PointCloud<pcl::PointXYZRGB>);
	pcl::StatisticalOutlierRemoval<pcl::PointXYZRGB> sor;
	sor.setInputCloud(cloud);
	sor.setMeanK(50); //K近邻搜索点个数
	sor.setStddevMulThresh(1.0); //标准差倍数
	sor.setNegative(false); //保留未滤波点（内点）
	sor.filter(*cloud_filter);  //保存滤波结果到cloud_filter

	//3.滤波结果保存
	pcl::PCDWriter w;
	w.writeASCII<pcl::PointXYZRGB>("noise_remove.pcd", *cloud_filter);
	cout << "there are " << cloud_filter->points.size() << " points after filtering." << endl;

	return 0;
}
