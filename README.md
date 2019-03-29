# Anki Vector URDF #

![](doc/anki.gif)

I don't actually have one of these robots, but it sure looks like a decent piece of tech:

- It has a Quad-core Qualcomm Snapdragon processor running on 1.2GHz
- 4-microphone array
- Single point time-of-flight NIR Laser, 1m range
- 720p camera
- 802.11n Wi-Fi
- Bluetooth
- Capacitive top and bottom casing
- 4 cliff sensors

#### Model ####

- binary STL mesh as visual
- single URDF-XACRO model
- standard gazebo plugins:
  - IMU: libgazebo_ros_imu_sensor
  - Camera: libgazebo_ros_camera
  - Kinematics: libgazebo_ros_skid_steer_drive
  - Cliff sensor: libgazebo_ros_range

##### To do: #####

- add ranger
- slice mesh and create movable head and fork
- gazebo display plugin as face (?)
- wait for my birthday . . .
