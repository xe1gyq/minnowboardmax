#!/usr/bin/python

import mraa
import os
import time

class Cbuttons(object):

    def __init__(self):

        self.button1 = 14
        self.button2 = 10
        self.button3 = 12

        self.mcb1 = mraa.Gpio(self.button1)
        self.mcb1.dir(mraa.DIR_IN)
        self.mcb2 = mraa.Gpio(self.button2)
        self.mcb2.dir(mraa.DIR_IN)
        self.mcb3 = mraa.Gpio(self.button3)
        self.mcb3.dir(mraa.DIR_IN)

    def start(self):

        print 'Hello Calamari Buttons!'

        while (1):
            os.system('clear')
            print self.mcb1.read()
            print self.mcb2.read()
            print self.mcb3.read()

# End of File
