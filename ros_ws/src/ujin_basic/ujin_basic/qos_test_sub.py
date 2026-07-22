import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSProfile
from rclpy.qos import qos_profile_default


class M_pub(Node):
    def __init__(self):
        super().__init__("message_sub") #노드 이름
        #timer 등록

        self.qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_ALL,
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
        )
        self.subscription = self.create_subscription(String, "message", self.sub_callback, self.qos_profile)

        self.count = 0


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