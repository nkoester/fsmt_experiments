import subprocess

p = subprocess.Popen(['rostopic', 'pub', '-1', '/human/motion_human', 'geometry_msgs/Twist', "{linear: {x: .5}, angular: {z: .7}}"])
