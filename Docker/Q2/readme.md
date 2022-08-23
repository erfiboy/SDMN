## Simple Docker
This is the implementation of a simple version of docker with Go. This code extends [container-from-scratch](https://github.com/lizrice/containers-from-scratch) code which you can create multiple containers at the same time. In this code every container has it's own ubuntu20:04 filesystem in a separate folder in root the uid of container is a random number.

## How to Run
### Ubuntu Filesystem
First we need a ubuntu filesystem:
You can download the filesystem from [my drive](https://drive.google.com/file/d/1qaRuYevX475tSrT1GkOwnKhNSt9suoY5/view?usp=sharing) or the following instruction.
```bash
docker pull ubuntu:20.04
```
This command will pull the ubuntu:20.04 image from docker hub.

```bash
docker run ubuntu
```
```bash
docker ps
CONTAINER ID   IMAGE          COMMAND      CREATED          STATUS                      PORTS       NAMES
a25060975c97   ubuntu:20.04   "bash"       59 seconds ago   Exited (0) 58 seconds ago               inspiring_albattani
```

Now we export the filesystem of the ubuntu with the following command:
```bash
docker export -o ubuntu.tar a25060975c97
```
### Run container
and then place it in the Q2 directory.the for run the container use following command:
```bash
sudo go run container.go run <hostname> <memory>
```
replace hostname and memory (MB) with the desired values.

