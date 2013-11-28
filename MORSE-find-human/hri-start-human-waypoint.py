from pymorse import Morse, MorseServicePreempted

with Morse() as simu:
    waypoint = simu.human.waypoint
    waypoint.publish({'x' : 4.0, 'y': 2.0, 'z': 0.0, 'tolerance' : 0.5, 'speed' : 1.0})