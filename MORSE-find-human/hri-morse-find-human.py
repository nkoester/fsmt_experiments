from morse.builder import *


# Robot
robot = Jido()
robot.translate(x=0.8, z=0.2)

# Robot differential drive 
motion = MotionVW()
robot.append(motion)

# Waypoint actuator
waypoint = Waypoint()
robot.append(waypoint)

# Human component
human = Human()
human.translate(x=-1.0, z=0.0)
human.use_world_camera()
human.disable_keyboard_control()

# Properties for the semantic camera
human.properties(Object = True, Graspable = False, Label = "HUMAN")

# Key controls
# keyboard = Keyboard()
# keyboard.properties(Speed=3.0)
# robot.append(keyboard)

# Semantic camera
semantic = SemanticCamera()
semantic.translate(x=0.2, y=0.3, z=0.9)
robot.append(semantic)

# Middlware output
semantic.add_stream('ros')
motion.add_stream('ros')
waypoint.add_stream('ros')

# Environment
env = Environment('apartment')
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.0470, 0, 0.7854])
