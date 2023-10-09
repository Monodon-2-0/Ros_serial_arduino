import pygame
import numpy as npm
import time
import rospy
from std_msgs.msg import Int8


# initialize pygame to start
pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

# enumerate the joysticks enable
joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

print("Initializing serial communication with the motors")
print("------------------------")
print("Press Y button to increase velocity, X button to decrease and B button for exit")
print("Only three modes developed, 3, A = 0; 4, A = 15 grades; 5, A = 30 grades")
pub = rospy.Publisher('toggle_led', Int8, queue_size=10)
rospy.init_node('talker', anonymous=True)
# obtain data about joystick
name = joystick.get_name()
axes = joystick.get_numaxes()
buttons = joystick.get_numbuttons()
hat = joystick.get_numhats()
x_acum = 3
command = 3
command_old = 3
b = 0
while b == 0:
    # call events
    event = pygame.event.get()
    # axis data
    XL = joystick.get_axis(0)
    YL = joystick.get_axis(1)
    TL = joystick.get_axis(2)
    XR = joystick.get_axis(3)
    YR = joystick.get_axis(4)
    TR = joystick.get_axis(5)
    # Buttons data
    a = joystick.get_button(0)
    b = joystick.get_button(1)
    x = joystick.get_button(2)
    y = joystick.get_button(3)
    l = joystick.get_button(4)
    r = joystick.get_button(5)
    back = joystick.get_button(6)
    start = joystick.get_button(7)
    logitec = joystick.get_button(8)
    axisl = joystick.get_button(9)
    axisr = joystick.get_button(10)
    # hat data
    arrow = joystick.get_hat(0)
    x_acum += y-x

    if y == 1 and x_acum < 6:
        command += 1
    elif y == 1 and x_acum >= 6:
        x_acum = 5
        command = x_acum
    if x == 1 and x_acum > 2:
        command -= 1
    elif x == 1 and x_acum <= 2:
        x_acum = 3
        command = x_acum
    if command_old != command:
        print(f"Mode {command} activated")
        pub.publish(command)
    command_old = command
    time.sleep(0.1)



