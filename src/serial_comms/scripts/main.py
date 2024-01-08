#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from serial_comms.msg import position_msg


class DataReceiver:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        self.sub_pos = rospy.Subscriber("position_measured", position_msg, self.sub_pos)
        self.pub_commands = rospy.Publisher('commands', String, queue_size=10)
        while True:
            # TODO: Check if while in wait for input values it is calling the callback
            val = input("Enter your value: ")
            self.pub_commands.publish(val)
            if val == "closed":
                break

    @staticmethod
    def sub_pos(self):
         print(f"I received this information {position_msg.data}")


if __name__ == '__main__':
    try:
        DataReceiver()
    except rospy.ROSInterruptException:
        pass


