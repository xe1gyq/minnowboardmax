# Software Defined Radio

Review http://backports.debian.org/Instructions/"

    # nano /etc/apt/sources.list
    deb http://http.debian.net/debian wheezy-backports main
    # apt-get update
    # apt-get install gnuradio gnuradio-dev
    # apt-get install rtl-sdr
    # apt-get -t wheezy-backports install libvolk-bin
    # apt-get -t wheezy-backports install gr-osmosdr
    # apt-get -t wheezy-backports install gqrx-sdr
    $ echo "Connect SDR"
    $ dmesg
    [2146267.913545] usb 1-2: new high-speed USB device number 14 using xhci_hcd
    [2146268.109208] usb 1-2: New USB device found, idVendor=0bda, idProduct=2838
    [2146268.109217] usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [2146268.109224] usb 1-2: Product: RTL2838UHIDIR
    [2146268.109230] usb 1-2: Manufacturer: Realtek
    [2146268.109235] usb 1-2: SerialNumber: 00000001
    $ lsusb
    Bus 001 Device 014: ID 0bda:2838 Realtek Semiconductor Corp. RTL2838 DVB-T
    $ rtl_test -t
    Found 1 device(s):
      0:  Realtek, RTL2838UHIDIR, SN: 00000001
    Using device 0: Generic RTL2832U OEM
    Found Rafael Micro R820T tuner
    Supported gain values (29): 0.0 0.9 1.4 2.7 3.7 7.7 8.7 12.5 14.4 15.7 16.6 19.7 20.7 22.9 25.4 28.0 29.7 32.8 33.8 36.4 37.2 38.6 40.2 42.1 43.4 43.9 44.5 48.0 49.6 
    Sampling at 2048000 S/s.
    No E4000 tuner found, aborting.
    $ rtl_fm -f 96.3e6 -M wbfm -s 200000 -r 48000 - | aplay -r 48k -f S16_LE

Do not follow this steps, Sandbox

    # rmmod dvb_usb_rtl28xxu rtl2832
    $ gqrx &
    $ nano /etc/modprobe.d/blacklist-sdr.conf
    blacklist dvb_usb_rtl28xx

Update the Apt cache:

    $ sudo apt-get update
    $ sudo apt-get install gnuradio gnuradio-dev libboost-all-dev libboost-thread-dev
    # blacklist dvb_usb_rtl28xxu
    $ sudo apt-get install rtl-sdr gr-osmosdr
    $ lusb
    Bus 001 Device 008: ID 0bda:2838 Realtek Semiconductor Corp. RTL2838 DVB-T
    # nano /etc/udev/rules.d/20.rtlsdr.rules
    SUBSYSTEM=="usb", ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="2838", GROUP="adm", MODE="0666", SYMLINK+="rtl_sdr"
    $ osmocom_fft

gr-air-modes

    $ sudo apt-get install sqlite pyqt4-dev-tools liblog4cpp5-dev swig
    $ git clone https://github.com/bistromath/gr-air-modes.git
    $ cd gr-air-modes
    $ mkdir build
    $ cd build
    $ cmake ../
    $ make
    $ sudo make install
    $ sudo ldconfig
    $ modes_rx -s osmocom

# HackRF PyBoombs

    apt-get update
    apt-get install python-dev python-qt4 cmake pkg-config libusb-dev libusb-1.0-0-dev
    git clone git://github.com/pybombs/pybombs
    cd pybombs
    ./pybombs install gnuradio
    ./pybombs install hackrf
    nano /etc/ld.so.conf.d/gnuradio.conf
     /home/xe1gyq/Projects/Radio/lib/
    ldconfig

## HackRF AptGet

    apt-get install gnuradio gnuradio-dev hackrf gr-osmosdr rtl-sdr gqrx-sdr git-core cmake g++ python-dev swig pkg-config libfftw3-dev libcppunit-dev libgsl0-dev libusb-dev libsdl1.2-dev python-numpy python-cheetah python-lxml doxygen libxi-dev python-sip libqt4-opengl-dev libqwt-dev libfontconfig1-dev libxrender-dev python-qwt5-qt4 python-sip python-sip-dev cmake xorg-dev libglu1-mesa-dev python-zmq pypy-zmq gedit

    $ hackrf_transfer -s 2 -f 147570000 -t test

# End of File



