import rospy
import json
import time
from std_msgs.msg import String

start = time.time()
# print "xpos,ypos,zpos,time"

def callback(msg):
    now = time.time()
    human = msg
    human_j = json.loads(human.data)
    if len(human_j) is not 0:
        # Make this CSV'ish
        x = human_j[0]['position'][0]
        y = human_j[0]['position'][1]
        z = human_j[0]['position'][2]
        elapsed = now-start
        print "%.3f, %.3f, %.3f, %.3f" % (x,y,z,elapsed)

rospy.init_node("hri_log_human")
rospy.Subscriber("/robot/semantic", String, callback)

# This will block until you hit Ctrl+C
rospy.spin()
