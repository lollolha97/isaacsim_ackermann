"""
This launch file was added as part of isaacsim_ackermann.

Original package: cmdvel_to_ackermann from IsaacSim-ros_workspaces (Apache License 2.0)
See: https://github.com/isaac-sim/IsaacSim-ros_workspaces

Modifications:
- Added launch functionality for improved integration with isaacsim_ackermann.

Author: [lollolha97]
Date: [2025-03-06]
"""

import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    cmdvel_launch_file = os.path.join(
        FindPackageShare("cmdvel_to_ackermann").find("cmdvel_to_ackermann"),
        "launch",
        "cmdvel_to_ackermann.launch.py"
    )

    load_teleop_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        output='screen',
        prefix=['xterm', ' -e']
    )

    ld = LaunchDescription()
    
    ld.add_action(IncludeLaunchDescription(
        PythonLaunchDescriptionSource(cmdvel_launch_file)
    ))
    ld.add_action(load_teleop_node)

    return ld
