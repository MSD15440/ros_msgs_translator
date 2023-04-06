import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Float64MultiArray, MultiArrayDimension, MultiArrayLayout

class F64ToMultiArray(Node):

    def __init__(self):
        super().__init__('f64_to_multiarray')

        self.subscriber = self.create_subscription(
            Float64,
            '/teleop_convert/f64',
            self.f64_callback,
            10
        )

        self.publisher = self.create_publisher(
            Float64MultiArray,
            '/forward_position_controller/commands',
            10
        )

    def f64_callback(self, msg):
        # Create the MultiArrayDimension object
        dim = MultiArrayDimension()
        dim.label = 'f64_data'
        dim.size = 1
        dim.stride = 1

        # Create the MultiArrayLayout object
        layout = MultiArrayLayout()
        layout.dim = [dim]
        layout.data_offset = 0

        # Create and populate the Float64MultiArray message
        multiarray_msg = Float64MultiArray()
        multiarray_msg.layout = layout
        multiarray_msg.data = [msg.data]

        # Publish the Float64MultiArray message
        self.publisher.publish(multiarray_msg)

def main(args=None):
    rclpy.init(args=args)

    node = F64ToMultiArray()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
