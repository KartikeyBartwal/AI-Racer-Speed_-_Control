from Box2D.b2 import *
joint = Box2D.b2.b2RevoluteJoint()
speed_64 = np.float64(3.0)
speed_32 = np.float32(3.0)

try:
    joint.SetMotorSpeed(speed_64)
except TypeError as e:
    print("float64 failed:", e)

try:
    joint.SetMotorSpeed(speed_32)
    print("float32 worked!")
except TypeError as e:
    print("float32 also failed:", e)
