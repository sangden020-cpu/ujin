import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Move_turtle(Node):
    def __init__(self):
        super().__init__("move_turtle")  # 노드 이름
        self.pub = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )
        self.petals = 0
        self.state = 0
        self.count = 0


    def timer_callback(self):
        msg = Twist()
        if self.state == 0:

            # 원호 이동
            msg.linear.x = 2.0
            msg.angular.z = 2.0

            self.count += 1

            # 한쪽 곡선 완료
            if self.count > 25:
                self.state = 1
                self.count = 0


        elif self.state == 1:

            # 반대 방향 곡선
            msg.linear.x = 2.0
            msg.angular.z = 2.0

            self.count += 1

            # 꽃잎 하나 완료
            if self.count > 25:
                self.petals += 1
                self.count = 0

                # 다음 꽃잎 방향으로 회전
                self.state = 2


        elif self.state == 2:

            # 꽃잎 사이 회전
            msg.angular.z = 2.5

            self.count += 1

            if self.count > 10:

                self.count = 0

                if self.petals >= 6:
                    self.state = 3
                else:
                    self.state = 0


        # 종료
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0


        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = Move_turtle()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")

    finally:
        node.destroy_node()