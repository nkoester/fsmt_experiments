import subprocess
import time

p = subprocess.Popen(['rostopic', 'pub', '-1', '/robot/motion_vw', 'geometry_msgs/Twist', "{linear: {x: 0.0}, angular: {z: 0.8}}"])
p.wait()
p_1 = subprocess.Popen(['rostopic', 'pub', '-1', '/robot/motion_vw', 'geometry_msgs/Twist', "{linear: {x: 0.0}, angular: {z: 0.0}}"])
p_1.wait()

