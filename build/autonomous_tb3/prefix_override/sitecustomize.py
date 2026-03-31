import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sarish/robotics_workspaces/ros_ws/src/install/autonomous_tb3'
