# UPM

Sensor/Actuator repository for libmraa

    root@Minnowboard:~# apt-get update
    root@Minnowboard:~# apt-get install cmake pkg-config swig
    user@Minnowboard:~$ git clone https://github.com/intel-iot-devkit/upm.git
    user@Minnowboard:~$ cd upm
    user@Minnowboard:~$ mkdir build
    user@Minnowboard:~$ cd build
    user@Minnowboard:~$ cmake .. -DBUILDSWIGNODE=OFF
    user@Minnowboard:~$ make
    root@Minnowboard:~# make install
