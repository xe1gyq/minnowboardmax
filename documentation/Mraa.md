# Mraa

Also knwon as libmraa, a Low Level Skeleton Library for Communication on GNU/Linux platforms

Clone, compile and install mraa 

    root@Minnowboard:~# apt-get update
    root@Minnowboard:~# apt-get install cmake
    user@Minnowboard:~$ git clone https://github.com/intel-iot-devkit/mraa.git
    user@Minnowboard:~$ mkdir mraa/build && cd $_
    user@Minnowboard:~$ cmake ..
    user@Minnowboard:~$ make
    root@Minnowboard:~# make install
    
Configure the environment to have mraa available
    
    root@Minnowboard:~# ldconfig
    root@Minnowboard:~# ldconfig -p | grep mraa
    root@Minnowboard:~# export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))
    root@Minnowboard:~$ nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))

Let's compile and execute one example

    root@Minnowboard:~# cd mraa/examples
    root@Minnowboard:~# gcc -lmraa hellomraa.c -o hellomraa
    root@Minnowboard:~# ./hellomraa
    hello mraa
     Version: v0.7.2-2-g1c4be07
     Running on MinnowBoard MAX

