from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rtf_sensors',
            namespace='dps310_1',
            executable='dps310_node',
            name='dps310_1_node',
            parameters=[
                {'i2c_address': 0x77,
                 'frame_id': "dps310_1"}
                ]
            ),
        Node(
            package='rtf_sensors',
            namespace='dps310_2',
            executable='dps310_node',
            name='dps310_2_node',
            parameters=[
                {'i2c_address': 0x76,
                 'frame_id': "dps310_2"}
                ]
            )
        ])
