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
foo@bar:~$ rosrun rosserial_python serial_node.py /dev/tty*
```


