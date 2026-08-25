# Run Commands

## Build the Package

cd ~/robotics_workspace/ros2_ws
colcon build --packages-select my_first_ros2_pkg
source install/setup.bash

## Run Publisher and Subscriber Demo

Terminal 1:
ros2 run my_first_ros2_pkg simple_publisher

Terminal 2:
ros2 run my_first_ros2_pkg simple_subscriber

## Run Turtlesim

Terminal 1:
ros2 run turtlesim turtlesim_node

## Run Turtle Controller

Terminal 2:
ros2 run my_first_ros2_pkg turtle_controller

## Run Square Motion Controller

Terminal 2:
ros2 service call /reset std_srvs/srv/Empty
ros2 run my_first_ros2_pkg turtle_square_controller

## Useful Debug Commands

ros2 node list
ros2 topic list
ros2 topic echo /turtle1/cmd_vel
ros2 topic echo /turtle1/pose
ros2 topic info /turtle1/cmd_vel
ros2 interface show geometry_msgs/msg/Twist
