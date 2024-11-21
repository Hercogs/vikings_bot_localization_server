# vikings_bot_localization_server

<hr>

### Description
This package contains `vikings_bot` project localization related files. It uses AMCL localization method from `ROS2 NAV2` stack.

<hr>

## Installation

Download source and install dependencies:
```
cd <path/to/your/ros_ws>
git clone git@github.com:Hercogs/vikings_bot_localization_server.git src/vikings_bot_localization_server
rosdep update
rosdep install --ignore-src --default-yes --from-path src
```

Build package:
```
colcon build
source install/setup.bash
```

<hr>

### Usage

To spawn localization:
```ros2 launch vikings_bot_localization_server spawn_localization.launch.py```
#### Parameters:
- `vikings_bot_name`: namespace of robot - [vikings_bot_1 or vikings_bot_2] -> *string*, default *vikings_bot_1*
- `x_spawn_arg`: Initial x pose -> *float*, default *0.0*
- `y_spawn_arg`: Initial y pose -> *float*, default *0.0*
- `yaw_spawn_arg`: Initial yaw pose -> *float*, default *0.0*
- `use_sim`: whether to use simulated or real robot -> *bool*, default *true*



