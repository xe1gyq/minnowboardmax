# Camera

## Camera, Genius FaceCam 320X USB Camera
 http://www.geniusnet.com/Genius/wSite/ct?xItem=53156&ctNode=161 

## Camera, Fswebcam Installation
> Small and simple webcam for *nix

    root@Minnowboard:~# apt-get install fswebcam

## Camera, Kernel Drivers Tests
> Are the Camera drivers being installed correctly? 

This output shows that Camera is recognized by the Kernel but the **input/inputX** device is not set:

    user@Minnowboard:~$ dmesg
    [44070.765782] usb 1-2.3: new high-speed USB device number 8 using xhci_hcd
    [44070.887108] usb 1-2.3: New USB device found, idVendor=0458, idProduct=708a
    [44070.887118] usb 1-2.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    [44070.887124] usb 1-2.3: Product: FaceCam 320X
    [44070.887130] usb 1-2.3: Manufacturer: KYE Systems Corp.

This output shows that Camera is recognized by the Kernel and the input/inputX
device is set:

    user@sayulita:~$ dmesg
    [214180.239379] usb 2-1.1: new high-speed USB device number 6 using ehci-pci
    [214180.364693] usb 2-1.1: New USB device found, idVendor=0458, idProduct=708a
    [214180.364702] usb 2-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    [214180.364708] usb 2-1.1: Product: FaceCam 320X
    [214180.364712] usb 2-1.1: Manufacturer: KYE Systems Corp.
    [214180.367515] uvcvideo: Found UVC 1.00 device FaceCam 320X (0458:708a)
    [214180.373009] input: FaceCam 320X as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.1/2-1.1:1.0/input/input17

If your camera is recognized and the input/inputX device is set then go to "Camera, Kernel Modules Tests" section, otherwise keep reading

## Camera, Kernel Drivers Enablement

Compile your Kernel, once compiled let's enable all the required drivers
for our Camera:

    user@Minnowboard:~$ cd linux
    user@Minnowboard:~$ make menuconfig
    
    Device Drivers  --->
     <*> Multimedia support  --->
    
    Symbol: MEDIA_CAMERA_SUPPORT [=y]
    [*]   Cameras/video grabbers support
    Symbol: MEDIA_USB_SUPPORT [=y]
    [*]   Media USB Adapters  --->
    
    Device Drivers  --->
     <*> Multimedia support  ---> 
       [*]   Media USB Adapters  ---> 
    
    Symbol: USB_VIDEO_CLASS [=m]
    <M>   USB Video Class (UVC)
    Symbol: USB_VIDEO_CLASS_INPUT_EVDEV [=y]
    [*]     UVC input events device support

For FaceCam 320X the "required" controller (seems it uses another driver)
is GSPCA_PAC7302, we enable it as module

    Device Drivers  --->
     <*> Multimedia support  ---> 
       [*]   Media USB Adapters  ---> 
    
    Symbol: USB_GSPCA_PAC7302 [=n]
    <M>   Pixart PAC7302 USB Camera Driver

Once configuration changes are done, we save, compile again, reboot and check if Camera is recognized and input/inputX device is set as described in "Camera, Kernel Drivers Tests" section

## Camera, Kernel Modules Tests

Check some Camera Kernel modules that could be loaded

    user@Minnowboard:~$ lsmod
    Module                  Size  Used by
    uvcvideo               71309  0
    videobuf2_vmalloc      13048  1 uvcvideo
    videobuf2_memops       13170  1 videobuf2_vmalloc
    videobuf2_core         39258  1 uvcvideo
    videodev              108503  4 uvcvideo,gspca_main,gspca_pac7302,videobuf2_core
    gspca_pac7302          17233  0
    gspca_main             27814  1 gspca_pac7302

## Camera, Userspace Tests

We add our user as part of video group, look again that /dev/videoX is enabled
and finally we get our picture with fswebcam application

    root@Minnowboard:~# apt-get install fswebcam
    root@Minnowboard:~# adduser <user> video
    user@Minnowboard:~$ ls /dev/video*
    /dev/video0
    user@Minnowboard:~$ fswebcam -r 1280x1024 -s brightness=65% -s Contrast=50% -s Gamma=100% --jpeg 100 --no-banner image.jpg

# End of File
