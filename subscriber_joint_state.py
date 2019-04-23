#!/usr/bin/env python

import rospy
import os
from socket import *

from  sensor_msgs.msg import JointState

f=open("subscriber_joint_state_output","w")

host = "10.17.73.242" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

def callback(data):
    rospy.loginfo(data.position)

    # send to xw pc
    #dataToSend = raw_input(data.position)

    result=data.position.__str__()
    UDPSock.sendto(result, addr)
    print >> f, data.position

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/joint_states',JointState, callback)
    rospy.spin()
    
if __name__ == '__main__':
    main()
f.close()


