import rclpy
from rclpy.node import Node
from std_msgs.msg import Header


class Header_pub(Node):

    def __init__(self):
        super().__init__("header_pub")  # 노드 이름

        # publisher 생성
        self.publisher = self.create_publisher(
            Header,
            "time",
            10
        )

        # 1초마다 실행
        self.timer = self.create_timer(
            1,
            self.timer_callback
        )

        self.count = 0

    def timer_callback(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        msg.frame_id = "time test"

        self.publisher.publish(msg)

        self.get_logger().info(
            f"frame_id: {msg.frame_id}"
        )

    def pub_callback(self):
        msg = String()

        msg.data = f"hello ROS2 {self.count}"

        self.publisher.publish(msg)


        self.count += 1


def main(args=None):
    rclpy.init(args=args)

    node = Header_pub()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")

    finally:
        node.destroy_node()


if __name__ == '__main__':
    main()