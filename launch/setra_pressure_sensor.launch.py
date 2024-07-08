from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ads1x15_ros',
            namespace='setra',
            executable='ads1x15_node',
            name='setra_node',
            parameters=[
                {"pub_rate": 100,
                 "frame_id": 'setra'},
                ],
            )
        ])

