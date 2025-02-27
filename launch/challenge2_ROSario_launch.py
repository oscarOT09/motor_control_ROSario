from launch import LaunchDescription
from launch_ros.actions import Node
#from launch.actions import ExecuteProcess

def generate_launch_description():
    motor_node = Node(name="motor_sys_ROSario",
                       package='motor_control_ROSario',
                       executable='dc_motor_ROSario',
                       emulate_tty=True,
                       output='screen',
                       parameters=[{
                        'sample_time': 0.02,
                        'sys_gain_K': 1.75,
                        'sys_tau_T': 0.5,
                        'initial_conditions': 0.0,
                            }
                        ]
                    )
    
    sp_node = Node(name="sp_gen_ROSario",
                       package='motor_control_ROSario',
                       executable='set_point_ROSario',
                       emulate_tty=True,
                       output='screen',
                       )
    
    pid_node = Node(name="control_pid_ROSario",
                       package='motor_control_ROSario',
                       executable='control_pid_ROSario',
                       emulate_tty=True,
                       output='screen',
                       parameters=[{
                        'kp': 0.784448352257978,
                        'ki': 18.9480680587262,
                        'kd': 0.00259088726253201,
                            }
                        ]
                    )
    
    plot_node = Node(name="rqt_plot",
                       package='rqt_plot',
                       executable='rqt_plot',
                       output='screen',
                    )
    
    l_d = LaunchDescription([motor_node, sp_node, pid_node, plot_node,])
    # ExecuteProcess(cmd=['ros2', 'topic', 'echo', '/motor_speed_y_ROSario'], output='screen'),
    return l_d