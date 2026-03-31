#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoidingBot(Node):
    def __init__(self):
        super().__init__('Go_to_position_node')

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 40)

        self.subscription = self.create_subscription(
            LaserScan, '/scan', self.get_scan_values, 40)

        timer_period = 0.2
        self.timer = self.create_timer(timer_period, self.send_cmd_vel)

        self.linear_vel = 0.22

        self.regions = {'right': [], 'mid': [], 'left': []}

        self.velocity = Twist()

    def get_scan_values(self, scan_data):

        self.regions = {
            'right':   int(min(min(scan_data.ranges[0:120]), 100)),
            'mid':     int(min(min(scan_data.ranges[120:240]), 100)),
            'left':    int(min(min(scan_data.ranges[240:360]), 100)),
        }
        print(self.regions['left'], " / ",
              self.regions['mid'], " / ", self.regions['right'])

    def send_cmd_vel(self):

        self.velocity.linear.x = self.linear_vel

        if (self.regions['left'] > 4 and self.regions['mid'] > 4 and self.regions['right'] > 4):
            self.velocity.angular.z = 0.0  
            print("forward")
            
        elif (self.regions['left'] > 4 and self.regions['mid'] > 4 and self.regions['right'] < 4):
            self.velocity.angular.z = 1.57  
            print("right")
            
        elif (self.regions['left'] < 4 and self.regions['mid'] > 4 and self.regions['right'] > 4):
            self.velocity.angular.z = -1.57  
            print("left")
            
        elif (self.regions['left'] < 4 and self.regions['mid'] < 4 and self.regions['right'] < 4):
            self.velocity.angular.z = 3.14  
            print("reverse")
            
        else:
            print("some other conditions are required to be programmed")

        self.publisher.publish(self.velocity)


def main(args=None):
    rclpy.init(args=args)
    oab = ObstacleAvoidingBot()
    rclpy.spin(oab)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
