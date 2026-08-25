import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(0.5, self.move_turtle)
        self.time_count = 0

    def move_turtle(self):
        msg = Twist()

        if self.time_count < 10:
            msg.linear.x = 1.0
            msg.angular.z = 1.0
            self.get_logger().info('Moving turtle...')
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Turtle stopped.')
            self.timer.cancel()

        self.publisher_.publish(msg)
        self.time_count += 1


def main(args=None):
    rclpy.init(args=args)

    node = TurtleController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
