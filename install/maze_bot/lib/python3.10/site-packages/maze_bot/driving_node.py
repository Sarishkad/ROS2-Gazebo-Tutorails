#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrivingNode(Node):
    def __init__(self):
        super().__init__("driving_node")

        self.publisher = self.create_publisher(Twist, "cmd_vel", 10)
        timer_period = 0.5

        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.5

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrivingNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
