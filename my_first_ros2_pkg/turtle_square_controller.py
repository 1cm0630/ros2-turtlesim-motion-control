import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleSquareController(Node):
    def __init__(self):
        super().__init__('turtle_square_controller')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(0.5, self.control_loop)

        self.step = 0
        self.phase = 'move'
        self.side_count = 0

    def control_loop(self):
        msg = Twist()

        if self.side_count >= 4:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Square motion finished.')
            self.timer.cancel()
            return

        if self.phase == 'move':
            msg.linear.x = 1.0
            msg.angular.z = 0.0
            self.step += 1
            self.get_logger().info('Moving forward')

            if self.step >= 4:
                self.phase = 'turn'
                self.step = 0

        elif self.phase == 'turn':
            msg.linear.x = 0.0
            msg.angular.z = 1.57
            self.step += 1
            self.get_logger().info('Turning left')

            if self.step >= 2:
                self.phase = 'move'
                self.step = 0
                self.side_count += 1

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = TurtleSquareController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
