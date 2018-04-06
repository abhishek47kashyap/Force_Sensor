import dvrk
import math
import PyKDL as pk
import numpy as np
# import rospy
# from rosserial_arduino.msg import Adc
#
# global sensor1, sensor2, sensor3, sensor4
# sensor1 = float()
# sensor2 = float()
# sensor3 = float()
# sensor4 = float()
#
# def data_acquisition(data):
#     global sensor1, sensor2, sensor3, sensor4
#
#     sensor1 = (float(data.adc0) * 5.0 / 1024.0)
#     sensor2 = (float(data.adc1) * 5.0 / 1024.0)
#     sensor3 = (float(data.adc2) * 5.0 / 1024.0)
#     sensor4 = (float(data.adc3) * 5.0 / 1024.0)


amplitude = 0.005  # 2 mm (SI units
a = list(range(5, 361, 5))
angles = np.array([0] + 2*a)  # angles in degrees

angles = np.reshape(angles, (np.shape(angles)[0], 1))
angles = angles * 3.14 / 180  # angles in radians

displacement_magnitude = amplitude

displacement_x = list(displacement_magnitude * np.cos(angles))
displacement_z = list(displacement_magnitude * np.sin(angles))


# move is absolute (SI units)
# dmove is relative

arm = dvrk.mtm('MTMR')
arm.dmove(pk.Vector(displacement_x[0], 0.0, displacement_z[0]))

# rospy.init_node('MTM_circular_tracking')
# rospy.Subscriber('/adc', Adc, data_acquisition, queue_size=1)

# rate = rospy.Rate(500)

# directory = "/home/davincic3/Documents/data1.csv"
#
# csv = open(directory, "w")   # "w" indicates that you're writing strings to the file
# csv.write("rospy.time, angle, sensor1, sensor2, sensor3, sensor4\n")
#
# initial_time = rospy.get_time()

for i in range(1, len(displacement_x)):
    dx = displacement_x[i] - displacement_x[i-1]
    dz = displacement_z[i] - displacement_z[i-1]

    # print "dx = {}, dz = {}".format(dx, dz)

    # t = rospy.get_time() - initial_time
    #
    # row = t + "," + angles[i]*180/3.14 + "," + sensor1 + "," + sensor2 + "," + sensor3 + "," + sensor4
    # csv.write(row)

    arm.dmove(pk.Vector(dx, 0.0, dz))



# csv.close()