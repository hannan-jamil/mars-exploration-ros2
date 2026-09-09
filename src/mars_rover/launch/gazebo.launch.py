from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction, SetEnvironmentVariable
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    # PACKAGE PATHS

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

   
    # GAZEBO RESOURCE PATH
   

    rover_resource_root = os.path.dirname(rover_pkg)

    existing_gz_path = os.environ.get(
        'GZ_SIM_RESOURCE_PATH',
        ''
    )

    existing_ign_path = os.environ.get(
        'IGN_GAZEBO_RESOURCE_PATH',
        ''
    )

    gz_resource_path = os.pathsep.join(
        p for p in [
            rover_resource_root,
            existing_gz_path
        ]
        if p
    )

    ign_resource_path = os.pathsep.join(
        p for p in [
            rover_resource_root,
            existing_ign_path
        ]
        if p
    )

    gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=gz_resource_path
    )

    ignition_resource_path = SetEnvironmentVariable(
        name='IGN_GAZEBO_RESOURCE_PATH',
        value=ign_resource_path
    )

   
    # ROBOT DESCRIPTION
   

    robot_description = ParameterValue(
        Command([
            'xacro ',
            xacro_file
        ]),
        value_type=str
    )

   
    # 1. GAZEBO
   

    gazebo = ExecuteProcess(
        cmd=[
            'ign',
            'gazebo',
            '-r',
            world_file
        ],
        output='screen'
    )

   
    # 2. ROBOT STATE PUBLISHER
   

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

   
    # 3. JOINT STATE PUBLISHER
   

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

   
    # 4. SPAWN ROVER
   

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'mars_rover',
            '-topic', 'robot_description',
            '-x', '20.5',
            '-y', '17.35',
            '-z', '2.15'
        ],
        output='screen'
    )

   
    # 5. ROS <-> GAZEBO CMD_VEL BRIDGE
   

    cmd_vel_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'
        ],
        output='screen'
    )

   
    # 6. ROS <-> GAZEBO BRIDGES
   

    left_camera_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/zed/zed_node/left/image_rect_color@sensor_msgs/msg/Image@gz.msgs.Image'
        ],
        output='screen'
    )

    right_camera_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/zed/zed_node/right/image_rect_color@sensor_msgs/msg/Image@gz.msgs.Image'
        ],
        output='screen'
    )   
    

    imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/imu/data@sensor_msgs/msg/Imu@gz.msgs.IMU'
        ],
        output='screen'
    )


    robosense_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/robosense/points@sensor_msgs/msg/PointCloud2@gz.msgs.PointCloudPacked'
        ],
        output='screen'
    )

    
   
    # 7. RVIZ
   

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

   
    # 8. RQT
   

    rqt = Node(
        package='rqt_gui',
        executable='rqt_gui',
        name='rqt',
        output='screen'
    )

   
    # DELAYS
   

    delayed_rviz = TimerAction(
        period=2.0,
        actions=[
            rviz
        ]
    )

    delayed_spawn = TimerAction(
        period=5.0,
        actions=[
            spawn_robot
        ]
    )

    # delayed_rqt = TimerAction(
    #     period=7.0,
    #     actions=[
    #         rqt
    #     ]
    # )

   
    # LAUNCH DESCRIPTION
   

    return LaunchDescription([
        gazebo_resource_path,
        ignition_resource_path,

        gazebo,

        robot_state_publisher,
        joint_state_publisher,

        cmd_vel_bridge,

        robosense_bridge,

        imu_bridge,
        
        left_camera_bridge,
        right_camera_bridge,

        delayed_rviz,
        delayed_spawn,
        #delayed_rqt
    ])
