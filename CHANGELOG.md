# Changelog

## Final Simulation Baseline

- Six-wheel rover model integrated into Ignition Gazebo.
- Wheel joints validated.
- Rover mass and inertial properties configured.
- Mars gravity configured at approximately 3.73 m/s².
- Mars-inspired heterogeneous terrain integrated.
- Separate visual and collision terrain representations implemented.
- Mars-inspired surface materials integrated.
- Independent rock and boulder assets integrated.
- ZED 2i-style stereo image streams integrated.
- IMU integrated and validated under Mars gravity.
- RoboSense-style 16-channel 3D LiDAR integrated.
- LiDAR PointCloud2 output validated on `/robosense/points`.
- ROS 2/Gazebo bridges integrated.
- RViz visualization integrated.
- `/cmd_vel` teleoperation interface validated.

## Known Limitations

- Terrain is Mars-inspired rather than an exact geological reconstruction.
- Sensor configurations approximate physical hardware.
- Actual sensor rates depend on simulation workload.
- Third-party visual assets require individual license verification.
