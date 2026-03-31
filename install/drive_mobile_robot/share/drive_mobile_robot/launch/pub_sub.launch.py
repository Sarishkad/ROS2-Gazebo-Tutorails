from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    pub_node = Node(
        package='drive_mobile_robot',
        executable='publisher',
        name='publisher_node'
    )
    
    sub_node = Node(
        package='drive_mobile_robot',
        executable='subscriber',
        name='subscriber_node'
    )
    
    return LaunchDescription([
        pub_node,
        sub_node
    ])