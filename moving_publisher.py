#!/usr/bin/env python

import rospy
from visualization_msgs.msg import InteractiveMarkerFeedback

def talker():
    pub = rospy.Publisher('/interactive_marker_server/feedback', InteractiveMarkerFeedback, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    x = 0.4
    y = [-0.2, -0.1, 0, 0.1, 0.2]
    z = [0.1, 0.2]
    imf = InteractiveMarkerFeedback()
    #imf.header.stamp = 'now'
    imf.header.frame_id = 'base_link'
    imf.client_id = '/rviz/InteractiveMarkers'
    imf.marker_name = '/interactive_transform_publisher'
    imf.control_name = 'move_y'
    #imf.event_type = 0
    imf.pose.orientation.x = 1
    imf.pose.orientation.y = 0
    imf.pose.orientation.z = 0
    imf.pose.orientation.w = 0
    #imf.menu_entry_id = 0
    #imf.mouse_point = [0,0,0]
    #imf.mouse_point_valid = False

    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        for n in z:
            for m in y:
                imf.pose.position.x = x
                imf.pose.position.y = m
                imf.pose.position.z = n
                rospy.loginfo('Publish x: {}, y: {}, z:{}'.format(x,m,n))
                pub.publish(imf)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass