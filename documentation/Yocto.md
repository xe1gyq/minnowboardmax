Yocto
==

    user@host:~$ mkdir source
    user@host:~$ cd source
    user@host:~$ git clone -b fido git://git.yoctoproject.org/poky
    user@host:~$ cd poky
    user@host:~$ git clone -b fido git://git.yoctoproject.org/meta-intel
    user@host:~$ source oe-init-build-env yocto-x86-minnowmax
    user@host:~$ bitbake-layers add-layer "$HOME/source/poky/meta-intel"
    user@host:~$ echo 'MACHINE = "intel-corei7-64"' >> conf/local.conf
    user@host:~$ bitbake core-image-minimal
    user@host:~$ ls tmp/deploy/images/intel-corei7-64/
    ...
    core-image-minimal-intel-corei7-64.hddimg
    $ sudo $HOME/source/poky/scripts/contrib/mkefidisk.sh HOST_DEVICE \
    tmp/deploy/images/intel-corei7-64/core-image-minimal-intel-corei7-64.hddimg \
    TARGET_DEVICE

## Links

- http://elinux.org/Minnowboard:MinnowMaxYoctoProject
- http://wiki.minnowboard.org/Yocto_Project
- http://wiki.minnowboard.org/Projects/Maker_Yocto
- http://knyeoh.blogspot.mx/2014/12/how-to-build-yocto-rt-for-minnowboard.html
- http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html
- http://www.yoctoproject.org/docs/latest/yocto-project-qs/yocto-project-qs.html
- http://git.yoctoproject.org/cgit/cgit.cgi/meta-minnow/tree/README?h=master

