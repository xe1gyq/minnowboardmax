#!/usr/bin/python

import mraa
import time

class Crgb(object):

    def __init__(self):

        self.red = 21
        self.green = 23
        self.blue = 26

        self.mcred = mraa.Gpio(self.red)
        self.mcred.dir(mraa.DIR_OUT)
        self.mcgreen = mraa.Gpio(self.green)
        self.mcgreen.dir(mraa.DIR_OUT)
        self.mcblue = mraa.Gpio(self.blue)
        self.mcblue.dir(mraa.DIR_OUT)

    def alloff(self):
        self.mcred.write(0)
        self.mcgreen.write(0)
        self.mcblue.write(0)

    def allon(self):
        self.mcred.write(1)
        self.mcgreen.write(1)
        self.mcblue.write(1)

    def start(self):
        print 'Hello Calamari RGB!'
        self.alloff()
        time.sleep(5)
        self.allon()

# End of File
