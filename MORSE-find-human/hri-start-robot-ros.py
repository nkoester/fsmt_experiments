import subprocess

p = subprocess.Popen(['rostopic', 'pub', '-1', '/robot/motion_vw', 'geometry_msgs/Twist', "{linear: {x: .5}, angular: {z: .7}}"])
