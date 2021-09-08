def do_passthrough(pcl_data,filter_axis,axis_min,axis_max):
    '''
    Create a PassThrough  object and assigns a filter axis and range.
    :param pcl_data: point could data subscriber
    :param filter_axis: filter axis
    :param axis_min: Minimum  axis to the passthrough filter object
    :param axis_max: Maximum axis to the passthrough filter object
    :return: passthrough on point cloud
    '''
    passthrough = pcl_data.make_passthrough_filter()
    passthrough.set_filter_field_name(filter_axis)
    passthrough.set_filter_limits(axis_min, axis_max)
    return passthrough.filter()


cloud = pcl.load("test_save_hallway_6f.pcd")

#filter_axis = 'x'
#axis_min = 1.0
#axis_max = 20.0
#cloud = filter.do_passthrough(cloud, filter_axis, axis_min, axis_max)

#filter_axis = 'y'
#axis_min = -7.0
#axis_max = 5.5
#cloud = filter.do_passthrough(cloud, filter_axis, axis_min, axis_max)

filter_axis = 'z'
axis_min = -1.2
axis_max = 10.0
cloud = filter.do_passthrough(cloud, filter_axis, axis_min, axis_max)

visualization3D_xyz(cloud.to_array())
