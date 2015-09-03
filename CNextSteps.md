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

- Reboot your board and keep pressing F2 until you get into the BIOS menu, make sure the below configurations are set


    LPSS & SCC Devices Mode (ACPI Mod)
    PCI Mode / __ACPI Mod__

    LPSS 1 Configuration
    LPSS HSUART #1 Support
    Disable / Enable
    Note: Controls the state of Low-speed pins #6, #8, #10, #12
    LPSS HSUART #1 FlowCtrl
    Enable / Disable
    Note: This is only available when HSUART #1 is on
    LPSS HSUART #2 Support
    Disable / Enable
    Note: Controls the state of Low-speed pins #17, #19. HSUART #2 does not have hardware FlowControl due to lack of CTS/RTS lines being pulled out
    LPSS HSUART #2 FlowCtrl
    Enable / Disable
    Note: This is only available when HSUART #2 is on
    Note: Hardware Flow Control is not available, since CTS / RTS are not pulled out and available



