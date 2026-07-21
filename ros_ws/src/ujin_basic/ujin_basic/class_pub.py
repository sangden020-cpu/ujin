import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class M_pub(Node):
    def __init__(self):
        super().__init__("message_pub") #노드 이름
        #timer 등록
        self.create_timer(1.0, self.timer_callback) 
        self.pub = self.create_publisher(String, "message", 10)
        self.count = 0

    def timer_callback(self):
        msg = String()  #DDS에 보낼 객체 초기화
        msg.data = f"Hello, ROS2! ({self.count})"   #DATA를 입력
        self.get_logger().info(f"Publishing: {msg.data}")
        self.pub.publish(msg)   #DDS로 보내는 기능 수행
        self.count += 1

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