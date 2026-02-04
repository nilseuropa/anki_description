from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    ankirobot = LaunchConfiguration("ankirobot")
    model = LaunchConfiguration("model")
    use_joint_state_publisher = LaunchConfiguration("use_joint_state_publisher")

    default_model = PathJoinSubstitution(
        [FindPackageShare("anki_description"), "urdf", "vector.xacro"]
    )

    robot_description = Command([
        "xacro ",
        model,
    ])

    return LaunchDescription(
        [
            DeclareLaunchArgument("ankirobot", default_value="vector"),
            DeclareLaunchArgument("model", default_value=default_model),
            DeclareLaunchArgument("use_joint_state_publisher", default_value="true"),
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
                condition=IfCondition(use_joint_state_publisher),
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                parameters=[{"robot_description": robot_description}],
            ),
        ]
    )
