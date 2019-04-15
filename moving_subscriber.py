#!/usr/bin/env python

import rospy
from  visualization_msgs.msg import InteractiveMarkerFeedback


def callback(data):
    x = data.pose.position.x
    y = data.pose.position.y
    z = data.pose.position.z
    rospy.loginfo('Subscribe x: {}, y: {}, z:{}'.format(x,y,z))

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/interactive_marker_server/feedback',InteractiveMarkerFeedback, callback)
    rospy.spin()
    
if __name__ == '__main__':
    main()
