from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    return LaunchDescription([

        ExecuteProcess(

            cmd=[

                'ign',

                'gazebo',

                '/home/hannan/mars_exploration_ws/src/red_planet/worlds/mars.sdf'

            ],

            output='screen'

        )

    ])
