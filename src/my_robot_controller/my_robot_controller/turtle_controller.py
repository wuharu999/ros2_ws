#!/usr/bin/env  python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose  
from geometry_msgs.msg import Twist 

class TurtleControllerNode(Node):

    def __init__(self):
        super.__init__("turtle_controller")
        self.cmd_vel_publisher = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)      #no call back
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )
        self.get_logger.info("Turtle controller started")

    def pose_callback(self, pose: Pose):    #runs as long as node is spinning
        cmd = Twist()
        ...

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()