import os, yaml
from pathlib import Path
from datetime import datetime

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler
from launch.event_handlers import OnShutdown

bag_time = ""
def generate_launch_description():

    config_folder = os.path.join(get_package_share_directory('altimeter_rig_launch_files'), 'config')
    topics_file = os.path.join(config_folder, 'topics_to_record.yaml')

    topics_list = yaml.safe_load(open(topics_file, 'r'))["topics"]

    bag_time = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    bag_output_dir = os.path.join(Path.home(), 'data', ('rosbag2_' + bag_time))

    command = ['ros2', 'bag', 'record', '-s', 'mcap', '-o', bag_output_dir]
    command.extend(topics_list)

    rosbag_record = ExecuteProcess(
        name="rosbag_record",
        cmd=command,
        output='screen'
    )

    return LaunchDescription([
        rosbag_record
    ])
