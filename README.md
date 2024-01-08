# Ros_serial_arduino

This repository aims to communicate a host computer with an Arduino using [rosserial](http://wiki.ros.org/rosserial_arduino/Tutorials) library, the ros version used is ros noetic built with a Dockerfile.
There is a communication between topside computer and raspberry pi done via sockets.

## Dockerfile

The main dockerfile functions are:
- Install ros noetic
- Install nano 
- Copy this repository in the docker under the folder /Serial_communication/
- Source the ROS environment

docker build -f Dockerfile -t nombre_imagen .

```console
// Create the image with the Dockerfile
foo@bar:~$ docker build -f Dockerfile -t nombre_imagen .  
// Run ls dev/tty* to see the USB port of arduino. It is necessary to run network as host
foo@bar:~$ docker run -it --device=/dev/tty* --rm --net=host nombre_imagen  
// To see what containers are active ant their names
foo@bar:~$ docker ps
// To execute multiple interactive sessions
foo@bar:~$ docker exec -it container_name bash
```
## Rosserial

To start the bridge for publishers and subscribers:

```console
foo@bar:~$ rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600
foo@bar:~$ rosrun rosserial_client make_library.py ~/sketchbook/libraries position_msg
foo@bar:~$ rosrun rosserial_client make_libraries ~/Arduino/libraries serial_comms
```
To create the new library.
- Delete the ros_lib before running the command.
- In the docker run:
```console
foo@bar:~$ cd catkin_ws
foo@bar:~$ catkin_make
foo@bar:~$ source devel/setup.bash
foo@bar:~$ rosrun rosserial_arduino make_libraries.py ~/Arduino/libraries/ serial_comms
It could be also the following 
foo@bar:~$ rosrun rosserial_client  make_libraries.py ~/Arduino/libraries/ serial_comms
```
**NOTE**
Ensure that the ROS Master URI and ROS IP configuration on both the Raspberry Pi and the other computer are correctly set to enable them to communicate with each other. 
Once set up correctly, the other computer should be able to subscribe to the topic and receive the messages published by the Arduino via the Raspberry Pi.

# TODO
Check if you can use simultaneously ros and the mavlink messages. Check if you can receive and send data from/to the arduino on/from the topside computer without the need of raspberry pi, just with the Ethernet Cable. 
