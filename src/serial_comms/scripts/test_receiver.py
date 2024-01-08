#!/usr/bin/env python

import rospy

from serial_comms.msg import position_msg


class DataReceiver:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        self.sub_pos = rospy.Subscriber("position_measured", position_msg, self.sub_pos)
        rospy.spin()
    @staticmethod
    def sub_pos(self):
         print(f"I received this information {position_msg.data}")


if __name__ == '__main__':
    try:
        DataReceiver()
    except rospy.ROSInterruptException:
        pass


