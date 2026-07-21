import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def timer_callback():
    print("Hello, ROS2!")
class MessagePub(Node):

    def __init__(self):
        super().__init__("message_pub")

        self.publisher = self.create_publisher(
            String,
            "message",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f"hello ROS2 {self.count}"

        self.publisher.publish(msg)

        self.get_logger().info(
            f"publish: {msg.data}"
        )

        self.count += 1


def main(args=None):
    rclpy.init(args=args)

    node = MessagePub()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    
def main(args=None):
    rclpy.init(args=args)   # rmw 활성화
    node = Node("message_pub") #노드 이름
    node.create_timer(1.0, timer_callback) #1초마다 콜백함수 호출
    pub = node.create_publisher(String, "message", 10)

    try:
        rclpy.spin(node) #블럭 무한루프
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        node.destroy_node() #노드 종료
if __name__ == '__main__':
    main()