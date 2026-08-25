# Resume Description

## Project Name

ROS2 Turtlesim Motion Control Demo

## One-line Description

Developed a ROS2 Python package for basic robot motion control using publisher/subscriber communication and velocity command topics.

## Resume Bullet Points

- Developed a ROS2 Python package for turtlesim motion control, including custom publisher and subscriber nodes using rclpy and std_msgs/msg/String.
- Implemented velocity command publishing with geometry_msgs/msg/Twist to control turtlesim through /turtle1/cmd_vel.
- Built a square-like trajectory controller by combining forward motion and rotation commands with time-based open-loop control.
- Used ROS2 CLI tools, including ros2 node list, ros2 topic list, ros2 topic echo, and ros2 topic info, to inspect node communication and debug topic messages.
- Documented build steps, run commands, system structure, and project limitations in README and supporting documentation.

## Skills Used

- ROS2 Humble
- Python
- Linux
- rclpy
- Publisher / Subscriber
- Topic communication
- geometry_msgs/msg/Twist
- std_msgs/msg/String
- /cmd_vel velocity control
- Turtlesim
- Git
- Markdown documentation

## Interview Explanation

This project helped me understand the core communication model of ROS2. I created custom publisher and subscriber nodes, then extended the package to control turtlesim using velocity commands.

The controller publishes Twist messages to /turtle1/cmd_vel, allowing the turtle to move forward, rotate, and follow a square-like trajectory.

The project uses open-loop control, so the motion is based on time rather than real-time pose feedback. This means the square trajectory is not perfectly accurate.

A future improvement would be to subscribe to /turtle1/pose and implement feedback-based control.
