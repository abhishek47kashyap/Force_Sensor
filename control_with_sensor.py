# Abhishek Kashyap

# convert voltage variations to velocity

import rospy
from rosserial_arduino.msg import Adc
from std_msgs.msg import Float32
from sensor_msgs.msg import JointState
import numpy as np

# from numpy import interp

global sensor1, sensor2, sensor3, sensor4, outer_yaw_joint_vel
sensor1 = Float32()
sensor2 = Float32()
sensor3 = Float32()
sensor4 = Float32()
outer_yaw_joint_vel = 0.0


def ros_cd(data):
    global sensor1, sensor2, sensor3, sensor4, outer_yaw_joint_vel

    # bias_S1, bias_S2, bias_S3, bias_S4 = 2.5, 2.8, 2.8, 2.7
    bias_S1, bias_S2, bias_S3, bias_S4 = 0.0, 0.0, 0.0, 0.0

    # sensor1 = (float(data.adc0) * 5.0 / 1024.0) - bias_S1
    # sensor2 = (float(data.adc1) * 5.0 / 1024.0) - bias_S2
    # sensor3 = (float(data.adc2) * 5.0 / 1024.0) - bias_S3
    sensor4 = (float(data.adc3) * 5.0 / 1024.0) - bias_S4

    outer_yaw_joint_vel = sensor4
    # outer_yaw_joint_vel = np.interp(sensor1, [2.6, 2.9], [-1.31, 0.79]) # sensor1
    # outer_yaw_joint_vel = np.interp(sensor1, [2.70, 2.95], [-1.31, 0.79]) # sensor4

    # print "S1 = ", outer_yaw_joint_vel, ", type = ", type(outer_yaw_joint_vel)
    # print 'S1 = {}, S2 = {}, S3 = {}, S4 = {}'.format(sensor1, sensor2, sensor3, sensor4)


rospy.init_node('nodeA')
rospy.Subscriber('/adc', Adc, ros_cd, queue_size=1)

# S1 = rospy.Publisher('/sensor1', Float32, queue_size=1)
# S2 = rospy.Publisher('/sensor2', Float32, queue_size = 1)
# S3 = rospy.Publisher('/sensor3', Float32, queue_size = 1)
S4 = rospy.Publisher('/sensor4', Float32, queue_size=1)

new_state = rospy.Publisher('/joint_states', JointState, queue_size=1)

msg = JointState()
msg.name.append('right_outer_yaw_joint')
msg.position = [0.0]

rate = rospy.Rate(500)

while not rospy.is_shutdown():
    global sensor1, outer_yaw_joint_vel
    # S1.publish(sensor1)
    # S2.publish(sensor2)
    # S3.publish(sensor3)
    S4.publish(sensor4)
    # print(type(sensor1))

    #print sensor4

    if sensor4 > 2.75:   # 2.75
        if msg.position[0] < 0.79:
            msg.position[0] = msg.position[0] + (outer_yaw_joint_vel * 0.001)
        else:
            msg.position[0] = 0.79
        print "sensor value = {}, positive direction; msg.position = {}".format(sensor4, msg.position[0])

    elif sensor4 < 2.72:    # 2.70
        if msg.position[0] > -1.31:
            msg.position[0] = msg.position[0] - (outer_yaw_joint_vel * 0.001)
        else:
            msg.position[0] = -1.31

    else:
        print "sensor value = {}, Stay put". format(sensor4)


    #print "sensor value = {}, negative direction; msg.position = {}".format(sensor4, msg.position[0])

    # msg.position[0] = outer_yaw_joint_vel
    # print "msg.position = ", msg.position[0], ", sensor_value = ", sensor1

    new_state.publish(msg)
    rate.sleep()
