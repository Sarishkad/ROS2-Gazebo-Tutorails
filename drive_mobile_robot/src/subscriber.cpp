#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
     

class SubscriberNode : public rclcpp::Node 
{
public:
    SubscriberNode() : Node("subscriber_node") 
    {
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "hello_ros2", 
            10, 
            std::bind(&SubscriberNode::data_callback, this, std::placeholders::_1)
        );

        RCLCPP_INFO(this->get_logger(), "Subscriber Node has been started.");
    }
     
private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

    void data_callback(const std_msgs::msg::String::SharedPtr msg) const
    {
        RCLCPP_INFO(this->get_logger(), "Received: '%s'", msg->data.c_str());
    }
};
     
int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SubscriberNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}