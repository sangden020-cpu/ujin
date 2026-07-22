import rclpy
from rclpy.node import Node
from user_interface.msg import UserInt


class MessagePub(Node):

    def __init__(self):
        super().__init__("message_pub")
        self.create_timer(
            1.0,
            timer_callback
        )

        self.publisher = self.create_publisher(
            UserInt,
            "message",
            10
        )
        def timer_callback(self):
            msg = UserInt()
            msg.header.frame_id = "time test"
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.user_int =12
            msg.user_int2 =23
            msg.user_int3 = 53
            self.pub.publish(msg)



    
def main(args=None):
    rclpy.init(args=args)   # rmw 활성화
    node = MessagePub() #노드 이름

    try:
        rclpy.spin(node) #블럭 무한루프
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        node.destroy_node() #노드 종료
if __name__ == '__main__':
    main()