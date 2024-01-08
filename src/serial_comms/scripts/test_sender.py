#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Int8


class DataSender:
    def __init__(self):
        rospy.init_node('sender', anonymous=True)
        self.pub = rospy.Publisher('toggle_led', Int8, queue_size=10)
        while True:
            pub.publish(3)
            time.sleep(1)



if __name__ == '__main__':
    try:
        DataSender()
    except rospy.ROSInterruptException:
        pass
