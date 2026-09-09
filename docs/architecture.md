# Simulation Architecture

## Overview

The workspace contains the rover simulation and Mars environment packages.

```text
ROS 2
 |
 +-- robot_state_publisher
 |
 +-- joint_state_publisher
 |
 +-- ros_gz_bridge
 |
 +-- RViz
 |
 +-- /cmd_vel
 +-- camera
 +-- IMU
 +-- LiDAR
 |
Ignition Gazebo
 |
 +-- Mars environment
 +-- rover
 +-- physics
 +-- sensors
Rover Package

mars_rover contains:

rover URDF/Xacro
wheel definitions
inertial properties
rover visual meshes
rover collision meshes
sensor definitions
launch files
ROS-Gazebo integration
Environment Packages

The environment packages contain:

Mars world SDF
terrain models
terrain collision geometry
terrain materials
rocks
boulders
environmental lighting and background
Rover Structure
base_link
 |
 +-- FL_motor_link
 |     |
 |     +-- FL_wheel_link
 |
 +-- FR_motor_link
 |     |
 |     +-- FR_wheel_link
 |
 +-- ML_motor_link
 |     |
 |     +-- ML_wheel_link
 |
 +-- MR_motor_link
 |     |
 |     +-- MR_wheel_link
 |
 +-- RL_motor_link
 |     |
 |     +-- RL_wheel_link
 |
 +-- RR_motor_link
 |     |
 |     +-- RR_wheel_link
 |
 +-- camera_link
 |
 +-- imu_link
 |
 +-- lidar_link
 |
 +-- zed_left_camera_link
 |
 +-- zed_right_camera_link
Sensor Interfaces
/zed/zed_node/left/image_rect_color
/zed/zed_node/right/image_rect_color
/imu/data
/robosense/points
Motion Interface
/cmd_vel
/joint_states
Coordinate Frames

The primary rover body frame is:

base_link

Sensor frames include:

zed_left_camera_link
zed_right_camera_link
imu_link
lidar_link

Wheel frames include:

FL_wheel_link
FR_wheel_link
ML_wheel_link
MR_wheel_link
RL_wheel_link
RR_wheel_link

