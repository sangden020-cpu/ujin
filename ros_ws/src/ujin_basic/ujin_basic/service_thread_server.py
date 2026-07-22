import rclpy
import threading
import time
from rclpy.node import Node
from user_interface.srv import AddAndOdd
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


class Service_server(Node):
    def __init__(self):
        super().__init__("service_server") #노드 이름
        #timer 등록
        self.lock = threading.Lock()
        self.callback_group = ReentrantCallbackGroup()
        self.create_service(AddAndOdd, "add_server", self.add_callback, callback_group=self.callback_group)


    def add_callback(self, request: AddAndOdd.Request, response: AddAndOdd.Response):
        with self.lock:
            response.sum = request.inta + request.intb
        time.sleep(10)
        if response.sum % 2:
            response.odd = "Two ints sum is odd"
        else:
            response.odd = "Two ints sum is not odd"
        return response


def main(args=None):
    rclpy.init(args=args)   # rmw 활성화
    node = Service_server() #노드 생성
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")
    finally:
        executor.shutdown()
        node.destroy_node() #노드 종료

if __name__ == '__main__':
    main()