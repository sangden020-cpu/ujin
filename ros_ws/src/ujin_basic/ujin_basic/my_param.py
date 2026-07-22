import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class TParam(Node):

    def __init__(self):
        super().__init__("tparam")  # 노드 이름

        self.declare_parameter("my_param", "내가 만든 클래스 노드 안의 파라미터")
        self.my_param = self.get_parameter('my_param').get_parameter_value().string_value
        # 1초마다 실행
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.add_on_set_parameters_callback(self.parameter_callback)

    def timer_callback(self):
        self.get_logger().info(self.my_param)
    def parameter_callback(self, params: list[Parameter]):
        for param in params:
            if param.name == "my_param":
                self.my_param = param.value
        return SetParametersResult(successful=True)



def main(args=None):
    rclpy.init(args=args)

    node = TParam()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt")

    finally:
        node.destroy_node()


if __name__ == '__main__':
    main()