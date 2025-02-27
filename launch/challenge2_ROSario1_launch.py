#IMPORTS REQUIRED TO SET THE PACKAGE ADDRESS (DIRECTORIES)
import os
from ament_index_python.packages import get_package_share_directory

#iMPORTS REQUIRED FOR CALLING OTHER LAUNCH FILES (NESTING)
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

#IMPORTS REQUIRED TO PUSH A NAMESPACE (APPEND) A NAMESPACE TO A NESTED LAUNCH FILE
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

#INITIATE LAUNCH FILE
def generate_launch_description():

    #USER VARIABLES
    package = 'motor_control_ROSario'             #Package to be launched
    launch_file = 'challenge2_ROSario_launch.py' #Launch file to get a namespace

    group1_ns = 'group1'    #namespace to be used for group 1
    group2_ns = 'group2'    #namespace to be used for group 2
    group3_ns = 'group3'    #namespace to be used for group 3

    #Get the address of the package 
    package_directory = get_package_share_directory(package)
    #Get the address of the launch file
    launch_file_path = os.path.join(package_directory, 'launch', launch_file)
    #Set the launch file source for the group1 and group2
    launch_source1 = PythonLaunchDescriptionSource(launch_file_path)
    launch_source2 = PythonLaunchDescriptionSource(launch_file_path)
    launch_source3 = PythonLaunchDescriptionSource(launch_file_path)

    #Include the launch description for group1
    talker_listener_launch_1 = IncludeLaunchDescription(launch_source1)
    #Include the launch description for group2
    talker_listener_launch_2 = IncludeLaunchDescription(launch_source2)
    #Include the launch description for group3
    talker_listener_launch_3 = IncludeLaunchDescription(launch_source3)

    

    #SET NAMESPACE FOR ALL THE NODES INSIDE THE LAUNCH FILE
    motor_control_group1 = GroupAction(
        actions=[PushRosNamespace(group1_ns), talker_listener_launch_1,]
    )

    motor_control_group2 = GroupAction(
        actions=[PushRosNamespace(group2_ns),
                 talker_listener_launch_2,
                 ]
    )

    motor_control_group3 = GroupAction(
        actions=[PushRosNamespace(group3_ns),
                 talker_listener_launch_3,
                 ]
    )

    plot_node = Node(name="rqt_plot",
                       package='rqt_plot',
                       executable='rqt_plot',
                       output='screen',
                    )
    
    graph_node = Node(name="rqt_graph",
                       package='rqt_graph',
                       executable='rqt_graph',
                       output='screen',
                    )
    
    reconfigure_node = Node(name="rqt_reconfigure",
                       package='rqt_reconfigure',
                       executable='rqt_reconfigure',
                       output='screen',
                    )

    #LAUNCH THE DESCRIPTION
    l_d = LaunchDescription([motor_control_group1, motor_control_group2, motor_control_group3, plot_node,graph_node,reconfigure_node,])

    return l_d