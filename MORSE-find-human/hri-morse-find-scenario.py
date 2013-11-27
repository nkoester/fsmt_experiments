from morse.builder import *

# Robot
robot = BasePR2()
robot.translate(x=0.8, z=0.2)
robot.rotate(x=0.0, y=0.0, z=3.14)

# Robot differential drive 
motion = MotionVW()
robot.append(motion)

# Adding objects
box_blue = PassiveObject('props/objects','BlueToyTrashbin')
box_blue.setgraspable()
box_blue.translate(x=0.5, y=-3, z=0.0)
box_blue.rotate(z=0.2)

box_pink = PassiveObject('props/objects','PinkToyTrashbin')
box_pink.setgraspable()
box_pink.translate(x=1.5, y=-3, z=0.0)
box_pink.rotate(z=0.2)

# Properties for the semantic camera
box_blue.properties(Object = True, Graspable = False, Label = "BOX_BLUE")
box_pink.properties(Object = True, Graspable = False, Label = "BOX_PINK")

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
human.add_service('socket')

# Environment
env = Environment('apartment')
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.0470, 0, 0.7854])
