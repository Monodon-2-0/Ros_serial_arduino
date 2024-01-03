#!/usr/bin/env python

import rospy
import socket

from std_msgs.msg import Int8

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


class Communicator:
    def __init__(self):
        self.pub = rospy.Publisher('toggle_led', Int8, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        self.receiver()

    def receiver(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    data_decoded = data.decode('utf-8')
                    print(f"Data received {data}")
                    if data_decoded.lower() == "close":
                        # send response to the client which acknowledges that the
                        # connection should be closed and break out of the loop
                        conn.sendall("closed".encode("utf-8"))
                        break
                    else:
                        conn.sendall(data)
                    self.pub.publish(int(data_decoded))
                conn.close()
            s.close()

if __name__ == '__main__':
    try:
        Communicator()
    except rospy.ROSInterruptException:
        pass
