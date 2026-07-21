from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package="ujin_basic", executable="class_pub"),
        Node(package="ujin_basic", executable="class_sub"),
    ])