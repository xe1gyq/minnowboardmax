# Kernel Compilation

__All these steps in your Minnowboard MAX__

Check your current Kernel version

    user@Minnowboard:~$ uname -a
    Linux Minnowboard A.BB.CC ...

Update and upgrade system packages and install Kernel Development packages

    root@Minnowboard:~# apt-get update
    root@Minnowboard:~# apt-get upgrade
    root@Minnowboard:~# apt-get install linux-headers-$(uname -r) kernel-package libncurses5 libncurses5-dev git

Clone, compile and install Mainline Linux Kernel

    user@Minnowboard:~$ git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
    user@Minnowboard:~$ cd linux
    user@Minnowboard:~$ make olddefconfig
    user@Minnowboard:~$ make
    root@Minnowboard:~# make modules_install
    root@Minnowboard:~# make install

Ready! Reboot the board and check again Kernel Version

    user@Minnowboard:~$ uname -a
    Linux Minnowboard X.YY.ZZ ...

## Kernel Menuconfig

    user@Minnowboard:~$ cd linux
    user@Minnowboard:~$ make menuconfig

# End of File
