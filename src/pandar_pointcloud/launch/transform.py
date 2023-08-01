from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package ='pandar_pointcloud',
            node_namespace ='hesai',
            node_executable ='pandar_transform_node',
            name ='pandar_transform',
            output ="screen",
            parameters=[
                {"frame_id"  : "PandarSwift"},
                {"calibration"  : "./src/HesaiLidar_Swift_ROS/pandar_pointcloud/params/Pandar128_Correction.csv"},
                {"firetime_file"  : "./src/HesaiLidar_Swift_ROS/pandar_pointcloud/params/Pandar128_Firetimes.csv"},
                {"coordinate_correction_flag"  : False},
            ]
        )
    ])
