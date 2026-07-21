import rclpy
from rclpy.node import Node

def timer_callback():
    print("Hello, ROS2!")

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