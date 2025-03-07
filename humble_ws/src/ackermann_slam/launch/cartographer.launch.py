import os
import launch
import launch_ros.actions
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, TextSubstitution
from launch.actions import DeclareLaunchArgument
from launch import LaunchDescription
from launch.conditions import IfCondition


def generate_launch_description():
    # LaunchDescription 객체 생성
    ld = LaunchDescription()

    # Declare launch arguments
    declare_rviz_cmd = DeclareLaunchArgument(
        'use_rviz',
        default_value='True',
        description='Whether to start RViz'
    )
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='True',
        description='Use simulation (Gazebo) clock if true'
    )
    declare_cartographer_config_dir_cmd = DeclareLaunchArgument(
        'cartographer_config_dir',
        default_value=os.path.join(FindPackageShare("ackermann_slam").find("ackermann_slam"), "config"),
        description='Full path to config file to load'
    )
    declare_configuration_basename_cmd = DeclareLaunchArgument(
        'configuration_basename',
        default_value='cartographer.lua',
        description='Name of lua file for cartographer'
    )
    declare_rviz_config_dir_cmd = DeclareLaunchArgument(
        'rviz_config_dir',
        default_value=os.path.join(FindPackageShare("ackermann_slam").find("ackermann_slam"), "rviz"),
        description='Full path to the RViz config file directory'
    )
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value='rviz.rviz',
        description='Full path to the RViz config file to use'
    )
    declare_resolution_cmd = DeclareLaunchArgument(
        'resolution',
        default_value='0.05',
        description='Resolution of a grid cell in the published occupancy grid'
    )
    declare_publish_period_sec_cmd = DeclareLaunchArgument(
        'publish_period_sec',
        default_value='0.5',
        description='OccupancyGrid publishing period'
    )

    # Define LaunchConfigurations
    use_rviz = LaunchConfiguration('use_rviz')
    use_sim_time = LaunchConfiguration('use_sim_time')
    cartographer_config_dir = LaunchConfiguration('cartographer_config_dir')
    configuration_basename = LaunchConfiguration('configuration_basename')
    rviz_config_dir = LaunchConfiguration('rviz_config_dir')
    rviz_config_file = LaunchConfiguration('rviz_config_file')
    resolution = LaunchConfiguration('resolution')
    publish_period_sec = LaunchConfiguration('publish_period_sec')

    # Declare and add the cartographer_node
    cartographer_node = launch_ros.actions.Node(
        package="cartographer_ros",
        executable="cartographer_node",
        name="cartographer_node",
        parameters=[{'use_sim_time': use_sim_time}],
        output="screen",
        arguments=[
            '-configuration_directory', cartographer_config_dir,
            '-configuration_basename', configuration_basename
        ]
    )

    # Declare and add the cartographer_occupancy_grid_node
    cartographer_occupancy_grid_node = launch_ros.actions.Node(
        package="cartographer_ros",
        executable="cartographer_occupancy_grid_node",
        name="cartographer_occupancy_grid_node",
        parameters=[
            {'use_sim_time': use_sim_time},
            {'resolution': resolution},
            {'publish_period_sec': publish_period_sec}
        ],
        output="screen"
    )

    # Declare and add the rviz_node with PathJoinSubstitution
    rviz_config_path = PathJoinSubstitution([rviz_config_dir, rviz_config_file])
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path],
        condition=IfCondition(use_rviz),
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # Add the actions to the launch description
    ld.add_action(declare_rviz_cmd)
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_cartographer_config_dir_cmd)
    ld.add_action(declare_configuration_basename_cmd)
    ld.add_action(declare_rviz_config_dir_cmd)
    ld.add_action(declare_rviz_config_file_cmd)
    ld.add_action(declare_resolution_cmd)
    ld.add_action(declare_publish_period_sec_cmd)
    ld.add_action(cartographer_node)
    ld.add_action(cartographer_occupancy_grid_node)
    ld.add_action(rviz_node)

    return ld  # 생성한 LaunchDescription 객체 반환