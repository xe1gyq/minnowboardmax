Next Steps
==

Kernel update and installation

    user@Minnowboard:~$ uname -a
    Linux minnowboard 4.1.0-rc7+ #4 SMP ... x86_64 GNU/Linux
    user@Minnowboard:~$ cd linux
    user@Minnowboard:~$ git pull
    user@Minnowboard:~$ git checkout -b 4.1 v4.1
    Checking out files: 100% (13004/13004), done.
    Switched to a new branch '4.1'
    user@Minnowboard:~$ rm .config
    user@Minnowboard:~$ wget https://raw.githubusercontent.com/xe1gyq/minnowboardmax/master/.config
    user@Minnowboard:~$ make
    user@Minnowboard:~# make modules_install
    user@Minnowboard:~# make install
    user@Minnowboard:~# reboot
    user@Minnowboard:~$ uname -a

BIOS Configuration

Taken from http://elinux.org/Minnowboard:MaxBios#BIOS_menu

- Reboot your board and keep pressing F2




