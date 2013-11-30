from pymorse import Morse, MorseServicePreempted
import time


def getpos(_simu):
    pos_stream = _simu.human.pose
    pos = pos_stream.get()
    return pos


def setwyp(_waypoint, target):
    _waypoint.publish(target)


with Morse() as simu:
    waypoint = simu.human.waypoint

    setwyp(waypoint, {'x' : -2.0, 'y': -2.0, 'z': 0.0, 'tolerance' : 0.1, 'speed' : 1.0})
    curr_pos = getpos(simu)
    while curr_pos['y'] > -1.9:
        curr_pos = getpos(simu)
        time.sleep(0.1)

    setwyp(waypoint, {'x' : -1.0, 'y': -5.0, 'z': 0.0, 'tolerance' : 0.1, 'speed' : 1.0})
    curr_pos = getpos(simu)
    while curr_pos['y'] > -4.9:
        curr_pos = getpos(simu)
        time.sleep(0.1)

    setwyp(waypoint, {'x' : 0.5, 'y': -3.5, 'z': 0.0, 'tolerance' : 0.1, 'speed' : 1.0})