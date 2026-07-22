import os
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    param_dir = LaunchConfiguration(
        "param_dir",
        default=os.path.join(get_package_share_directory("ujin_basic"), "param", "my_param.yaml"),
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "param_dir",
                default_value=param_dir,
                description="launch parameter 를 지정하는 옵션",
            ),
            Node(
                package="ujin_basic",
                executable="my_param",
                parameters=[param_dir],
            ),
        ]
    )