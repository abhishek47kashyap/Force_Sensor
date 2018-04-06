import dvrk
import PyKDL as pk
import time
import math

arm = dvrk.mtm('MTMR')

# arm.home()
# arm.dmove(pk.Vector(-0.001, 0.0, 0.0))
# arm.dmove(pk.Vector(0.001, 0.0, 0.0))

# print "moving forward"
#
# for i in range(1, 41):
#     arm.dmove(pk.Vector(-0.0005, 0.0, 0.0))
#
# time.sleep(2)
#
# print "moving backward"
# for i in range(1, 41):
#     arm.dmove(pk.Vector(0.0005, 0.0, 0.0))
#
# print "movement completed"

r = pk.Rotation()
r.DoRotZ(math.pi / 6.0)
arm.dmove(r)
