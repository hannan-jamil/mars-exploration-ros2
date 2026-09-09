# Mars Rover Simulation and Evaluation Framework

ROS 2 and Ignition Gazebo simulation framework for evaluating a six-wheeled rover in a Mars-inspired, physically interactive environment.

## Research Context

The platform integrates rover mobility, heterogeneous terrain, stereo vision, inertial sensing, and 3D LiDAR within a common ROS 2 simulation architecture.

The rover is treated as both a mobility platform and a mobile sensing element for Mars-analog surface-operation studies, including inspection, monitoring, route assessment, environmental observation, and navigation-related research.

## Main Components

### Rover

- Six-wheel rover configuration
- Explicit continuous wheel joints
- Rover mass and inertial properties
- Separate visual and collision representations
- ROS 2 TF structure
- `/cmd_vel` teleoperation

### Mars-Inspired Environment

- Mars gravity: approximately 3.73 m/s²
- Uneven terrain
- Rocks and boulders
- Heterogeneous surface appearance
- Separate visual and collision terrain meshes
- Mars-inspired lighting
- SDF-based Gazebo environment

The environment is Mars-inspired and informed by geological and visual characteristics associated with Martian rover exploration, particularly the Perseverance exploration environment at Jezero Crater. It is not intended to be an exact metric reconstruction of Jezero Crater.

## Sensors

### ZED 2i-Style Stereo Camera

Topics:

`/zed/zed_node/left/image_rect_color`

`/zed/zed_node/right/image_rect_color`

### IMU

Topic:

`/imu/data`

A stationary validation run produced a vertical acceleration response consistent with the configured Mars gravity of approximately 3.73 m/s².

### RoboSense-Style 3D LiDAR

Topic:

`/robosense/points`

Configured characteristics:

- 16 vertical channels
- 720 horizontal samples
- 360° horizontal field of view
- approximately ±15° vertical field of view
- nominal update rate of 5 Hz
- PointCloud2 output
- XYZ, intensity, and ring fields

A validated run produced approximately 4.6–4.9 Hz under the tested simulation workload.

## Software Stack

- Ubuntu Linux
- ROS 2 Humble
- Ignition Gazebo Fortress
- RViz 2
- ros_gz_bridge
- URDF/Xacro
- SDF 1.9

## Build

```bash
source /opt/ros/humble/setup.bash
cd ~/mars_exploration_ws
colcon build --symlink-install
source install/setup.bash
Run
ros2 launch mars_rover gazebo.launch.py
Main ROS 2 Topics
Motion

/cmd_vel

/joint_states

IMU

/imu/data

LiDAR

/robosense/points

Stereo Camera

/zed/zed_node/left/image_rect_color

/zed/zed_node/right/image_rect_color

TF

/tf

/tf_static

Robot Description

/robot_description

LiDAR Validation
ros2 topic hz /robosense/points
ros2 topic echo /robosense/points --once
ros2 topic info /robosense/points -v

Expected type:

sensor_msgs/msg/PointCloud2

Expected structure:

height: 16
width: 720
fields: x, y, z, intensity, ring
IMU Validation
ros2 topic hz /imu/data
ros2 topic echo /imu/data --once

Under stationary Mars-gravity conditions, the vertical acceleration should be consistent with approximately 3.73 m/s².

Camera Validation
ros2 topic hz /zed/zed_node/left/image_rect_color
ros2 topic hz /zed/zed_node/right/image_rect_color
RViz

Recommended fixed frame:

base_link

For LiDAR visualization, add a PointCloud2 display using:

/robosense/points

Research Evaluation

The framework supports controlled variation of:

gravitational acceleration
surface friction
rover mass properties
terrain configuration
obstacle distribution
sensing configuration

Candidate measurements include displacement, travel time, velocity, wheel angular velocity, pitch, roll, IMU measurements, LiDAR output, point-cloud observations, and camera output rate.

Research Positioning

A representative operational context is infrastructure inspection or surface monitoring, where the rover acts as a mobile sensing element while traversing a Mars-analog environment.

Limitations

This repository does not claim:

exact geological reconstruction of Jezero Crater
exact Martian mineral spectral properties
exact Martian illumination
exact calibration of physical laboratory sensors
direct validation of rover dynamics on Mars
proof of long-duration autonomous Mars operation

The simulated sensor configurations and environmental parameters should be interpreted as engineering approximations suitable for simulation-based research.

Reproducibility

Generated directories such as build/, install/, and log/ are intentionally excluded from version control.

Usage

See COPYRIGHT.md and ASSET_LICENSES.md for copyright and third-party asset information.

Citation

See CITATION.cff.
