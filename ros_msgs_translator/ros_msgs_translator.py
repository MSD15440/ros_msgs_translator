import sys
import importlib
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Float64MultiArray, MultiArrayDimension, MultiArrayLayout

def import_message_type(package_name, message_name):
    pkg = importlib.import_module(package_name + '.msg')
    return getattr(pkg, message_name)

class RosMsgsTranslator(Node):

    def __init__(self, input_topic, input_type, output_topic, output_type):
        super().__init__('ros_msgs_translator')

        self.output_type = output_type

        self.subscriber = self.create_subscription(
            input_type,
            input_topic,
            self.f64_callback,
            10
        )

        self.publisher = self.create_publisher(
            output_type,
            output_topic,
            10
        )

    def f64_callback(self, msg):

        # Create the MultiArrayLayout object
        layout = MultiArrayLayout()
        layout.dim = []
        layout.data_offset = 0

        # Create and populate the new message
        output_message = self.output_type()
        output_message.layout = layout
        output_message.data = [msg.data]

        # Publish the translated message
        self.publisher.publish(output_message)

def main(args=None):
    if len(sys.argv) < 5:
        print("Usage: python3 script.py <input_topic> <input_type> <output_topic> <output_type>")
        return

    input_topic = sys.argv[1]
    input_type = import_message_type('std_msgs', sys.argv[2])
    output_topic = sys.argv[3]
    output_type = import_message_type('std_msgs', sys.argv[4])

    if input_type != Float64 or output_type != Float64MultiArray:
        print("Error: Only Float64 to Float64MultiArray conversion is supported.")
        return


    rclpy.init(args=args)

    node = RosMsgsTranslator(input_topic, input_type, output_topic, output_type)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
