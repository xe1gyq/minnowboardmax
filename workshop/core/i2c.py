#!/usr/bin/env python

import mraa as m

class I2c(object):

    def __init__(self):

        self.i2c = m.I2c(0)
        self.i2c.address(0x77)

    def read(self):

        print self.i2c.readReg(0xd0)
        self.i2c.writeReg(0xf4, 0x2e)
        print(str(self.i2c.readWordReg(0xf6)))
