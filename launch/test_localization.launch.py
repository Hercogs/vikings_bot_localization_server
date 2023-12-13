#!/usr/bin/python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    package_name = "vikings_bot_localization_server"

    robot_name = "vikings_bot_1"
    #node_name = robot_name + "_amcl"

    amcl_config = os.path.join(get_package_share_directory(package_name), "config", "test.yaml")
    #amcl_config = os.path.join(get_package_share_directory('vikings_bot_localization_server'), 'config', 'tb3_1_amcl_config.yaml')

    nav2_amcl = Node(
        #namespace=robot_name,
        package="nav2_amcl",
        executable="amcl",
        name="amcl",
        output="screen",
        parameters=[amcl_config]
    )

    # Lifecycle node
    lifecycle_node = Node(package='nav2_lifecycle_manager',
                            executable='lifecycle_manager',
                            name='nav2_amcl_lifecycle_manager',
                            output='screen',
                            parameters=[{'use_sim_time': True},
                                        {'autostart': True},
                                        {'node_names': ["amcl"]}
                            ]
    )
    
    return LaunchDescription([
        nav2_amcl,
        lifecycle_node
    ])