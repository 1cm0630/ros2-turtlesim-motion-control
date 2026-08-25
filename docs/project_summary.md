# Project Summary

## Project Name

ROS2 Turtlesim Motion Control Demo

## Project Goal

This project was created to practice basic ROS2 communication and motion control using Python and turtlesim.

The main goal was to understand how ROS2 nodes communicate through topics and how velocity commands can be used to control a robot-like object.

## Main Functions

- Created a ROS2 Python package
- Built custom publisher and subscriber nodes
- Published string messages to /robot_news
- Subscribed to /robot_news and printed received messages
- Controlled turtlesim using /turtle1/cmd_vel
- Published geometry_msgs/msg/Twist velocity commands
- Implemented a simple forward-and-turn controller
- Implemented a square-like motion controller
- Used ROS2 CLI tools to inspect nodes, topics, and messages

## ROS2 Communication Structures

simple_publisher -> /robot_news -> simple_subscriber

turtle_controller -> /turtle1/cmd_vel -> turtlesim_node

turtle_square_controller -> /turtle1/cmd_vel -> turtlesim_node

## Key Technical Concepts

- ROS2 workspace
- ROS2 package
- Node
- Topic
- Publisher
- Subscriber
- Message type
- std_msgs/msg/String
- geometry_msgs/msg/Twist
- /cmd_vel velocity control
- Open-loop control
- ROS2 command line debugging

## Important Commands Used

ros2 node list
ros2 topic list
ros2 topic echo
ros2 topic info
ros2 interface show
ros2 run
colcon build

## What I Learned

Through this project, I learned that a ROS2 robot system is made of multiple nodes communicating through topics.

I also learned that /cmd_vel is a common topic used for mobile robot velocity control, and that geometry_msgs/msg/Twist contains both linear and angular velocity.

The square motion controller is based on open-loop control, which means it controls the turtle using time-based commands instead of real-time position feedback. This makes the motion simple but not perfectly accurate.

## Limitations

- The square trajectory is not perfectly accurate
- The controller does not use pose feedback
- The movement is based on time rather than position
- There is no launch file yet
- The project has not been uploaded to GitHub yet

## Future Improvements

- Use /turtle1/pose for feedback control
- Improve square trajectory accuracy
- Add launch files
- Add screenshots and demo video
- Upload the project to GitHub
- Apply similar /cmd_vel control logic to a Gazebo mobile robot simulation

## Resume Description Draft

Developed a ROS2 Python package for turtlesim motion control, including custom publisher and subscriber nodes, velocity command publishing with geometry_msgs/msg/Twist, and a square-like trajectory controller using /turtle1/cmd_vel.

Used ROS2 CLI tools such as ros2 node list, ros2 topic list, ros2 topic echo, and ros2 topic info to debug node communication and topic messages.
