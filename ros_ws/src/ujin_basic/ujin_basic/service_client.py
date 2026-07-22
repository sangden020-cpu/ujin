import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from user_interface.srv import AddAndOdd

class Service_client(Node):
    def __init__(self):
        super().__init__("service_client") #노드 이름
        self.client = self.create_client(AddAndOdd, "add_server")
        #timer 등록
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("{Service not available}")
        self.request = AddAndOdd.Request()
        self.create_timer(3.0, self.send_request)
        self.count = 0

    def send_request(self):
        self.get_logger().info(f"서버에 요청함{self.count}")
        self.request.inta = 4
        self.request.intb = 8 + self.count
        self.count += 1
        self.future = self.client.call_async(self.request)
        self.future.add_done_callback(self.done_callback)

    def done_callback(self, future):
        response = AddAndOdd.Response = future.result()
        self.get_logger().info(f"{response.sum}")
        self.get_logger().info(f"{response.odd}")

    def update(self):
        self.get_logger().info("update")

def main(args=None):
    rclpy.init(args=args)   # rmw 활성화
    node = Service_client() #노드 생성
    try:
        rclpy.spin(node) #블럭 무한루프
    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")
    finally:
        node.destroy_node() #노드 종료

if __name__ == '__main__':
    main()