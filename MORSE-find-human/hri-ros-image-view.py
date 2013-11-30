__author__ = 'flier'

import subprocess

p = subprocess.Popen(['rosrun', 'image_view', 'image_view', 'image:=/robot/video_cam/image'])
p.wait()

