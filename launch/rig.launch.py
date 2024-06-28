import os, yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    share_folder = get_package_share_directory('altimeter_rig_launch_files')
    launch_folder = os.path.join(share_folder, 'launch')

    #dps310
    dps310_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(launch_folder, 'dps310_double.launch.py')
        ])
    )

    # Setra
    setra_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(launch_folder, 'setra_pressure_sensor.launch.py')
        ])
    )

    return LaunchDescription([
        dps310_launch,
        setra_launch,
    ])
