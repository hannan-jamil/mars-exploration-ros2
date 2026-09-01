from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    rover_pkg = get_package_share_directory('mars_rover')
    world_pkg = get_package_share_directory('red_planet')

    xacro_file = os.path.join(
        rover_pkg,
        'urdf',
        'rover.urdf.xacro'
    )

    world_file = os.path.join(
        world_pkg,
        'worlds',
        'mars.sdf'
    )

    robot_description = ParameterValue(
        Command([
            'xacro ',
            xacro_file
        ]),
        value_type=str
    )

    # ---------------------------------------------------------
    # 1. GAZEBO
    # ---------------------------------------------------------

    gazebo = ExecuteProcess(
        cmd=[
            'ign',
            'gazebo',
            world_file
        ],
        output='screen'
    )

    # ---------------------------------------------------------
    # 2. ROBOT STATE PUBLISHER
    # ---------------------------------------------------------

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description
            }
        ]
    )

    # ---------------------------------------------------------
    # 3. JOINT STATE PUBLISHER
    #
    # Do NOT really need this for Gazebo physics if
    # ros2_control is providing joint states.
    # Keeping it disabled avoids two publishers fighting.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # 4. SPAWN ROBOT INTO GAZEBO
    # ---------------------------------------------------------

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'mars_rover',
            '-topic', 'robot_description',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.15'
        ],
        output='screen'
    )

    # ---------------------------------------------------------
    # 5. RVIZ
    # ---------------------------------------------------------

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    # ---------------------------------------------------------
    # 6. RQT
    # ---------------------------------------------------------

    rqt = Node(
        package='rqt_gui',
        executable='rqt_gui',
        name='rqt',
        output='screen'
    )

    # ---------------------------------------------------------
    # DELAYED ACTIONS
    # ---------------------------------------------------------

    delayed_spawn = TimerAction(
        period=5.0,
        actions=[
            spawn_robot
        ]
    )

    delayed_rviz = TimerAction(
        period=2.0,
        actions=[
            rviz
        ]
    )

    delayed_rqt = TimerAction(
        period=7.0,
        actions=[
            rqt
        ]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        delayed_rviz,
        delayed_spawn,
        delayed_rqt
    ])
