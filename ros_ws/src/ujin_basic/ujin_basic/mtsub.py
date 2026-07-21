import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from std_msgs.msg import String

class M_pub(Node):
    def __init__(self):
        super().__init__("mtsub")

        self.header_sub = self.create_subscription(
            Header,
            "time",
            self.header_callback,
            10
        )

        self.string_sub = self.create_subscription(
            String,
            "message1",
            self.string_callback,
            10
        )

    def header_callback(self, msg: Header):
        self.get_logger().info(f"frame_id: {msg.frame_id}")

    def string_callback(self, msg: String):
        self.get_logger().info(f"message: {msg.data}")

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