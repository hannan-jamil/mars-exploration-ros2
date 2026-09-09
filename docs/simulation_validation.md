# Simulation Validation

## Rover

- Rover successfully spawns in Gazebo.
- Six wheel joints are present.
- Wheel rotation has been manually validated.
- `/cmd_vel` teleoperation has been validated.
- Rover TF structure is generated.

## Mars Physics

Configured gravity:

```text
3.73 m/s²
IMU

Topic:

/imu/data

A stationary validation run produced approximately:

linear_acceleration.z ≈ 3.73 m/s²

Observed output rate in a tested run:

approximately 23–24 Hz

under the tested simulation workload.

Stereo Camera

Topics:

/zed/zed_node/left/image_rect_color
/zed/zed_node/right/image_rect_color

Observed rates in tested runs were approximately:

15–17 Hz

under simulation load.

LiDAR

Topic:

/robosense/points

Type:

sensor_msgs/msg/PointCloud2

Cloud structure:

height: 16
width: 720

Fields:

x
y
z
intensity
ring

Configured rate:

5 Hz

Validated measured rate:

approximately 4.6–4.9 Hz

Frame:

lidar_link
Known Runtime Limitations
Sensor rates depend on simulation load.
The KDL parser may warn about inertia specified on the root link.
Graphics warnings may occur depending on the host GPU/rendering environment.
Complex mesh collision can increase physics-engine computational load.
