#!/usr/bin/python

import mraa
import time

class C7seg(object):

    def __init__(self):

        self.clock = 25
        self.latch = 18
        self.data = 20
        self.clear = 16

        self.mcclock = mraa.Gpio(self.clock)
        self.mcclock.dir(mraa.DIR_OUT)
        self.mclatch = mraa.Gpio(self.latch)
        self.mclatch.dir(mraa.DIR_OUT)
        self.mcdata = mraa.Gpio(self.data)
        self.mcdata.dir(mraa.DIR_OUT)
        self.mcclear = mraa.Gpio(self.clear)
        self.mcclear.dir(mraa.DIR_OUT)

    def off(self):
        self.mcclock.write(0)
        self.mclatch.write(0)
        self.mcdata.write(0)
        self.mcclear.write(0)

    def allclear(self):
        self.mcclear.write(1)
        self.mcclear.write(0)
        self.mcclear.write(1)

    def tick(self):
        self.mcclock.write(1)
        self.mcclock.write(0)

    def dolatch(self):
        self.mclatch.write(0)
        self.mclatch.write(1)
        self.mclatch.write(0)

    def clock0in(self):
        self.mcdata.write(1)
        self.tick()

    def clock1in(self):
        self.mcdata.write(0)
        self.tick()

    def start(self):
        print 'Hello Calamari RGB!'
        self.off()
        self.allclear()

        self.clock0in()
        self.clock0in()
        self.clock0in()
        self.clock0in()
        self.clock0in()
        self.clock0in()
        self.clock0in()
        self.clock0in()
        self.dolatch()

        time.sleep(1)

        self.clock1in()
        self.clock1in()
        self.clock1in()
        self.clock1in()
        self.clock1in()
        self.clock1in()
        self.clock1in()
        self.clock1in()
        self.dolatch()        

# End of File
