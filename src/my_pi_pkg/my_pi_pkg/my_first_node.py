#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello world!")

        # タイマー機能の実装，f秒ごとにコールバック関数を実行する．
        self.create_timer(1.0, self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().info("Hello" + str(self.counter_))
        self.counter_ += 1
        

def main(args=None):
    rclpy.init(args=args) # 通信の初期化，必須
    # node = Node("py_test") # Nodeの作成

    # # Nodeが行う処理
    # for i in range(10):
    #     node.get_logger().info("Hello world!")
    
    node = MyNode()

    rclpy.spin(node) # Nodeが中断されるまで動かし続ける？
    rclpy.shutdown() # Nodeの終了，必須

if __name__=="__main__":
    main()