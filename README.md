# ROS2 Turtlesim Motion Control Demo

## Project Overview

This project is a basic ROS2 motion control demo using Python and turtlesim.

The goal is to understand how ROS2 nodes communicate through topics and how velocity commands can control a robot-like object.

## What I Built

- Custom ROS2 publisher node
- Custom ROS2 subscriber node
- Turtlesim motion controller
- Square-like motion controller
- ROS2 topic and node inspection practice

## System Structure

simple_publisher -> /robot_news -> simple_subscriber

turtle_controller -> /turtle1/cmd_vel -> turtlesim_node

turtle_square_controller -> /turtle1/cmd_vel -> turtlesim_node

## Key ROS2 Concepts

- Workspace
- Package
- Node
- Topic
- Publisher
- Subscriber
- Message type
- std_msgs/msg/String
- geometry_msgs/msg/Twist
- /cmd_vel
- colcon build
- ros2 run
- ros2 topic echo
- ros2 node list

## Main Files

- simple_publisher.py
- simple_subscriber.py
- turtle_controller.py
- turtle_square_controller.py

## How to Build

cd ~/robotics_workspace/ros2_ws
colcon build --packages-select my_first_ros2_pkg
source install/setup.bash

## How to Run Publisher and Subscriber Demo

Terminal 1:

ros2 run my_first_ros2_pkg simple_publisher

Terminal 2:

ros2 run my_first_ros2_pkg simple_subscriber

## How to Run Turtlesim Controller

Terminal 1:

ros2 run turtlesim turtlesim_node

Terminal 2:

ros2 run my_first_ros2_pkg turtle_controller

## How to Run Square Motion Controller

Terminal 1:

ros2 run turtlesim turtlesim_node

Terminal 2:

ros2 service call /reset std_srvs/srv/Empty
ros2 run my_first_ros2_pkg turtle_square_controller

## What I Learned

- A ROS2 node is an independent running program.
- A topic is a message channel between nodes.
- A publisher sends messages to a topic.
- A subscriber receives messages from a topic.
- /cmd_vel is used to send velocity commands.
- geometry_msgs/msg/Twist contains linear and angular velocity.
- linear.x controls forward and backward movement.
- angular.z controls rotation.
- Open-loop control is simple but not perfectly accurate.

## Skills Demonstrated

- Python
- ROS2 Humble
- Linux terminal
- Publisher and subscriber nodes
- Topic debugging
- Turtlesim control
- Basic mobile robot velocity control
