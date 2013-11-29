from pymorse import Morse, MorseServicePreempted
import time


def getpos(_simu):
    pose_stream = _simu.robot.pose
    pose = pose_stream.get()
    print(pose.items())
    return pose.items()


def setpos(_waypoint, target):
    _waypoint.publish(target)

with Morse() as simu:
    waypoint = simu.human.waypoint
    setpos(waypoint, {'x' : -1.22, 'y': 0.88, 'z': 0.0, 'tolerance' : 0.3, 'speed' : 1.0})
    time.sleep(5)
    getpos(simu)
    setpos(waypoint, {'x' : -1.1, 'y': 2.6, 'z': 0.0, 'tolerance' : 0.3, 'speed' : 1.0})
    getpos(simu)
    time.sleep(5)
    setpos(waypoint, {'x' : -1.12, 'y': 1.57, 'z': 0.0, 'tolerance' : 0.3, 'speed' : 1.5})
    getpos(simu)
    time.sleep(5)
    setpos(waypoint, {'x' : -2.03, 'y': -2.616, 'z': 0.0, 'tolerance' : 0.3, 'speed' : 1.0})
    time.sleep(5)