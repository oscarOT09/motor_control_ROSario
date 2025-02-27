import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/oscar_ot09/ros2_ws/src/motor_control_ROSario/install/motor_control_ROSario'
