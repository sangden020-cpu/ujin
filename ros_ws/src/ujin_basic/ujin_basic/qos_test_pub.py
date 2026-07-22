import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import (
    QoSDurabilityPolicy,
    QoSHistoryPolicy,
    QoSReliabilityPolicy,
    QoSProfile
)


class Qos_M_Pub(Node):

    def __init__(self):
        super().__init__("message_pub")

        self.qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
        )

        self.publisher = self.create_publisher(
            String,
            "message",
            self.qos_profile
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

    node = Qos_M_Pub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()