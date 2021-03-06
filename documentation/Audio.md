# Audio

## Audio, Alsa-Utils Installation
> The ALSA Utilities package contains various utilities which are useful for controlling your sound card

    root@Minnowboard:~# apt-get install alsa-utils

## Audio, Kernel Drivers Tests
> Are the sound card drivers being installed correctly? 

Connect your USB Audio Device or Camera with built-in Microphone

    user@Minnowboard:~$ lsusb
    [62450.348474] usb 1-1.4: new full-speed USB device number 8 using xhci_hcd
    [62450.437700] usb 1-1.4: New USB device found, idVendor=0d8c, idProduct=013c
    [62450.437710] usb 1-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    [62450.437717] usb 1-1.4: Product: USB PnP Sound Device
    [62450.437723] usb 1-1.4: Manufacturer: C-Media Electronics Inc.      
    [62450.446465] input: C-Media Electronics Inc.       USB PnP Sound Device
    as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1.4/1-1.4:1.3/0003:0D8C:013C.0007/input/input14
    [62450.501053] hid-generic 0003:0D8C:013C.0007: input,hidraw3: USB HID v1.00 Device
    [C-Media Electronics Inc.       USB PnP Sound Device] on usb-0000:00:14.0-1.4/input3
    
    user@Minnowboard:~$ lsusb
    ...
    Bus 001 Device 008: ID 0d8c:013c C-Media Electronics, Inc. CM108 Audio Controller

List Capture Hardware Devices 

    user@Minnowboard:~$ arecord -l
    **** List of CAPTURE Hardware Devices ****
    card 1: C525 [HD Webcam C525], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 2: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

List Playback Hardware Devices

    user@Minnowboard:~$ aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: PCH [HDA Intel PCH], device 3: HDMI 0 [HDMI 0]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 0: PCH [HDA Intel PCH], device 7: HDMI 1 [HDMI 1]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 2: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

If your soundcard is recognized and the input/inputX device is set then go to "Alsa Utils, Test" section, otherwise keep reading

## Audio, Kernel Drivers Enablement

To be written

## Audio, Kernel Modules Tests

Looking at the Audio kernel modules, the list could look like this:

    user@sayulita:~$ lsmod | grep snd
    Module                  Size  Used by
    tbd

## Audio, Userspace Tests

Use command-line sound recorder and player for ALSA soundcard driver to test your device

    user@Minnowboard:~$ arecord -f cd -D plughw:1,0 -d 20 test.wav # Camera Built-In
    user@Minnowboard:~$ arecord -f cd -D plughw:2,0 -d 20 test.wav # USB
    user@Minnowboard:~$ aplay -D hw:2,0 test.wav # USB
    user@Minnowboard:~$ aplay -D hw:0,3 test.wav # HDMI
    
## Issues

http://lists.elinux.org/pipermail/elinux-minnowboard/Week-of-Mon-20150713/001759.html

# End of File
