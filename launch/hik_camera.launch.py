import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

serial_numbers = ['DA3302323', 'DA2584810', 'DA2419544']
nodes = []

def generate_launch_description():
    params_file = os.path.join(
        get_package_share_directory('hik_camera'), 'config', 'camera_params.yaml')

    # camera_info_url = 'package://hik_camera/config/camera_info.yaml'
    camera_info_folder_url = 'package://hik_camera/config/'

    for serial in serial_numbers:
        nodes.append(
            Node(
                package='hik_camera',
                executable='hik_camera_node',
                namespace='camera'+serial,
                output='screen',
                emulate_tty=True,
                parameters=[params_file,{
                    'Devcie_Serial_Num': serial,
                    'camera_info_url': camera_info_folder_url+'camera_info_'+serial+'.yaml',
                }],
            )
        )

    return LaunchDescription([
        DeclareLaunchArgument(name='use_sensor_data_qos',
                              default_value='false'),
        *nodes
    ])
