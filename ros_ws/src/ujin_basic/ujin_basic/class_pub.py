import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class M_pub(Node):

    def __init__(self):
        super().__init__("message_pub")  # 노드 이름

        # publisher 생성
        self.publisher = self.create_publisher(
            String,
            "message1",
            10
        )


        # 1초마다 실행
        self.timer = self.create_timer(
            1.0,
            self.pub_callback
        )

        self.count = 0


    def pub_callback(self):
        msg = String()

        msg.data = f"hello ROS2 {self.count}"

        self.publisher.publish(msg)

        self.count += 1


def main(args=None):
    rclpy.init(args=args)

    node = M_pub()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")

    finally:
        node.destroy_node()


if __name__ == '__main__':
    main()