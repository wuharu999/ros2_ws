#!/usr/bin/env python3  
#tells the interpreter
import rclpy
from rclpy.node import Node

class myNode(Node):

    def __init__(self):
        super().__init__("first_node")    #call Node and set name of Node
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('hello' + str(self.counter))
        self.counter += 1



def main(args=None):
    rclpy.init(args = args) #initialize ros2 communications, args from init function = the one from the main
    node = myNode()
    rclpy.spin(node)    #keep comunication alive


    rclpy.shutdown()        #shut down communication

    #create a node in the program


if __name__ == '__main__':
    main()