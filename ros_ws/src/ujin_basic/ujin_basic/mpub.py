import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class M_pub(Node):

    def __init__(self):
        super().__init__("mpub")  # 노드 이름

        # publisher 생성
        self.publish1 = self.create_publisher(
            String,
            "message1",
            10
        )
        self.publish2 = self.create_publisher(
            String,
            "message2",
            10
        )


        # 1초마다 실행
        self.timer = self.create_timer(
            1.0,
            self.pub_callback
        )

        self.count = 0


    def pub_callback(self):
        msg1 = String()
        msg2 = String()

        msg1.data = f"hello ROS2 {self.count}"
        msg2.data = f"goodbye ROS2 {self.count}"

        self.publish1.publish(msg1)
        self.publish2.publish(msg2)

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