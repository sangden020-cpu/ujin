import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class M_pub(Node):
    def __init__(self):
        super().__init__("m2sub") #노드 이름
        #timer 등록
        self.create_subscription(String, "message2", self.sub_callback, 10)


    def sub_callback(self, msg: String):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)   # rmw 활성화
    node = M_pub() #노드 생성
    try:
        rclpy.spin(node) #블럭 무한루프
    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")
    finally:
        node.destroy_node() #노드 종료

if __name__ == '__main__':
    main()